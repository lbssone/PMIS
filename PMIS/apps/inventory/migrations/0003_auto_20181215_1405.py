# Generated by Django 2.0 on 2018-12-15 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20181208_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='u_feature',
            field=models.CharField(choices=[('抗UV', '抗UV'), ('防風', '防風'), ('輕量', '輕量')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='u_type',
            field=models.CharField(choices=[('直傘', '直傘'), ('自動摺傘', '自動摺傘'), ('手開摺傘', '手開摺傘')], max_length=50, null=True),
        ),
    ]
