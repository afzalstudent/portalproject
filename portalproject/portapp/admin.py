from django.contrib import admin

# Register your models here.
from portapp.models import Department, Courses

admin.site.register(Department)
admin.site.register(Courses)
