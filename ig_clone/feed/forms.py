from django import forms

from feed.models import FileIt

class FileItForm(forms.ModelForm):
    class Meta:
        model = FileIt
        fields = ('description', 'file_it', )
