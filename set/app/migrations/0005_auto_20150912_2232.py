# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150909_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbalance',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserBalance',
        ),
    ]
