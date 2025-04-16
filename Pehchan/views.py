from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, PostForm
from .models import Profile, Post

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                login(request, user)
                return redirect('profile_update')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change 'home' to your desired page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def Home_view(request):
    return render(request, 'home.html', {'user': request.user})

@login_required
def create_or_update_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save()
            profile.user = request.user
            profile.save()
            return redirect('profile')  # Replace with the name of your profile view
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile_form.html', {'form': form, 'profile': profile})

@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    if not profile.profile_picture:
        profile.profile_picture = 'profile-pic.png'
    return render(request, "profile.html", {"profile": profile})

@login_required
def delete_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == "POST":
        profile.delete()
        return redirect("home")  # Redirect to the homepage after deletion
    return render(request, "delete_profile.html", {"profile": profile})


@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the current user as the author
            post.save()
            return redirect('feed')  # Redirect to a feed or success page
        else:
            return HttpResponse("Invalid form data.", status=400)
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)  # Ensure the post exists and belongs to the logged-in user
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('feed')  # Replace 'post_detail' with the name of your post detail view
    else:
        form = PostForm(instance=post)
    return render(request, 'post_update.html', {'form': form, 'post': post})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author = request.user)
    if request.method == "POST":
        post.delete()
        return redirect("feed")
    return render(request, 'delete_post.html',{'post':post})

@login_required
def feed_view(request):
    post = Post.objects.order_by('-created_at')
    return render(request, 'feed.html', {'post': post})