# Generated by Django 2.0 on 2018-12-12 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='cellphone_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='member',
            name='home_address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='working_address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_number',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
