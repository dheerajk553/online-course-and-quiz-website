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
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    
]

