# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_employee_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='office',
            field=models.ForeignKey(default='1', to='directory.Office'),
            preserve_default=False,
        ),
    ]
