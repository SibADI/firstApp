# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('target', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('place', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('vk', models.EmailField(max_length=255)),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField()),
                ('meeting', models.ForeignKey(null='true', on_delete=django.db.models.deletion.CASCADE, to='firstApp.Meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RunQuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('first_date', models.DateTimeField()),
                ('last_date', models.DateTimeField()),
                ('person', models.ForeignKey(null='true', on_delete=django.db.models.deletion.CASCADE, to='firstApp.Person')),
                ('quest', models.ForeignKey(null='true', on_delete=django.db.models.deletion.CASCADE, to='firstApp.Quest')),
            ],
        ),
        migrations.CreateModel(
            name='SysJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datein', models.DateTimeField()),
                ('dateout', models.DateTimeField()),
                ('person', models.ForeignKey(null='true', on_delete=django.db.models.deletion.CASCADE, to='firstApp.Person')),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='quest',
            field=models.ForeignKey(null='true', on_delete=django.db.models.deletion.CASCADE, to='firstApp.Quest'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='persons',
            field=models.ManyToManyField(through='firstApp.Journal', to='firstApp.Person'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='plans',
            field=models.ManyToManyField(through='firstApp.Plan', to='firstApp.Quest'),
        ),
        migrations.AddField(
            model_name='journal',
            name='meeting',
            field=models.ForeignKey(null='true', on_delete=django.db.models.deletion.CASCADE, to='firstApp.Meeting'),
        ),
        migrations.AddField(
            model_name='journal',
            name='person',
            field=models.ForeignKey(null='true', on_delete=django.db.models.deletion.CASCADE, to='firstApp.Person'),
        ),
    ]
