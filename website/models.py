from django.db import models


# Create your models here.


class CseDepartment(models.Model):
  title = models.CharField(max_length=200)
  image = models.CharField(max_length=300)
  description = models.TextField()
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.title
  
class NewsImage(models.Model):
	cseDepartment = models.ForeignKey(CseDepartment, on_delete=models.CASCADE, related_name="images")
	image = models.CharField(max_length=300)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.image[0:50]