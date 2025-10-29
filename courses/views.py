from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import StudentRegisterForm
from .models import Course, Lesson, StudentProfile
from .models import Course, Quiz
from .models import Quiz, QuizAttempt, Course
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from datetime import datetime
from .models import Course, StudentProfile
from django.http import HttpResponse
import pdfkit  # or use xhtml2pdf
from django.shortcuts import render

#from courses.views import mark_complete

#from .models import Lesson, LessonProgress
def register_view(request):
    return render(request, 'register.html')

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
    all_lessons = Lesson.objects.filter(course=course)

    profile = StudentProfile.objects.filter(user=request.user).first()
    is_enrolled = profile and course in profile.enrolled_courses.all()

    # Show all lessons if enrolled, else only first 3
    lessons = all_lessons if is_enrolled else all_lessons[:3]

    return render(request, 'courses/lesson_list.html', {
        'course': course,
        'lessons': lessons,
        'is_enrolled': is_enrolled,
    })


@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    profile, created = StudentProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'full_name': request.user.username,
            'age': None,
            'phone': '',
            'home_address': '',
            'status': 'Student',
        }
    )

    if course not in profile.enrolled_courses.all():
        profile.enrolled_courses.add(course)

    return redirect('lesson_list', course_id=course.id)



@login_required
def quiz_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizzes = Quiz.objects.filter(course=course)

    profile = StudentProfile.objects.filter(user=request.user).first()
    is_enrolled = profile and course in profile.enrolled_courses.all()

    return render(request, 'courses/quiz.html', {
        'course': course,
        'quizzes': quizzes,
        'is_enrolled': is_enrolled,
    })

@login_required
def course_dashboard_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    profile = StudentProfile.objects.filter(user=request.user).first()
    if not profile or course not in profile.enrolled_courses.all():
        messages.error(request, "You must enroll in this course to access dashboard.")
        return redirect('confirm_enroll', course_id=course.id)

    lessons = Lesson.objects.filter(course=course).order_by('order')
    quizzes = Quiz.objects.filter(course=course)

    return render(request, 'courses/course_dashboard.html', {
        'course': course,
        'lessons': lessons,
        'quizzes': quizzes,
    })

@login_required
def submit_quiz(request, course_id):
    course = Course.objects.get(id=course_id)
    questions = Quiz.objects.filter(course=course)[:10]
    score = 0

    if request.method == 'POST':
        for q in questions:
            selected = int(request.POST.get(f'question_{q.id}', 0))
            if selected == q.correct_option:
                score += 1

        passed = score >= 8

        full_name = request.user.get_full_name()
        if not full_name:
            full_name = request.user.username

        issue_date = datetime.now().strftime("%d %B %Y")

        QuizAttempt.objects.create(user=request.user, course=course, score=score, passed=passed)

        if passed:
            request.session['certificate_context'] = {
                'full_name': full_name,
                'issue_date': issue_date,
                'score': score,
                'course_id': course.id,
            }

        return render(request, 'courses/quiz_result.html', {
            'score': score,
            'passed': passed,
            'course': course,
        })

    return render(request, 'courses/quiz_page.html', {'course': course, 'questions': questions})


@login_required
def download_certificate(request):
    context = request.session.get('certificate_context')
    if not context:
        messages.error(request, "No certificate available.")
        return redirect('dashboard')

    course = get_object_or_404(Course, id=context['course_id'])

    html = render_to_string('courses/certificate_template.html', {
        'full_name': context['full_name'],
        'issue_date': context['issue_date'],
        'score': context['score'],
        'course': course,
    })

    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{course.title}_certificate.pdf"'
    return response

@login_required
def confirm_enroll_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/confirm_enroll.html', {'course': course})
# Get or create student profile
    profile, created = StudentProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'full_name': request.user.username,
            'age': None,
            'phone': '',
            'home_address': '',
            'status': 'Student',
        }
    )
    # Restriction: profile must be complete
    if not profile.age or not profile.phone:
        messages.error(request, "Please complete your profile before enrolling.")
        return redirect('edit_profile')  # Replace with your actual profile edit view name

    # Enroll if not already enrolled
    if course not in profile.enrolled_courses.all():
        profile.enrolled_courses.add(course)
        messages.success(request, f"You have successfully enrolled in {course.title}.")

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

 
