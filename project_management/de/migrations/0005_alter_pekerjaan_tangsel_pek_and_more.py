# Generated by Django 5.0.6 on 2024-06-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('de', '0004_remove_anggota_author_anggota_project_pekerjaan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pekerjaan',
            name='tangsel_pek',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pekerjaan',
            name='tempatsel_pek',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
