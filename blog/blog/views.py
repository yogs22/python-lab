from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages

from . import forms

def welcome(request):
	return render(request, 'welcome.html')

def contact(request):
	form = forms.ContactForm()

	if request.method == 'POST':
		form = forms.ContactForm(request.POST)
		if form.is_valid():
			#Send email
			messages.success(request, 'Berhasil mengirim email')
			return HttpResponseRedirect(reverse('contact'))

	return render(request, 'contact.html', {'form': form})