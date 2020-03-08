from django.contrib import admin

from .models import CPU, GPU, Motherboard, RAM, SSD, HDD, PC
# Register your models here.


admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(Motherboard)
admin.site.register(RAM)
admin.site.register(SSD)
admin.site.register(HDD)
admin.site.register(PC)