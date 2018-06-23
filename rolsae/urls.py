from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
   # url(r'^$', views.index, name='index'),
    # ex: /polls/5/
   # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
   # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
   # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
   url(r'^$', views.post_list, name='post_list'),
   url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
   url(r'^post/new/$', views.post_new, name='post_new'),
   url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
