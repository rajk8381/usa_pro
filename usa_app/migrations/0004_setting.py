# Generated by Django 3.1.3 on 2021-11-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usa_app', '0003_auto_20211119_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='uploads/videos')),
                ('video_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('about_company', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
