from django.db import models
from django.db.models.fields import CharField, DateField
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(postData['first']) < 2:
            errors["first"] = "First name must have at least 2 characters"
        if len(postData['last']) < 2:
            errors["last"] = "Last name must have at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        if postData['password'] != postData['confirm_password']:
            errors["password"] = "Passwords don't match"
        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 charachters long"
        return errors


class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        print(postData)

        if len(postData['title']) < 1:
            errors["title"] = "Show title should be at least 1 character"
        if len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 10 characters"
        return errors

# Create your models here.

class User(models.Model):
    #id
    first = CharField(max_length=200)
    last = CharField(max_length=200)
    email = CharField(max_length=200)
    password = CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # books_uploaded: books uploaded by the User
    # liked_books: books favorited by the User

class Book(models.Model):
    #id
    title = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
