# Generated by Django 3.1 on 2021-11-06 03:15

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitemanage', '0002_siteconfig_blog_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfig',
            name='top_subtitle',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='TOPページサブタイトル'),
        ),
    ]
