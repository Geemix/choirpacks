from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Post

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'posts/post_list.html', {'posts':posts})

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'posts/post_detail.html', {'post':post})