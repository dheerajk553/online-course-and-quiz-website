# Register your models here.
from django.contrib import admin
from .models import Course, Lesson

admin.site.register(Course)
admin.site.register(Lesson)
