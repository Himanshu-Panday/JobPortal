from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    mobile_number = models.CharField(max_length=15)
    skills = models.TextField(max_length=200)
    experience = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    job_title = models.CharField(max_length=200)
    job_company = models.CharField(max_length=500)
    skill = models.TextField(max_length=2000)
    description = models.TextField(max_length=2000)
    job_link = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title