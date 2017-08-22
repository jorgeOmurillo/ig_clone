from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from feed.models import FileIt
from feed.forms import FileItForm

# Create your views here.
def home(request):
    file_it = FileIt.objects.all()
    return render(request, 'feed/home.html', { 'file_it': file_it })

# @login_required
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'feed/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    
    return render(request, 'feed/upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = FileItForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileItForm()
    
    return render(request, 'feed/model_form_upload.html', {
        'form': form
    })
