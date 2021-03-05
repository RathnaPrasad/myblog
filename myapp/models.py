from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=50)
	description=models.TextField()
	image=models.ImageField(upload_to='')
	likes=models.IntegerField(default=0)

	def __str__(self):
		return self.title
class Comment(models.Model):
	blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
	comment=models.TextField()

	def __str__(self):
	   return self.comment
