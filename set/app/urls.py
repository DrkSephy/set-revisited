from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^shopping/$', views.shopping, name='shopping'),
	url(r'^checkout/$', views.checkout, name='checkout'),
)