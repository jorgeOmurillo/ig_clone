from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^signup/$', views.logout, name='logout'),
    url(r'^signout/$', views.signout, name='signout'),
]
