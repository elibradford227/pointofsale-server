# Generated by Django 4.1.3 on 2024-01-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointofsaleapi', '0002_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(),
        ),
    ]