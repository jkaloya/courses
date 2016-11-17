from __future__ import unicode_literals

from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Description(models.Model):
    courses = models.OneToOneField(Courses, primary_key=True)
    description = models.TextField(max_length=5000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Comments(models.Model):
    courses = models.OneToOneField(Courses, primary_key=True)
    description = models.TextField(max_length=5000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
