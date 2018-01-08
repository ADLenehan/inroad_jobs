from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


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


class Board(models.Model):
    author = models.ForeignKey(User)
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    logo = models.ImageField(blank=True, null=True, upload_to='images/publishers', default='images/publishers/no-image.png')

    def __str__(self):
        return self.slug


class Position(models.Model):
    company = models.ForeignKey(Company)
    experience = models.ForeignKey(Experience)
    board = models.ForeignKey(Board)
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
    position = models.ForeignKey(Position, default=1)
    company = models.CharField(max_length=200, blank=False, null=False)
    user_position = models.CharField(max_length=200, blank=False, null=False)
    text = models.TextField()
    picture_url = models.URLField(blank=True, null=True)


class SavedJobs(models.Model):
    user = models.ForeignKey(User)
    position = models.ForeignKey(Position)
    active = models.BooleanField(default=False)
    applied = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s" % (self.user, self.position)


class Application(models.Model):
    user = models.ForeignKey(User)
    position = models.ForeignKey(Position)
    question1 = models.CharField(max_length=1000, null=False, blank=False)
    question2 = models.CharField(max_length=1000, null=False, blank=False)
    checked = models.BooleanField(default=False)
    fit = models.IntegerField(default=0)