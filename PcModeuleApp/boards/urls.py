from django.urls import path

from . import views

app_name = 'modules'
urlpatterns = [
    path('', views.index, name='home'),

    path('cpu/', views.CpuIndexView.as_view(), name='cpu'),
    path('gpu/', views.GpuIndexView.as_view(), name='gpu'),
    path('mb/', views.mb_index, name='mb'),
    path('ram/', views.RamIndexView.as_view(), name='ram'),
    path('ssd/', views.SsdIndexView.as_view(), name='ssd'),
    path('hdd/', views.HddIndexView.as_view(), name='hdd'),
    path('pc/', views.PcIndexView.as_view(), name='pc'),

    path('cpu/<int:pk>/detail/', views.CpuDetailView.as_view(), name='cpu_detail'),
    path('gpu/<int:pk>/detail/', views.GpuDetailView.as_view(), name='gpu_detail'),
    path('mb/<int:mb_id>/detail/', views.mb_detail, name='mb_detail'),
    path('ram/<int:pk>/detail/', views.RamDetailView.as_view(), name='ram_detail'),
    path('ssd/<int:pk>/detail', views.SsdDetailView.as_view(), name='ssd_detail'),
    path('hdd/<int:pk>/detail', views.HddDetailView.as_view(), name='hdd_detail'),
    path('pc/<int:pk>/detail', views.PcDetailView.as_view(), name='pc_detail'),

    path('pc/new/', views.create_pc, name='create_pc'),
]
