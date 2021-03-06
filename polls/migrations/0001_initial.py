# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(blank=True, max_length=20, null=True)),
                ('voter_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Имя')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Choice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('ip_address', 'poll')]),
        ),
    ]
