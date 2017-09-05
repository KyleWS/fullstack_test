from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^resume', views.ResumeView, name="resume"),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
