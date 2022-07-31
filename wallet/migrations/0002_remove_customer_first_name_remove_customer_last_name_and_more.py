# Generated by Django 4.0.6 on 2022-07-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='firstname',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='lastname',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phonenumber',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
