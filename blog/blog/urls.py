from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('news/', include('news.urls')),
	path('', views.welcome),
    path('admin/', admin.site.urls),
]
