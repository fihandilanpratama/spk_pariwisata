# Generated by Django 3.2.9 on 2021-12-21 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekomendasi', '0006_auto_20211220_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='nama',
            field=models.CharField(default='RX', max_length=10),
        ),
    ]
