import re
from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from feed.models import Like

register = template.Library()

@register.simple_tag
def has_user_liked(post, user):
    try:
        like = Like.objects.get(post=post, user=user)
        return "fa-heart"
    except:
        return "fa-heart-o"

@register.simple_tag
def is_following(users_profile, profile_to_check):
    return users_profile.following.filter(user_id=profile_to_check.user_id).exists()
