# Generated by Django 2.0 on 2018-12-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('member_number', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=2)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('occupation', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
