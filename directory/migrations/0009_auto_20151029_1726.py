# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0008_auto_20151022_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='office',
            old_name='Location',
            new_name='location',
        ),
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(blank=True, to='directory.Employee', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'profile_pictures', blank=True),
        ),
    ]
