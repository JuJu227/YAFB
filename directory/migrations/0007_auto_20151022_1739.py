# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0006_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'profile_pictures'),
        ),
        migrations.AlterField(
            model_name='message',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
