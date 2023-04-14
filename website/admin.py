from django.contrib import admin

# Register your models here.

from .models import CseDepartment, NewsImage

admin.site.register(CseDepartment)
admin.site.register(NewsImage)