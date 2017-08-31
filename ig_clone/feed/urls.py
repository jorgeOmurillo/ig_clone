from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^signup_success/$', views.signup_success, name='signup_success'),
    url(r'^profile/(?P<username>[-_\w.]+)/$', views.profile, name='profile'),
    url(r'^profile/(?P<username>[-_\w.]+)/edit/$', views.profile_settings, name='profile_settings'),
]
