# Generated by Django 4.1.4 on 2022-12-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=200)),
                ('año', models.IntegerField()),
            ],
        ),
    ]
