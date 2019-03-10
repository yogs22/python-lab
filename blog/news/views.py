from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import News
from . import forms
from django.contrib import messages

def index(request):
	news = News.objects.all()
	return render(request, 'news/index.html', {'news': news})

def single(request, id):
	new = get_object_or_404(News, pk = id)
	form = forms.CommentForm()
	return render(request, 'news/single.html', {'new': new, 'form': form})

def handler404():
	return render(request, '404.html', status = 404)

def comment(request, id):
	new = get_object_or_404(News, pk = id)

	if request.method == 'POST':
		
		form = forms.CommentForm(request.POST)
		if form.is_valid():
			newDesc = request.POST['desc']
			new.comment_set.create(desc = newDesc)

			messages.success(request, 'Berhasil submit komentar !')
			return HttpResponseRedirect(reverse('news:index'))

	return render(request, 'news/single.html', {'new':new, 'form':form})