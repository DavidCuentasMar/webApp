from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	ultimos,
	nosotros,
	ayuda
	)

urlpatterns = [
	url(r'^home$', post_list, name="list"),
	url(r'^$', post_list, name="list"),
	url(r'^ultimos$', ultimos),
	url(r'^nosotros$', nosotros),
	url(r'^ayuda$', ayuda),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),    
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
]