from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from jobs import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add_position/$', views.add_position, name='add_position'),
    url(r'^(?P<pk>\d+)/add_comment/$', views.add_comment, name='add_comment'),
    url(r'^(?P<pk>\d+)/comments/$', views.comments, name='comments'),
]