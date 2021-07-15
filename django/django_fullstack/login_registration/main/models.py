from django.db import models
from datetime import datetime
from time import strftime, strptime
from django.db.models.fields import CharField, DateField
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        date_format = "%Y-%m-%d"
        birthday = postData['birthday']
        
        if len(postData['first']) < 2:
            errors["first"] = "First name must have at least 2 characters"
        if len(postData['last']) < 2:
            errors["last"] = "Last name must have at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        if postData['password'] != postData['confirm_password']:
            errors["password"] = "Passwords don't match"
        if len(postData['password']) < 8 or len(postData['password']) > 16:
            errors["password"] = "Password must be 8-16 charachters long"
        if len(postData['birthday']) == 0:
            errors["birthday"] = "Birthday is required"
        else:
            a = datetime.strptime(str(datetime.now().date()), date_format)
            b = datetime.strptime(str(birthday), date_format)
            delta = b - a
            if delta.days >=-4745:
                errors["birthday"] = "Must be at least 13 years of age to sign up"
        print(errors)
        return errors

# Create your models here.

class User(models.Model):
    #id
    first = CharField(max_length=200)
    last = CharField(max_length=200)
    email = CharField(max_length=200)
    password = CharField(max_length=16)
    birthday = DateField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()