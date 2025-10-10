from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile

class StudentRegisterForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = StudentProfile
        fields = ['full_name', 'age', 'phone', 'home_address', 'status']
