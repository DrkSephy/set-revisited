from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.userLogin, name='login'),
	url(r'^register/$', views.register, name='register'),
)