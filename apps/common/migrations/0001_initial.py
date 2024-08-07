# Generated by Django 5.0.4 on 2024-07-19 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('release_date', models.DateField()),
                ('duration', models.PositiveIntegerField(blank=True, help_text='Duration in minutes', null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posters/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='common.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.FileField(upload_to='content_files/')),
                ('title', models.CharField(max_length=255)),
                ('episode_number', models.PositiveIntegerField()),
                ('duration', models.PositiveIntegerField(help_text='Duration in minutes')),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='common.content')),
            ],
            options={
                'unique_together': {('content', 'episode_number')},
            },
        ),
    ]
