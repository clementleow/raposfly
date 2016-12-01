# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20161127_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='shop.Item')),
            ],
        ),
        migrations.RemoveField(
            model_name='composition',
            name='item',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='purchase',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='items',
            field=models.ManyToManyField(through='shop.Order', to='shop.Item'),
        ),
        migrations.DeleteModel(
            name='Composition',
        ),
        migrations.AddField(
            model_name='order',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='shop.Purchase'),
        ),
    ]
