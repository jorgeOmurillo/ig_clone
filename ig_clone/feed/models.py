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


class PostIt(models.Model):
    user = models.ForeignKey(UserID, null=True, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = ProcessedImageField(upload_to='posts/',
                                        format='JPEG',
                                        options={ 'quality': 100 })
    uploaded_on = models.DateTimeField(auto_now_add=True)
