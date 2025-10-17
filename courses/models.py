
# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    home_address = models.TextField()
    status = models.CharField(max_length=10, choices=[('Student', 'Student'), ('Working', 'Working')])

    def __str__(self):
        return self.full_name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #instructor = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    #image = models.ImageField(upload_to='lesson_images/', blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

