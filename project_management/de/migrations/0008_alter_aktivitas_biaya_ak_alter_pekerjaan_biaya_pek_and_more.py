# Generated by Django 5.0.6 on 2024-06-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('de', '0007_aktivitas_biaya_ak_pekerjaan_biaya_pek_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktivitas',
            name='biaya_ak',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='pekerjaan',
            name='biaya_pek',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='biaya',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12),
        ),
    ]