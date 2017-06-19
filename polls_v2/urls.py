from django.conf.urls import url
from . import views

app_name = 'polls_v2'
urlpatterns = [
    url(r'^$', views.polls, name='list'),
    url(r'^(?P<poll_id>[0-9]+)/$', views.poll_detail, name='detail'),
    url(r'^(?P<poll_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
