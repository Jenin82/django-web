from django.db import models
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    user_class = models.CharField(max_length=30)
    img = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
