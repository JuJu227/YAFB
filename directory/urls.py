from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^employee/(?P<employee_id>[0-9]+)/$', views.employee_detail, name='employee_detail'),
    url(r'^group/(?P<group_id>[0-9]+)/$', views.group_detail, name='group_detail'),
    url(r'^type/(?P<type_id>[0-9]+)/$', views.type_list, name='type_list'),
    url(r'^news-feed/', views.news_feed, name='news_feed'),
    url(r'^employee/message/(?P<employee_id>[0-9]+)/$', views.news_feed_by_empoyee, name='news_feed_by_empoyee'),
    url(r'^employee/message/(?P<employee_id>[0-9]+)/newpost/$', views.post_news_feed, name='post_news_feed'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^signin/$', views.signin, name="signin"),
]