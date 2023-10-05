# Generated by Django 2.0 on 2023-10-03 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20231002_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tihuo',
            options={'ordering': ['ren', 'today']},
        ),
        migrations.AlterField(
            model_name='custom_xiangqing',
            name='lilun_count',
            field=models.FloatField(verbose_name='理论提货量'),
        ),
        migrations.AlterField(
            model_name='custom_xiangqing',
            name='shiji_count',
            field=models.FloatField(verbose_name='理论提货量'),
        ),
        migrations.AlterField(
            model_name='custominfo',
            name='lirun',
            field=models.FloatField(default='0', verbose_name='利润'),
        ),
        migrations.AlterField(
            model_name='custominfo',
            name='use_credit',
            field=models.FloatField(verbose_name='使用额度'),
        ),
        migrations.AlterField(
            model_name='tihuo',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 3, 14, 33, 52, 984782), verbose_name='提货日期'),
        ),
        migrations.AlterField(
            model_name='tihuo',
            name='today_use',
            field=models.FloatField(verbose_name='今日支用'),
        ),
    ]
