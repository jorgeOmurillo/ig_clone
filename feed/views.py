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
    if not request.user.is_authenticated():
        return redirect('login')

    users_followed = request.user.userid.following.all()
    posts = PostIt.objects.filter(
            user__in=users_followed).order_by('-posted_on')

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

    posts = PostIt.objects.filter(user=request.user.userid).order_by('-uploaded_on')
    profile = UserID.objects.get(user=user)
    context = {
            'username': username,
            'user': user,
            'profile': profile,
            'posts': posts,
    }

    return render(request, 'feed/profile.html', context)

@login_required
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
            return redirect(reverse('profile', kwargs={ 'username': request.user.username }))
    else:
        form = PostPicture()

    context = {
            'form': form,
    }

    return render(request, 'feed/post_picture.html', context)

def followers(request, username):
    user = User.objects.get(username=username)
    user_profile = UserID.objects.get(user=user)
    profiles = user_profile.followers.all

    context = {
        'header': 'Followers',
        'profiles': profiles,
    }

    return render(request, 'feed/follow_list.html', context)

def following(request, username):
    user = User.objects.get(username=username)
    user_profile = UserID.objects.get(user=user)
    profiles = user_profile.following.all

    context = {
        'header': 'Following',
        'profiles': profiles,
    }

    return render(request, 'feed/follow_list.html', context)

def likes(request, pk):
    post = PostIt.objects.get(pk=pk)
    profiles = Like.objects.filter(post=post)

    context = {
        'header': 'Likes',
        'profiles': profiles
    }

    return render(request, 'feed/follow_list.html', context)

@login_required
def add_like(request):
    post_pk = request.POST.get('post_pk')
    post = PostIt.objects.get(pk=post_pk)
    
    try:
        like = Like(post=post, user=request.user)
        like.save()
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }

def post(request, pk):
    post = PostIt.objects.get(pk=pk)

    try:
        like = Like.objects.get(post=post, user=request.user)
        liked = 1
    except:
        like = None
        liked = 0

    context = {
        'post': post,
        'liked': liked
    }

    return render(request, 'feed/post.html', context)

def explore(request):
    random_posts = PostIt.objects.all().order_by('?')[:40]

    context = {
        'posts': random_posts
    }

    return render(request, 'feed/explore.html', context)

@login_required
def follow_toggle(request):
    user_profile = UserID.objects.get(user=request.user)
    follow_profile_pk = request.POST.get('follow_profile_pk')
    follow_profile = UserID.objects.get(pk=follow_profile_pk)

    try:
        if user_profile != follow_profile:
            if request.POST.get('type') == 'follow':
                user_profile.following.add(follow_profile)
                follow_profile.followers.add(user_profile)
            elif request.POST.get('type') == 'unfollow':
                user_profile.following.remove(follow_profile)
            user_profile.save()
            result = 1
        else:
            result = 0

    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'type': request.POST.get('type'),
        'follow_profile_pk': follow_profile_pk
    }
