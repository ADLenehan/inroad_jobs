from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth


class Company(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=1000)
    website = models.URLField(blank=True, null=True)
    email_domain = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='images/positions', null=True, blank=True)
    color = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


class Position(models.Model):
    company = models.ForeignKey(Company)
    experience = models.ForeignKey(Experience)
    created_on = models.DateTimeField(auto_now_add=True)
    indeed_id = models.CharField(max_length=16, null=True, blank=True)
    job_title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    url = models.CharField(max_length=125, null=True, blank=True)
    city = models.CharField(max_length=125, null=True, blank=True)
    state = models.CharField(max_length=125, null=True, blank=True)

    def __str__(self):
        return self.job_title

class Comment(models.Model):
    position = models.ForeignKey(Position)
    user = models.ForeignKey(UserSocialAuth)
