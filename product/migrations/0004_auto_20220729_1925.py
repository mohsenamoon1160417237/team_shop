# Generated by Django 3.1 on 2022-07-29 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_defineproduct_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productvariation',
            unique_together={('product', 'value')},
        ),
    ]
