# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_employee_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='writer',
            field=models.ForeignKey(to='directory.Employee'),
        ),
    ]
