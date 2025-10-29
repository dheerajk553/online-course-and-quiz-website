from django.urls import path
from django.shortcuts import redirect
from . import views
from .views import download_certificate
from .views import (
    register, login_view, logout_view, dashboard_view,
    confirm_enroll_view, enroll_course, quiz_view, submit_quiz,
    course_dashboard_view, course_list_view, course_detail,
    enroll_view, lesson_detail, course_menu_view, lesson_list_view
)

urlpatterns = [
    path('', views.register, name='home'),
    #path('', lambda request: redirect('/register/')), #  homepage redirect
    path('register/', views.register_view, name='register'), #  actual register view
    path('register/', register, name='register'), 
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),

    path('courses/', course_list_view, name='course_list'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('course/<int:course_id>/dashboard/', course_dashboard_view, name='course_dashboard'),

    path('enroll/', enroll_view, name='enroll_view'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll'),
    path('course/<int:course_id>/confirm-enroll/', confirm_enroll_view, name='confirm_enroll'),
    path('course/<int:course_id>/enroll/', enroll_course, name='enroll_course'),

    path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'),
    path('lessons/<int:course_id>/', lesson_list_view, name='lesson_list'),

    path('courses/menu/', course_menu_view, name='course_menu'),
    path('menu/', course_menu_view, name='course_menu'),  # optional duplicate

    path('course/<int:course_id>/quiz/', quiz_view, name='quiz'),
    path('course/<int:course_id>/quiz/submit/', submit_quiz, name='submit_quiz'),
    path('certificate/download/', download_certificate, name='download_certificate'),

]
