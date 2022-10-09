# Generated by Django 3.2.12 on 2022-08-08 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0005_alter_categ_options'),
        ('cart', '0003_auto_20220808_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=250, unique=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quant', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartlist')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
