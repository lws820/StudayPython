# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-05 09:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='\u7f16\u53f7')),
                ('classname', models.CharField(max_length=36, verbose_name='\u73ed\u7ea7')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'grades',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_join', models.DateTimeField()),
            ],
            options={
                'db_table': 'membership',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.IntegerField(max_length=6, primary_key=True, serialize=False, verbose_name='\u5b66\u53f7')),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('age', models.CharField(max_length=3, verbose_name='\u5e74\u9f84')),
                ('tel', models.CharField(max_length=11, verbose_name='\u7535\u8bdd')),
                ('sex', models.CharField(max_length=10, verbose_name='\u6027\u522b')),
                ('birthday', models.DateTimeField(verbose_name='\u751f\u65e5')),
                ('gradeId', models.ForeignKey(db_column='gradeid', on_delete=django.db.models.deletion.CASCADE, related_name='g_set', to='APP.Grades')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.IntegerField(max_length=6, primary_key=True, serialize=False, verbose_name='\u79d1\u76ee\u7f16\u53f7')),
                ('sname', models.CharField(max_length=32)),
                ('subjectName', models.ManyToManyField(through='APP.Membership', to='APP.Students')),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.AddField(
            model_name='membership',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.Students'),
        ),
        migrations.AddField(
            model_name='membership',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.Subject'),
        ),
    ]
