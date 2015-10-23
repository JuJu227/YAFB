# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0007_auto_20151022_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default=123, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]
