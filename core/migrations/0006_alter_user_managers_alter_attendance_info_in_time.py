# Generated by Django 4.0.4 on 2022-06-01 12:55

import datetime
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_last_login_alter_attendance_info_in_time'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='attendance_info',
            name='in_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 14, 55, 13, 761816)),
        ),
    ]