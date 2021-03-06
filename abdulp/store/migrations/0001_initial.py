# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 00:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=80)),
                ('secondName', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('isPhysical', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nType', models.CharField(max_length=50)),
                ('benefit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NotebookOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('NS', 'Not Started'), ('PP', 'Preparing...'), ('DO', 'Done'), ('SH', 'Shipping...'), ('SD', 'Shipped')], default='NS', max_length=2)),
                ('notebook', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Notebook')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('priority', models.CharField(choices=[('H', 'High'), ('N', 'Normal'), ('L', 'Low')], default='L', max_length=1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='notebookorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order'),
        ),
        migrations.AddField(
            model_name='notebookorder',
            name='page',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Page'),
        ),
    ]
