from django.urls import path
from django.shortcuts import redirect

def default_redirect(request):
    return redirect('/register/')

urlpatterns = [
    path('', default_redirect),  # homepage redirects to register
    path('register/', your_register_view, name='register'),  # ← replace with actual view
]
