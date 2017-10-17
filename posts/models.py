from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
#	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=255)
	description = models.TextField()
	slug = models.SlugField(max_length=100, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	post_img = models.ImageField(upload_to="media/post_img")
	publish = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	
	class Meta:
		ordering = ('-publish',)
	
	def __str__(self):
		return(self.title)
	
#	def slug (self):
#		return slugify(self.title)
#	
##	def save(self, *args, **kwargs):
##		self.slug = slugify(self.title) # set the slug explicitly
##		super(Post, self).save(*args, **kwargs) # call Django's save()
#	
#	def save(self, *args, **kwargs):
#		if not self.id:
#			self.slug = slugify(self.title)
#	
#		super(Post, self).save(*args, **kwargs)