# Generated by Django 2.0.6 on 2019-06-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0004_auto_20190628_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='headpic',
            field=models.ImageField(upload_to='pics'),
        ),
    ]