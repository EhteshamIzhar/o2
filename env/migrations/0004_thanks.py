# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 05:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('env', '0003_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='thanks',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user', serialize=False, to='env.user_auth')),
                ('thanks_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thanks_from', to='env.user_auth')),
            ],
        ),
    ]
