# Generated by Django 3.0.2 on 2020-01-22 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snach', '0003_auto_20200122_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snach.Seller'),
        ),
    ]
