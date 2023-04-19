from django.db import models

# Create your models here.

class CseNews(models.Model):
  title = models.CharField(max_length=200)
  poster = models.CharField(max_length=300)
  description = models.TextField(max_length=300)
  body = models.TextField()
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.title
  
class CseNewsImage(models.Model):
	cseDepartment = models.ForeignKey(CseNews, on_delete=models.CASCADE, related_name="images")
	image = models.CharField(max_length=300, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.image[0:50]

class CseEvent(models.Model):
  title = models.CharField(max_length=200)
  poster = models.CharField(max_length=300)
  description = models.TextField(max_length=300)
  last_date = models.CharField(max_length=50)
  google_form = models.CharField(max_length=300, null=True, blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.title

class CseTeacher(models.Model):
  name = models.CharField(max_length=200)
  profile_picture = models.CharField(max_length=300)
  email = models.CharField(max_length=100)
  qualification = models.TextField(max_length=200)
  role = models.CharField(max_length=100)
  experience = models.TextField(max_length=400)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['created']

  def __str__(self):
    return self.name
  
class CseAchievement(models.Model):
  title = models.CharField(max_length=200)
  image = models.CharField(max_length=300)
  description = models.TextField(max_length=800)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.title
  
class MechNews(models.Model):
  title = models.CharField(max_length=200)
  poster = models.CharField(max_length=300)
  description = models.TextField(max_length=500)
  body = models.TextField()
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.title
  
class MechNewsImage(models.Model):
	mechDepartment = models.ForeignKey(MechNews, on_delete=models.CASCADE, related_name="mechimages")
	image = models.CharField(max_length=300, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.image[0:50]

class MechEvent(models.Model):
  title = models.CharField(max_length=200)
  poster = models.CharField(max_length=300)
  description = models.TextField(max_length=300)
  last_date = models.CharField(max_length=50)
  google_form = models.CharField(max_length=300, null=True, blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.title

class MechTeacher(models.Model):
  name = models.CharField(max_length=200)
  profile_picture = models.CharField(max_length=300)
  email = models.CharField(max_length=100)
  qualification = models.TextField(max_length=200)
  role = models.CharField(max_length=100)
  experience = models.TextField(max_length=400)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['created']

  def __str__(self):
    return self.name

class MechAchievement(models.Model):
  title = models.CharField(max_length=200)
  image = models.CharField(max_length=300, null=True, blank=True)
  description = models.TextField(max_length=800)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.title
  

class CivilNews(models.Model):
  title = models.CharField(max_length=200)
  poster = models.CharField(max_length=300)
  description = models.TextField(max_length=500)
  body = models.TextField()
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.title

  
class CivilNewsImage(models.Model):
	civilDepartment = models.ForeignKey(CivilNews, on_delete=models.CASCADE, related_name="civilimages")
	image = models.CharField(max_length=300, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.image[0:50]