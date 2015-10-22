from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^employee/(?P<employee_id>[0-9]+)/$', views.employee_detail, name='employee_detail'),
    url(r'^group/(?P<group_id>[0-9]+)/$', views.group_detail, name='group_detail'),
    url(r'^employee/message/(?P<employee_id>[0-9]+)/$', views.news_feed, name='news_feed'),
]