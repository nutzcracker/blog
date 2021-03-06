# Generated by Django 3.2.8 on 2022-01-14 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('photo', models.ImageField(blank=True, upload_to='photos', verbose_name='Фото')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объект',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='photos', verbose_name='Фото')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('dossier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myblog.dossier', verbose_name='Досье')),
            ],
            options={
                'verbose_name': 'Снаряжение',
                'verbose_name_plural': 'Снаряжения',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_type', models.CharField(max_length=200, verbose_name='Особенность')),
                ('cat_description', models.CharField(max_length=200, null=True, verbose_name='Описание особенности')),
                ('dossier', models.ManyToManyField(blank=True, to='myblog.Dossier')),
            ],
            options={
                'verbose_name': 'Класс объекта',
                'verbose_name_plural': 'Класс объекта',
            },
        ),
    ]
