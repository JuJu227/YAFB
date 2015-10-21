# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='full_name',
            field=models.CharField(default='Vanessa Sergeon', max_length=100),
            preserve_default=False,
        ),
    ]
