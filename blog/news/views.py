from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from .models import News

def index(request):
	news = News.objects.all()
	return render(request, 'news/index.html', {'news': news})

def single(request, id):
	new = get_object_or_404(News, pk = id)
	return render(request, 'news/single.html', {'new': new})

def handler404():
	return render(request, '404.html', status = 404)

def comment(request, id):
	new = get_object_or_404(News, pk = id)

	if request.method == 'POST':
		newDesc = request.POST['desc']
		new.comment_set.create(desc = newDesc)

		return HttpResponseRedirect('/news/' + str(id))