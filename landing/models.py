# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Purpose(models.Model):
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary


class SignUp (models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, blank=False, unique=True,
                              error_messages={'required': 'Please provide your email address.',
                                              'unique': 'An account with this email exist.'},)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    purpose = models.ForeignKey(Purpose, default=1)

    def __str__(self):
        return self.email
