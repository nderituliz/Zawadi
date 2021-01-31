# Generated by Django 3.1.5 on 2021-01-31 20:31

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name=django.contrib.auth.models.User)),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('image2', pyuploadcare.dj.models.ImageField(null=True)),
                ('description', models.TextField(max_length=200)),
                ('url', models.URLField(blank=True, default='', null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', pyuploadcare.dj.models.ImageField()),
                ('bio', models.TextField(default='Here is my bio...')),
                ('contact', models.CharField(max_length=30)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ManyToManyField(to='rateme.Projects')),
            ],
        ),
    ]
