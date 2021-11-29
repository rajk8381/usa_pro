# Generated by Django 3.2.9 on 2021-11-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usa_app', '0006_auto_20211124_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='fb_link',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook URL'),
        ),
        migrations.AddField(
            model_name='setting',
            name='insta_link',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram URL'),
        ),
        migrations.AddField(
            model_name='setting',
            name='linked_link',
            field=models.URLField(blank=True, null=True, verbose_name='Linked URL'),
        ),
        migrations.AddField(
            model_name='setting',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/logo'),
        ),
        migrations.AddField(
            model_name='setting',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='skype_link',
            field=models.URLField(blank=True, null=True, verbose_name='Skype URL'),
        ),
        migrations.AddField(
            model_name='setting',
            name='tw_link',
            field=models.URLField(blank=True, null=True, verbose_name='Twitter URL'),
        ),
        migrations.AddField(
            model_name='setting',
            name='website_link',
            field=models.URLField(blank=True, null=True, verbose_name='website'),
        ),
    ]
