from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from slugify import slugify
class Post(models.Model):
	title 		= models.CharField(max_length=100)
	content 	= models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author 		= models.ForeignKey(User, on_delete=models.CASCADE)
	Slug        = models.SlugField(max_length=250, blank=True, null=True)
	
	def __str__(self):
		return str(self.title)

	def get_absolute_url(self):
		return reverse('blog:post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
	post 	= models.ForeignKey(Post, null=True,related_name='comments',on_delete=models.CASCADE)
	user 	= models.ForeignKey(User,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	content = models.TextField(null=True,blank=True)
	date_posted= models.DateTimeField(default=timezone.now)
	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		post=self.get(post)
		return reverse('blog:post-detail', kwargs={'id':self.object.id})
	def get_success_url(self):
            return reverse('blog:post-detail', kwargs={'user_id': self.pk})