# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-11 12:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.storm.Category', verbose_name='文章分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.ManyToManyField(help_text='文章关键词，用来作为SEO中keywords，最好使用长尾词，3-4个足够', to='apps.storm.Keyword', verbose_name='文章关键词'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='apps.storm.Tag', verbose_name='标签'),
        ),
    ]
