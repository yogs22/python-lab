from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('news/', include('news.urls', namespace = 'news')),
	path('', views.welcome, name = 'home'),
	path('kontak/', views.contact, name = 'contact'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()