from django.urls import path
from .views import register
from . import views
from .views import logout_view  
from .views import dashboard_view


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]

