from django.db import models

class ProjectInfo(models.Model):
    nama_project = models.CharField(max_length=100)
    tujuan_project = models.CharField(max_length=1000)
    tangmul_project = models.DateField()
    tangsel_project = models.DateField()
    pic_project = models.CharField(max_length=40)
    status_project = models.TextField()
    tanggal_add = models.DateField(auto_now=True)
    biaya = models.DecimalField(max_digits=12,decimal_places=2,default=0.00,blank=True,null=True)
    is_archived = models.BooleanField(default=False)
    signature_picture = models.ImageField(upload_to='signatures/', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.nama_project}'

class Pekerjaan(models.Model):
    project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE, related_name='pekerjaan', default=1)
    nama_pek = models.CharField(max_length=40)
    desk_pek = models.CharField(max_length=1000)
    tangmul_pek = models.DateField()
    tempatmul_pek = models.CharField(max_length=1000)
    tangsel_pek = models.DateField(blank=True, null=True)
    tempatsel_pek = models.CharField(max_length=1000, blank=True, null=True)
    pel_pek = models.CharField(max_length=1000)
    super_pek = models.CharField(max_length=50)
    status_pek = models.TextField()
    biaya_pek = models.DecimalField(max_digits=12,decimal_places=2,default=0.00,blank=True, null=True)


    def __str__(self) -> str:
        return f'{self.nama_pek}'
    

class Aktivitas(models.Model):
    pekerjaan = models.ForeignKey(Pekerjaan, on_delete=models.CASCADE, related_name='aktivitas' ,  default=1)
    nama_akti = models.CharField(max_length=50)
    wakpel_akti = models.DateField()
    pel_akti = models.CharField(max_length=1000)
    eval_akti = models.CharField(max_length=1000)
    ren_akti = models.CharField(max_length=1000)
    status_akti = models.TextField()
    biaya_akti = models.DecimalField(max_digits=12,decimal_places=2,default=0.00)

    def __str__(self) -> str:
        return f'{self.nama_akti}'
