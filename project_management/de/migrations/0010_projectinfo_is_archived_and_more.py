# Generated by Django 5.0.6 on 2024-06-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('de', '0009_alter_aktivitas_biaya_ak_alter_pekerjaan_biaya_pek_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectinfo',
            name='signature_picture',
            field=models.ImageField(blank=True, null=True, upload_to='signatures/'),
        ),
        migrations.AlterField(
            model_name='aktivitas',
            name='biaya_ak',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
