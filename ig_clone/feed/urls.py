from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^uploads/$', views.upload, name='upload'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
]
