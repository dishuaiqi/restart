# Generated by Django 2.0 on 2023-09-13 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20230913_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='tihuo',
            name='ren',
            field=models.CharField(default='zhangsan', max_length=64, verbose_name='提货人'),
        ),
        migrations.AlterField(
            model_name='tihuo',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 13, 18, 36, 18, 426421), verbose_name='提货日期'),
        ),
    ]
