# Generated by Django 4.0.4 on 2022-06-01 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_user_options_rename_isadmin_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_info',
            name='in_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 16, 48, 2, 732687)),
        ),
    ]