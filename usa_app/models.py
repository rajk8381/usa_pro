from django.db import models
import re
from django.core.validators import RegexValidator
from django.core import validators
from django.db.models.deletion import PROTECT, CASCADE
from django.db.models.fields import related
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

interest_choice = (
    ('', 'Select Interest '),
    ('Watching Movies', 'Watching Movies'),
    ('Singing', 'Singing'),
    ('Gardening', 'Gardening'),
    ('Reading Books', 'Reading Books'),
    ('Playing Cricket', 'Playing Cricket'),
)


class Joinus(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    interest = models.CharField(max_length=25, choices=interest_choice)
    comment=models.TextField()

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('joinform')

class Video(models.Model):
    video =models.FileField(upload_to="uploads/videos", null=True,blank=True)
    video_link=models.URLField(null=True,blank=True)
    video_text=models.TextField(blank=True,null=True)
    created_at =models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,
                        choices=(
                            ('1', "Active"),('2', "Inactive"),('3', "Blocked"),('4', "Spam"),),
                            default="1")
    def __str__(self):
        return "video "+ str(self.pk)
    class Meta:
        db_table ="video"


class Post(models.Model):
    image =models.ImageField(upload_to="uploads/photos", null=True,blank=True)
    title=models.TextField(blank=True,null=True)
    created_at =models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,
                        choices=(
                            ('1', "Active"),('2', "Inactive")),
                            default="1")
    def __str__(self):
        return self.title
    class Meta:
        db_table ="posts"

class Team(models.Model):
    image =models.ImageField(upload_to="uploads/photos", null=True,blank=True)
    name=models.CharField(blank=True,null=True,max_length=200)
    position=models.CharField(blank=True,null=True,max_length=200)
    created_at =models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,
                        choices=(
                            ('1', "Active"),('2', "Inactive")),
                            default="1")
    fb_link=models.URLField("Facebook URL",null=True,blank=True)
    tw_link=models.URLField("Twitter URL",null=True,blank=True)
    insta_link=models.URLField("Instagram URL",null=True,blank=True)
    linked_link=models.URLField("Linked URL",null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table ="team"

class Setting(models.Model):
    video = models.FileField(upload_to="uploads/videos", null=True, blank=True)
    logo =models.ImageField(upload_to="uploads/logo",null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    company_name=models.CharField(max_length=50,null=True, blank=True)
    about_company=models.TextField(null=True, blank=True)
    phone =models.CharField(max_length=10, null=True, blank=True)
    email =models.EmailField(null=True,blank=True)
    website_link =models.URLField("Website",null=True, blank=True)
    address =models.TextField("Company Address",null=True, blank=True)
    fb_link = models.URLField("Facebook URL", null=True, blank=True)
    tw_link = models.URLField("Twitter URL", null=True, blank=True)
    insta_link = models.URLField("Instagram URL", null=True, blank=True)
    skype_link = models.URLField("Skype URL", null=True, blank=True)
    linked_link = models.URLField("Linked URL", null=True, blank=True)

    class Meta:
        db_table ="setting"

class FileManagement(models.Model):
    file_type=models.CharField(max_length=1,
                        choices=(
                            ('1', "PDF File"),('2', "Xls File"),),
                            default="1")
    file =models.FileField(upload_to="uploads/files", null=True)
    created_at = models.DateTimeField(auto_now=True)
