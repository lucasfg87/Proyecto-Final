# Generated by Django 4.1.4 on 2023-01-10 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('argentina', '0005_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='sub_titulo',
        ),
        migrations.RemoveField(
            model_name='about',
            name='titulo',
        ),
    ]
