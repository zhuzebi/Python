# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-15 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Args',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mod_args', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=20)),
                ('ip_addr', models.CharField(max_length=15)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webansi.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mod_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='args',
            name='mod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webansi.Module'),
        ),
    ]
