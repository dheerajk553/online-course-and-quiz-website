from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import StudentRegisterForm
from .models import StudentProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Course
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Lesson
from .models import Course, Lesson
#from courses.views import mark_complete

#from .models import Lesson, LessonProgress

@login_required
def dashboard_view(request):
    return render(request, 'courses/dashboard.html')



def register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)

            profile = form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('login')  # Or redirect to dashboard
    else:
        form = StudentRegisterForm()

    return render(request, 'courses/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('course_menu')
        else:
            error = "Invalid username or password"
            return render(request, 'courses/login.html', {'error': error})
    return render(request, 'courses/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def course_list_view(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    # Get next lesson in same course
    next_lesson = Lesson.objects.filter(
        course=lesson.course,
        order__gt=lesson.order
    ).order_by('order').first()

    # Get previous lesson in same course
    prev_lesson = Lesson.objects.filter(
        course=lesson.course,
        order__lt=lesson.order
    ).order_by('-order').first()

    return render(request, 'courses/lesson_detail.html', {
        'lesson': lesson,
        'next_lesson': next_lesson,
        'prev_lesson': prev_lesson
    })


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lesson = Lesson.objects.filter(course=course).order_by('order').first()

    next_lesson = Lesson.objects.filter(
        course=course,
        order__gt=lesson.order
    ).order_by('order').first()

    prev_lesson = Lesson.objects.filter(
        course=course,
        order__lt=lesson.order
    ).order_by('-order').first()

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'lesson': lesson,
        'next_lesson': next_lesson,
        'prev_lesson': prev_lesson
    })

def course_menu_view(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_menu.html', {'courses': courses})

@login_required
def enroll_view(request):
    profile = request.user.studentprofile
    enrolled = profile.enrolled_courses.all()
    return render(request, 'courses/enroll.html', {'enrolled_courses': enrolled})

@login_required
def lesson_list_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('order')
    return render(request, 'courses/lesson_list.html', {
        'course': course,
        'lessons': lessons
    })

@login_required
def lesson_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('order')

    # Check if user is enrolled
    try:
        profile = request.user.studentprofile
    except StudentProfile.DoesNotExist:
        profile = StudentProfile.objects.create(user=request.user)

    is_enrolled = course in profile.enrolled_courses.all()

    if is_enrolled:
        visible_lessons = lessons
    else:
        visible_lessons = lessons[:3]  # ✅ Show only first 3 lessons

    return render(request, 'courses/lesson_list.html', {
        'course': course,
        'lessons': visible_lessons,
        'is_enrolled': is_enrolled,
    })

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    profile, created = StudentProfile.objects.get_or_create(user=request.user)
    profile.enrolled_courses.add(course)
    return redirect('lesson_list', course_id=course.id)
#@login_required
#def mark_complete(request, lesson_id):
    #lesson = get_object_or_404(Lesson, id=lesson_id)

    # Check if progress already exists
    #progress, created = LessonProgress.objects.get_or_create(
        #user=request.user,
        #lesson=lesson,
        #defaults={'completed': True}
    #)

    # If already exists but not completed, update it
    #if not created and not progress.completed:
        #progress.completed = True
        #progress.save()

    #return redirect('lesson_detail', lesson_id=lesson.id)

 
