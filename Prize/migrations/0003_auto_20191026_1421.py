# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-26 12:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Prize', '0002_projects_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='user',
            new_name='username',
        ),
    ]
