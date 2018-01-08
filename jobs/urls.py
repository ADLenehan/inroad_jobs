from django.conf.urls import url, include
from jobs import views


urlpatterns = [
    url(r'^add_board/$', views.add_board, name='add_board'),
    url(r'^saved_jobs/$', views.saved_jobs, name='saved_jobs'),
    url(r'^(?P<pk>\d+)/save_job/$', views.save_job, name='save_job'),
    url(r'^(?P<pk>\d+)/apply/$', views.apply, name='apply'),
    url(r'^(?P<pk>\d+)/unsave_job/$', views.unsave_job, name='unsave_job'),
    url(r'^(?P<board_name>[-\w]+)/', include([
        url(r'^board/$', views.board, name='board'),
        url(r'^add_position/$', views.add_position, name='add_position'),
        url(r'^(?P<pk>\d+)/add_comment/$', views.add_comment, name='add_comment'),
        url(r'^(?P<pk>\d+)/comments/$', views.comments, name='comments'),
        ])),
]