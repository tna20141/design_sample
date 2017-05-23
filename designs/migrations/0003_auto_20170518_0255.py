# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0002_auto_20170517_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='path',
            field=models.CharField(max_length=100),
        ),
    ]
