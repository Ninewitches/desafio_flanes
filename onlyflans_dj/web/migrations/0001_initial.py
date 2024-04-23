# Generated by Django 4.2.11 on 2024-04-22 21:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flan_uuid', models.UUIDField(default=uuid.uuid4)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('slug', models.SlugField(unique=True)),
                ('isprivate', models.BooleanField(default=False)),
            ],
        ),
    ]
