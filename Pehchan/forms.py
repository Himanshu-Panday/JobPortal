from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'first_name', 'last_name', 'date_of_birth', 'mobile_number', 'skills', 'experience']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['job_title', 'job_company', 'skill', 'description', 'job_link']
