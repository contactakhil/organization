# Generated by Django 4.1 on 2022-08-26 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employees_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='total_salry',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
