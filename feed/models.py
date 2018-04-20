from datetime import datetime
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

    followers = models.ManyToManyField('UserID',
                                        related_name="followers_profile",
                                        blank=True)

    following = models.ManyToManyField('UserID',
                                        related_name="following_profile",
                                        blank=True)

    description = models.CharField(max_length=128, null=True, blank=True)

    def get_number_of_followers(self):
        print(self.followers.count())

        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0
    
    def __str__(self):
        return self.user.username


class PostIt(models.Model):
    user = models.ForeignKey(UserID, null=True, blank=True)
    description = models.CharField(max_length=255)
    image = ProcessedImageField(upload_to='posts',
                                        format='JPEG',
                                        options={ 'quality': 100 })
    uploaded_on = models.DateTimeField(auto_now_add=True)
    
    def get_number_of_likes(self):
        return self.like_set.count()

    def get_number_of_comments(self):
        return self.comment_set.count()

    def __str__(self):
        return self.description

class Comment(models.Model):
    post = models.ForeignKey('PostIt')
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.comment

class Like(models.Model):
    post = models.ForeignKey('PostIt')
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return 'Like: ' + self.user.username + ' ' + self.post.description
