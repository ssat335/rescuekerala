# Generated by Django 2.1 on 2018-08-17 23:46

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0038_auto_20180817_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=15, verbose_name='Phone (eg +919898989899)'),
        ),
        migrations.AlterField(
            model_name='districtmanager',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=15, verbose_name='Phone (eg +919898989899)'),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=15, verbose_name='Phone (eg +919898989899)'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=15, verbose_name='Phone (eg +919898989899)'),
        ),
    ]
