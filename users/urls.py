from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]