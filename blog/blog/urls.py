from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('news/', include('news.urls')),
	path('', views.hello_world),
    path('admin/', admin.site.urls),
]
