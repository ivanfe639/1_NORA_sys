# Generated by Django 3.2.6 on 2021-08-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuperUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USER', models.CharField(max_length=30)),
                ('PASSWORD', models.CharField(max_length=50)),
            ],
        ),
    ]