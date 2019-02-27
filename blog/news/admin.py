from django.contrib import admin
from .models import News, Comment

class CommentInline(admin.StackedInline):
	model = Comment
		
class NewsAdmin(admin.ModelAdmin):
	inlines = [CommentInline, ]

admin.site.register(News, NewsAdmin)
admin.site.register(Comment)