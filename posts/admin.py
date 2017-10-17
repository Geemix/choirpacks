from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'publish', 'status']
	ordering = ['status', 'publish']
	search_fields = ('title', 'description')
	date_hierarchy = 'publish'
	list_filter = ('status', 'publish', 'created_at')
	prepopulated_fields = {'slug': ('title',)}
	
admin.site.register(Post, PostAdmin)