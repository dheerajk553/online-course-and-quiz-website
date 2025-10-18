# Register your models here.
from django.contrib import admin
from .models import Course, Lesson
from .models import StudentProfile
#from .models import Course, Lesson, Quiz, Question, StudentProfile, Certificate

admin.site.register(Course)
admin.site.register(Lesson)
#admin.site.register(Quiz)
admin.site.register(StudentProfile)
#admin.site.register(Question)
#admin.site.register(Certificate)
