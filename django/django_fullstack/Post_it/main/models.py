from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Note(models.Model):
    #id
    text = TextField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"