# Generated by Django 2.0.6 on 2019-06-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0002_auto_20190627_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='headpic',
        ),
        migrations.AddField(
            model_name='employee',
            name='hobby',
            field=models.CharField(default='xx', max_length=20),
        ),
    ]