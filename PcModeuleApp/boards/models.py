from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CPU(models.Model):
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    codename = models.CharField(max_length=30)
    core = models.IntegerField(default=0)
    thread = models.IntegerField(default=0)
    clock = models.CharField(max_length=30)
    socket = models.CharField(max_length=30)
    process = models.CharField(max_length=30)
    tdp = models.CharField(max_length=30)

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)


class GPU(models.Model):
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    chip = models.CharField(max_length=30)
    bus = models.CharField(max_length=30)
    memory = models.CharField(max_length=30)
    gpu_clock = models.IntegerField(default=0)
    memory_clock = models.IntegerField(default=0)
    s_t_r = models.CharField(max_length=30)
    tdp = models.IntegerField(default=0)
    release_date = models.DateField()

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)


class Motherboard(models.Model):
    name = models.CharField(max_length=30)
    socket = models.CharField(max_length=10)
    ram_num = models.IntegerField(default=2)
    max_ram = models.IntegerField(default=0)
    m2_slot = models.BooleanField(default=False)
    power = models.IntegerField(default=0)
    brand = models.CharField(max_length=10)

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)


class RAM(models.Model):
    brand = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    speed = models.CharField(max_length=30)
    modules = models.CharField(max_length=30)

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)


class SSD(models.Model):
    brand = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    capacity = models.CharField(max_length=10)
    type = models.CharField(max_length=10)

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)


class HDD(models.Model):
    brand = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    capacity = models.CharField(max_length=10)
    type = models.CharField(max_length=10)

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)


class PC(models.Model):
    name = models.CharField(max_length=100)
    cpu = models.ForeignKey(CPU, related_name='cpu', on_delete=models.CASCADE)
    gpu = models.ForeignKey(GPU, related_name='gpu', on_delete=models.CASCADE)
    motherboard = models.ForeignKey(Motherboard, related_name='mb', on_delete=models.CASCADE)
    ram = models.ForeignKey(RAM, related_name='ram', on_delete=models.CASCADE)
    ssd = models.ForeignKey(SSD, related_name='ssd', on_delete=models.CASCADE)
    hdd = models.ForeignKey(HDD, related_name='hdd', on_delete=models.CASCADE)
    published_by = models.ForeignKey(User, related_name='publisher', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
