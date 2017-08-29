from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class UserID(models.Model):
    user = models.OneToOneField(User)

    pic_profile = ProcessedImageField(upload_to='profile_pics',
                                        format='JPEG',
                                        options={ 'quality': 100},
                                        null=True,
                                        blank=True)

    description = models.CharField(max_length=128, null=True, blank=True)
    
    def __str__(self):
        return self.user.username


class FileIt(models.Model):
    users = models.ForeignKey(UserID, null=True, blank=True)
    description = models.CharField(max_length=255, blank=True)
    file_it = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
