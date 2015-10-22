# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0003_auto_20151022_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='groups',
            field=models.ManyToManyField(to='directory.GroupProfile'),
        ),
    ]
