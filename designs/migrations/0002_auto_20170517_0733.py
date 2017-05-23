# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='path',
            field=models.FilePathField(path='/home/tna/workspace/virtualhosts/design_sample/design_sample/media/products'),
        ),
    ]
