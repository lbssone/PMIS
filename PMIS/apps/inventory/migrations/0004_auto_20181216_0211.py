# Generated by Django 2.0 on 2018-12-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20181215_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='level',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='level',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='level',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]