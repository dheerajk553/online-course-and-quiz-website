from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import StudentRegisterForm
from .models import StudentProfile
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course
from django.shortcuts import render

@login_required
def dashboard_view(request):
    return render(request, 'courses/dashboard.html')

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    profile = request.user.studentprofile
    profile.enrolled_courses.add(course)
    return redirect('dashboard')

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
            return redirect('dashboard')  # Next step: dashboard
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

 
