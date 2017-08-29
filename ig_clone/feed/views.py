from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from imagekit.models import ProcessedImageField
from .models import UserID, FileIt
from .forms import FileItForm, UserNewForm

# Create your views here.
@login_required
def home(request):
    return render(request, 'feed/home.html')

# @login_required
# def upload(request):
    # if request.method == 'POST' and request.FILES['myfile']:
        # myfile = request.FILES['myfile']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        # return render(request, 'feed/upload.html', {
            # 'uploaded_file_url': uploaded_file_url
        # })
    
    # return render(request, 'feed/upload.html')

# @login_required
# def model_form_upload(request):
    # if request.method == 'POST':
        # form = FileItForm(request.POST, request.FILES)
        # if form.is_valid():
            # form.save()
            # return redirect('home')
    # else:
        # form = FileItForm()
    
    # return render(request, 'feed/model_form_upload.html', {
        # 'form': form
    # })

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

    profile = UserProfile.objects.get(user=user)
    context = {
            'username': username,
            'user': user,
            'profile': profile
    }

    return render(request, 'feed/profile.html', context)
