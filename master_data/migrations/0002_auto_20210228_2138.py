# Generated by Django 2.2.10 on 2021-02-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='fiscalyear',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gender',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='locallevel',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='localleveltype',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='nepalimonth',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
    ]
