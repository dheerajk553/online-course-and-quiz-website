# Register your models here.
from django.contrib import admin
from .models import Course, Lesson
from .models import StudentProfile

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(StudentProfile)
