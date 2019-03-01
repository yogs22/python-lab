from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404, handler500

app_name = 'news'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:id>', views.single), 
]
