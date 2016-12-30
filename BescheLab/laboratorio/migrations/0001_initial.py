# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
            ],
        ),
    ]