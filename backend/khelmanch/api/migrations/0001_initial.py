# Generated by Django 4.1.1 on 2022-09-16 09:04

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('profilepic', models.ImageField(default='profilepic.jpg', upload_to=api.models.save_image)),
                ('address', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('rating', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('playerid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('profilepic', models.ImageField(default='profilepic.jpg', upload_to=api.models.save_image)),
                ('profileCreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.creator')),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.sport')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('view_count', models.IntegerField(blank=True, default=0, null=True)),
                ('rating', models.FloatField(default=0.0)),
                ('contentCreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.creator')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.player')),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.sport')),
            ],
        ),
    ]
