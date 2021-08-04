from main.models import Note as Notes
from django.contrib import admin

class UAdmin(admin.ModelAdmin):
    pass

admin.site.register(Notes, UAdmin)

# Register your models here.
