from django.db import models
from django import forms
from datetime import date

# Create your models here.
class ProjectInfo(models.Model):
    nama_project=models.CharField(max_length= 100)
    tujuan_project= models.CharField(max_length= 1000)
    tangmul_project = models.DateField()
    tangsel_project = models.DateField()
    pic_project=models.CharField(max_length=40)
    status_project  = models.TextField()
    tanggal_add = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nama_project}'

class Anggota(models.Model):
    author =  models.ForeignKey(ProjectInfo,on_delete=models.CASCADE)
    nama_ang = models.CharField(max_length= 40)
    tangla_ang = models.DateField()
    deskom_ang = models.CharField(max_length=1000)
    deskpen_ang = models.CharField(max_length=1000)
    peran_ang = models.TextField()

