# Generated by Django 3.0.2 on 2020-01-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snach', '0002_auto_20200122_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]