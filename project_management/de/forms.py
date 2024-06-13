from django import forms
from .models import ProjectInfo, Anggota, Pekerjaan, Aktivitas

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
    nama_project = forms.CharField(label='Nama Project :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan Nama Project'}))
    tujuan_project = forms.CharField(label='Tujuan Project :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan Tujuan Project'}))
    tangmul_project = forms.DateField(label='Tanggal Mulai Project', widget=forms.DateInput(attrs={'placeholder': "Masukkan Tanggal Mulai Proyek", 'type': 'date'}))
    tangsel_project = forms.DateField(label='Tanggal Selesai Project', widget=forms.DateInput(attrs={'placeholder': "Masukkan Tanggal Selesai Proyek", 'type': 'date'}))
    pic_project = forms.CharField(label='PIC Project :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan PIC Project'}))
    status_project = forms.ChoiceField(choices=STATE)

    class Meta:
        model = ProjectInfo
        exclude = ["tanggal_add"]

class AnggotaForm(forms.ModelForm):
    role_anggota = forms.ChoiceField(choices=ROLE)
    nama_ang = forms.CharField(label='Nama Anggota :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan Nama Anggota'}))
    tangla_ang = forms.DateField(label='Tanggal Lahir Anggota', widget=forms.DateInput(attrs={'placeholder': "Masukkan Tanggal Lahir Anggota", 'type': 'date'}))
    deskom_ang = forms.CharField(label='Deskripsi Kompetensi Anggota :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan Deskripsi Kompetensi Anggota'}))
    deskpen_ang = forms.CharField(label='Deskripsi Pengalaman Anggota :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan Deskripsi Pengalaman Anggota'}))
    peran_ang = forms.CharField(label='Peran Anggota :', widget=forms.Textarea(attrs={'placeholder': 'Masukkan Peran Anggota'}))

    class Meta:
        model = Anggota
        exclude = ["tanggal_add", "author"]
from django import forms
from .models import Pekerjaan

class PekerjaanForm(forms.ModelForm):
    nama_pek = forms.CharField(label='Nama Pekerjaan :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan Nama Pekerjaan'}))
    desk_pek = forms.CharField(label='Deskripsi Pekerjaan :', widget=forms.Textarea(attrs={'placeholder': 'Masukkan Deskripsi Pekerjaan'}))
    tangmul_pek = forms.DateField(label='Tanggal Mulai Pekerjaan', widget=forms.DateInput(attrs={'placeholder': "Masukkan Tanggal Mulai Pekerjaan", 'type': 'date'}))
    tempatmul_pek = forms.CharField(label='Tempat Mulai Pekerjaan :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan Tempat Mulai Pekerjaan'}))
    tangsel_pek = forms.DateField(label='Tanggal Selesai Pekerjaan', required=False, widget=forms.DateInput(attrs={'placeholder': "Masukkan Tanggal Selesai Pekerjaan", 'type': 'date'}))
    tempatsel_pek = forms.CharField(label='Tempat Selesai Pekerjaan :', required=False, widget=forms.TextInput(attrs={'placeholder': 'Masukkan Tempat Selesai Pekerjaan'}))
    pel_pek = forms.CharField(label='Pelaksana Pekerjaan :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan Pelaksana Pekerjaan'}))
    super_pek = forms.CharField(label='Supervisor Pekerjaan :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan Supervisor Pekerjaan'}))
    status_pek = forms.ChoiceField(label='Status Pekerjaan :', choices=STATE)

    class Meta:
        model = Pekerjaan
        exclude = ["author"]


class AktivitasForm(forms.ModelForm):
    nama_akti = forms.CharField(label='Nama Aktivitas :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan Nama Aktivitas'}))
    wakpel_akti = forms.DateField(label='Waktu Pelaksanaan Aktivitas', widget=forms.DateInput(attrs={'placeholder': "Masukkan Waktu Pelaksanaan Aktivitas", 'type': 'date'}))
    pel_akti = forms.CharField(label='Pelaksana Aktivitas :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan Pelaksana Aktivitas'}))
    eval_akti = forms.CharField(label='Evaluasi Aktivitas :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan Evaluasi Aktivitas'}))
    ren_akti = forms.CharField(label='Rencana Aktivitas :', widget=forms.TextInput(attrs={'placeholder': 'Masukkan Rencana Aktivitas'}))
    status_pek = forms.ChoiceField(label='Status Aktivitas :', choices=STATE)

    class Meta:
        model = Aktivitas
        exclude = ["pekerjaan"]
