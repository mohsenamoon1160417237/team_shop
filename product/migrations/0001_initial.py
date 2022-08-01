# Generated by Django 3.1 on 2022-07-29 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefineProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('note', models.TextField(blank=True, null=True)),
                ('sales_count', models.PositiveBigIntegerField(default=0)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product_category.productcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.PositiveBigIntegerField()),
                ('sale_price', models.PositiveBigIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prop', to='product.defineproduct')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProdPreOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.defineproduct')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.defineproduct')),
            ],
            options={
                'unique_together': {('product', 'title')},
            },
        ),
    ]