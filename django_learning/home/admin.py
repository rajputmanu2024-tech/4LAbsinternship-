from django.contrib import admin

# Register your models here.
from .models import student, address

admin.site.register(student)
admin.site.register(address)