# Generated by Django 3.2.8 on 2022-02-21 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_dossier_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossier',
            name='url',
            field=models.SlugField(null=True),
        ),
    ]
