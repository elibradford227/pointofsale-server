# Generated by Django 4.1.3 on 2024-01-17 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointofsaleapi', '0004_alter_orderitem_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenue',
            name='tip',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='total',
            field=models.FloatField(),
        ),
    ]