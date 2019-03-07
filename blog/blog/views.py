from django.http import HttpResponse
from django.shortcuts import render
from . import forms

def welcome(request):
	return render(request, 'welcome.html')

def contact(request):
	form = forms.ContactForm()
	return render(request, 'contact.html', {'form': form})