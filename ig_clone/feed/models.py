from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    def __str__(self):
        return self.user.username


class FileIt(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file_it = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

