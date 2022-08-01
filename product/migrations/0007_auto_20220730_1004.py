# Generated by Django 3.1 on 2022-07-30 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20220729_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productvariation',
            old_name='description',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='productvariation',
            old_name='value',
            new_name='title',
        ),
        migrations.AlterUniqueTogether(
            name='productvariation',
            unique_together={('product', 'title')},
        ),
    ]