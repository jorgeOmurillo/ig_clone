import datetime

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from imagekit.models import ProcessedImageField
from .models import UserID, PostIt
from .forms import UserNewForm, UserProfilePic, PostPicture

# Create your views here.
def home(request):

    return render(request, 'feed/home.html')

def login_user(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'feed/login.html', {
        'form': form
    })

def signup(request):
    form = UserNewForm

    if request.method == 'POST':
        form = UserNewForm(request.POST)

        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username'])
            profile = UserID(user=user)
            profile.save()

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('home')

    return render(request, 'feed/signup.html', {
        'form': form
    })

def signup_success(request):
    return render(request, 'feed/signup_success.html')

def signout(request):
    logout(request)
    return redirect('home')

def profile(request, username):
    user = User.objects.get(username=username)
    if not user:
        return redirect('home')

    profile = UserID.objects.get(user=user)
    context = {
            'username': username,
            'user': user,
            'profile': profile
    }

    return render(request, 'feed/profile.html', context)

def profile_settings(request, username):
    user = User.objects.get(username=username)

    if request.user != user:
        return redirect('home')
    
    if request.method == 'POST':
        print(request.POST)

        form = UserProfilePic(request.POST, instance=user.userid, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse('profile', kwargs={'username': user.username}))
    else:
        form = UserProfilePic(instance=user.userid)

    context = {
            'user': user,
            'form': form,
    }

    return render(request, 'feed/profile_settings.html', context)

def post_picture(request):
    if request.method == 'POST':
        form = PostPicture(data=request.POST, files=request.FILES)

        if form.is_valid():
            post = PostIt(user=request.user.userid,
                            description=request.POST['description'],
                            image=request.FILES['image'],
                            uploaded_on=datetime.datetime.now())

            post.save()
            return redirect(reverse('home'))
    else:
        form = PostPicture()

    context = {
            'form': form,
    }

    return render(request, 'feed/post_picture.html', context)
