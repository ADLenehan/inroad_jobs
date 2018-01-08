from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^landing/$', views.index, name='home'),
    url(r'^thanks/$', TemplateView.as_view(template_name='thanks.html'), name='thanks'),
]