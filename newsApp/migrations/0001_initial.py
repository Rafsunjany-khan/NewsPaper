# Generated by Django 4.1.2 on 2022-10-10 17:18

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='AdsImage')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'ContactUs',
                'verbose_name_plural': 'ContactUs',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=800)),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[('national', 'national'), ('international', 'international'), ('entertainment', 'entertainment'), ('play', 'play')], max_length=255)),
                ('details', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date', models.DateField(default=datetime.datetime(2022, 10, 10, 17, 18, 43, 589501, tzinfo=datetime.timezone.utc))),
                ('image', models.ImageField(upload_to='NewsImage')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
