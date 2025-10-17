from django.urls import path
from .views import register
from . import views
from .views import logout_view  
from .views import dashboard_view


urlpatterns = [
    path('register/', views.register, name='register'), 
    path('login/', views.login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('courses/', views.course_list_view, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('courses/menu/', views.course_menu_view, name='course_menu'),
    # path('lesson/<int:lesson_id>/complete/', views.mark_complete, name='mark_complete'),
]

