from django.shortcuts import render

# Create views here.

from .models import Lesson

@login_required
def lesson_list_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lessons.all()
    return render(request, 'courses/lesson_list.html', {'course': course, 'lessons': lessons})

