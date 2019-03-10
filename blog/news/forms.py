from .models import Comment
from django import forms
from django.core import validators

class CommentForm(forms.ModelForm):
	desc = forms.CharField(required = True,
		widget = forms.Textarea,
		validators = [validators.MinLengthValidator(3)])

	class Meta:
		model = Comment
		fields = ['desc']