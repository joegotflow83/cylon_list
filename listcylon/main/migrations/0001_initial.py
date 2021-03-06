# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 23:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Post')),
                ('brand', models.CharField(choices=[('Acura', 'Acura'), ('Audi', 'Audi'), ('BMW', 'BMW'), ('Buick', 'Buick'), ('Cheverolet', 'Cheverolet'), ('Dodge', 'Dodge'), ('Ferrai', 'Ferrai'), ('Ford', 'Ford'), ('Lamborghini', 'Lamborghini'), ('Mclaren', 'Mclaren'), ('Mercedes', 'Mercedes'), ('Mitusbishi', 'Mitsubishi'), ('Pagani', 'Pagani'), ('Porsche', 'Porsche'), ('Subaru', 'Subaru'), ('Tesla', 'Tesla'), ('Volkswagen', 'Volkwagen')], max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('condition', models.CharField(max_length=255)),
                ('cylinders', models.CharField(max_length=32)),
                ('drive', models.CharField(max_length=3)),
                ('odometer', models.CommaSeparatedIntegerField(max_length=8)),
                ('color', models.CharField(max_length=32)),
                ('transmission', models.CharField(max_length=20)),
                ('car_type', models.CharField(max_length=32)),
                ('price', models.CommaSeparatedIntegerField(max_length=15)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            bases=('main.post',),
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Post')),
                ('condition', models.CharField(max_length=255)),
                ('year_built', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('baths', models.FloatField()),
                ('square_feet', models.CommaSeparatedIntegerField(max_length=7)),
                ('price', models.CommaSeparatedIntegerField(max_length=15)),
                ('mortgage', models.CommaSeparatedIntegerField(max_length=7)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            bases=('main.post',),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Post')),
                ('category', models.CharField(choices=[('Accounting', 'Accounting'), ('Buisness', 'Buisness'), ('Education', 'Education'), ('Real Estate', 'Real Estate'), ('Government', 'Government'), ('Technology', 'Technology')], max_length=64)),
                ('highlight_skills', models.CharField(max_length=255)),
                ('plus_skills', models.CharField(max_length=255)),
                ('compensation', models.CharField(max_length=12)),
                ('employment_type', models.CharField(max_length=15)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            bases=('main.post',),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
