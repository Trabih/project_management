
from django import forms
from .models import ProjectInfo,Anggota


STATE = (
    ('', 'CHOOSE STATE OF PROJECT ... '),
    ('Fn', 'Finished'),
    ('Pr', 'Progress'),
    ('Er', 'Error')
)

ROLE = (
    ('', 'CHOOSE ROLE ... '),
    ('P0W', 'Project Owner'),
    ('PO', 'Product Owner'),
    ('MAS', 'Master'),
    ('KS', 'Ketua Sprint'),
    ('A', 'Anggota'),
)

class ProjectForm(forms.ModelForm):
    nama_project=forms.CharField(label='Nama Project :',widget=forms.TextInput(attrs={'placeholder':'Masukkan Nama Project'}))
    tujuan_project= forms.CharField(label='Tujuan Project :',widget=forms.TextInput(attrs={'placeholder':'Masukkan Tujuan Project'}))
    tangmul_project = forms.DateField(label='Tanggal Mulai Project', widget= forms.DateInput(attrs={'placeholder' : "Masukkan Tanggal Mulai Proyek", 'type': 'date'}))
    tangsel_project = forms.DateField(label='Tanggal Selesai Project', widget= forms.DateInput(attrs={'placeholder' : "Masukkan Tanggal Selesai Proyek", 'type': 'date'}))
    pic_project=forms.CharField(label='PIC Project :',widget=forms.TextInput(attrs={'placeholder':'Masukkan PIC Project'}))
    status_project  = forms.ChoiceField(choices = STATE)

    class Meta: 
        model = ProjectInfo
        exclude = ["tanggal_add"]

class AnggotaForm(forms.ModelForm):
    role_anggota = forms.ChoiceField(choices = ROLE)
    class Meta:
        model = Anggota
        exclude = ["tanggal_add"]




