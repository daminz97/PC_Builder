from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from .forms import UserCreationForm


# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserCreationForm

    success_url = reverse_lazy('accounts:login')
    template_name = 'signup.html'


class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('username', 'email')
    template_name = 'my_account.html'
    success_url = reverse_lazy('modules:home')

    def get_object(self, queryset=None):
        return self.request.user
