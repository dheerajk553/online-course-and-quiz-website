# Create your models here.

from django.contrib.auth.models import User
from django.db import models
#from django.contrib.auth.models import User

#from .models import Course

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    home_address = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='Student')
    enrolled_courses = models.ManyToManyField('Course', blank=True)

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

class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField(choices=[
        (1, 'Option 1'),
        (2, 'Option 2'),
        (3, 'Option 3'),
        (4, 'Option 4')
    ])

    def __str__(self):
        return f"{self.question[:30]} ({self.course.title})"


class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.IntegerField()
    passed = models.BooleanField(default=False)
    attempted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} - {self.score}/10"

