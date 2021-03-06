# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 09:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadlift', models.FloatField(default='0')),
                ('oh_press', models.FloatField(default='0')),
                ('barbell_row', models.FloatField(default='0')),
                ('bench_press', models.FloatField(default='0')),
                ('squat', models.FloatField(default='0')),
                ('pull_ups', models.IntegerField(default='0')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
