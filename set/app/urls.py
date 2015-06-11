from django.conf.urls import patterns, urls

from app import views

urlpatterns = pattern('',
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.userLogin, name='login'),
)