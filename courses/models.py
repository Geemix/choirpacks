from django.db import models
#from django.utils.text import slugify

# Create your models here.
class Course(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	description = models.TextField()
	topic_img = models.ImageField(upload_to='media/topic_img')
	
	def __str__(self):
		return(self.title)
	
class Step(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	content = models.TextField(blank=True, default='')
	order = models.IntegerField(default=0)
	course = models.ForeignKey(Course)
	
	class Meta:
		ordering = ['order',]
	
	def __str__(self):
		return self.title
	
#	order = models.SlugField()
	
	
#	def save(self, *args, **kwargs):
#		if not self.id:
#			# Newly created object, so set slug
#			self.order = slugify(self.title)
#		super(Step, self).save(*args, **kwargs)