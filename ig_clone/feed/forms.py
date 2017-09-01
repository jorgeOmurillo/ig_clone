from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from imagekit.forms import ProcessedImageField

from .models import UserID, PostIt

class UserNewForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserNewForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user

class UserProfilePic(ModelForm):
    class Meta:
        model = UserID
        fields = ['pic_profile', 'description']

class PostPicture(ModelForm):
    class Meta:
        model = PostIt
        fields = ['title', 'image']
