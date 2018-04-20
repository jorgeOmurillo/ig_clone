from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^signup_success/$', views.signup_success, name='signup_success'),
    url(r'^profile/(?P<username>[-_\w.]+)/$', views.profile, name='profile'),
    url(r'^profile/(?P<username>[-_\w.]+)/edit/$', views.profile_settings, name='profile_settings'),
    url(r'^profile/(?P<username>[-_\w.]+)/followers/$', views.followers, name='followers'),
    url(r'^profile/(?P<username>[-_\w.]+)/following/$', views.following, name='following'),
    url(r'^post/(?P<pk>\d+)/$', views.post, name='post'),
    url(r'^post/$', views.post_picture, name='post_picture'),
    url(r'^explore/$', views.explore, name='explore'),
]
