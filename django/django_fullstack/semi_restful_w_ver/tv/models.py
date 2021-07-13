from django.core.checks.messages import Error
from django.db import models
from datetime import datetime, date
import time

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        date = postData['release_date']
        today = datetime.today().date()
        print(today)

        if len(postData['title']) < 1:
            errors["name"] = "Show title should be at least 1 character"
        if len(postData['network']) < 2:
            errors["network"] = "Network name should be at least 2 characters"
        if len(date) == 0:
            errors["release_date"] = "There must be a release date"
        # else:
        #     date(0) > today(0)
        #     errors["release_date"] = "This show will be realsed in the future"
        if len(postData['desc']) == 0:
            return errors
        if len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 10 characters"
        return errors

class Show(models.Model):
    #id
    title = models.CharField(max_length=200)
    network = models.CharField(max_length=200)
    release_date = models.DateField(auto_now=False)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
