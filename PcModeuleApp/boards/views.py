from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import NewPcForm
from .models import CPU, GPU, Motherboard, RAM, SSD, HDD, PC

# Create your views here.


def index(request):
    cpu_list = CPU.objects.all()[:5]
    gpu_list = GPU.objects.all()[:5]
    mb_list = Motherboard.objects.all()[:5]
    ram_list = RAM.objects.all()[:5]
    ssd_list = SSD.objects.all()[:5]
    hdd_list = HDD.objects.all()[:5]
    pc_list = PC.objects.all()[:5]

    return render(request, 'index.html', {'cpu_list': cpu_list,
                                          'gpu_list': gpu_list,
                                          'mb_list': mb_list,
                                          'ram_list': ram_list,
                                          'ssd_list': ssd_list,
                                          'hdd_list': hdd_list,
                                          'pc_list': pc_list})


class CpuIndexView(ListView):
    model = CPU
    template_name = 'cpu/index.html'
    paginate_by = 50


class CpuDetailView(DetailView):
    model = CPU
    template_name = 'cpu/detail.html'


class GpuIndexView(ListView):
    model = GPU
    template_name = 'gpu/index.html'
    paginate_by = 50


class GpuDetailView(DetailView):
    model = GPU
    template_name = 'gpu/detail.html'


def mb_index(request):
    mb_list = Motherboard.objects.all()
    return render(request, 'mb/index.html', {'mb_list': mb_list})


def mb_detail(request, mb_id):
    mb = Motherboard.objects.get(pk=mb_id)
    return render(request, 'mb/detail.html', {'mb': mb})


class RamIndexView(ListView):
    model = RAM
    template_name = 'ram/index.html'
    paginate_by = 50


class RamDetailView(DetailView):
    model = RAM
    template_name = 'ram/detail.html'


class SsdIndexView(ListView):
    model = SSD
    template_name = 'ssd/index.html'
    paginate_by = 50


class SsdDetailView(DetailView):
    model = SSD
    template_name = 'ssd/detail.html'


class HddIndexView(ListView):
    model = HDD
    template_name = 'hdd/index.html'
    paginate_by = 50


class HddDetailView(DetailView):
    model = HDD
    template_name = 'hdd/detail.html'


class PcIndexView(ListView):
    model = PC
    template_name = 'pc/index.html'
    paginate_by = 50


class PcDetailView(DetailView):
    model = PC
    template_name = 'pc/detail.html'


@login_required
def create_pc(request):
    if request.method == 'POST':
        form = NewPcForm(request.POST)
        if form.is_valid():
            pc = PC.objects.create(
                name=form.cleaned_data['name'],
                cpu=form.cleaned_data['cpu'],
                gpu=form.cleaned_data['gpu'],
                motherboard=form.cleaned_data['motherboard'],
                ram=form.cleaned_data['ram'],
                ssd=form.cleaned_data['ssd'],
                hdd=form.cleaned_data['hdd'],
                published_by=request.user
            )
        return redirect('modules:pc_detail', pk=pc.id)
    else:
        form = NewPcForm()
        return render(request, 'pc/new_pc.html', {'form': form})
