# Generated by Django 3.0.2 on 2020-01-19 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_remove_attendreport_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendreport',
            name='office_branch',
            field=models.CharField(default='I2IT', max_length=50),
        ),
    ]
