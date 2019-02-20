from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('', views.hello_world),
    path('admin/', admin.site.urls),
]
