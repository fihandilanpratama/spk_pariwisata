# Generated by Django 3.2.9 on 2021-12-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekomendasi', '0003_alter_wisata_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wisata',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
