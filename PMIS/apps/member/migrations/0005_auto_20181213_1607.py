# Generated by Django 2.0 on 2018-12-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20181213_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='home_address',
            field=models.CharField(choices=[('北部', '北部'), ('中部', '中部'), ('南部', '南部'), ('東部', '東部')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='working_school_address',
            field=models.CharField(choices=[('北部', '北部'), ('中部', '中部'), ('南部', '南部'), ('東部', '東部')], max_length=50, null=True),
        ),
    ]
