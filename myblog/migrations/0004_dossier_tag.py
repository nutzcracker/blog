# Generated by Django 3.2.8 on 2022-02-18 09:47

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('myblog', '0003_alter_dossier_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossier',
            name='tag',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
