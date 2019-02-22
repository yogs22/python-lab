from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
	news = News.objects.all()
	output = ', '. join([str(new) for new in news])
	return HttpResponse(output)