from django.core.checks.messages import Error
from django.db import models

# Create your models here.

class Show(models.Model):
    #id
    title = models.CharField(max_length=200)
    network = models.CharField(max_length=200)
    release_date = models.DateField(auto_now=False)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ShowManager(models.Manager):
    def basic_validator(self, PostData):
        errors = {}
        if len(postData['title']) < 1:
            errors["name"] = "Show title should be at least 1 character"
        if len(postData['network'])<2:
            errors["network"] = "Network name should be at least 2 characters"
        if postData['release_date'] is None:
            errors["release_date"] = "There must be a release date"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors
