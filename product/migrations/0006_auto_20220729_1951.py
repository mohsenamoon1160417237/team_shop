# Generated by Django 3.1 on 2022-07-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productvariation_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='defineproduct',
            name='stock_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='defineproduct',
            name='sales_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]