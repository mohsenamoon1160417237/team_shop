# Generated by Django 3.1 on 2022-07-30 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20220730_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defineproduct',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=200),
        ),
    ]