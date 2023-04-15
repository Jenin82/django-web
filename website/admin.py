from django.contrib import admin

# Register your models here.

from .models import CseDepartment, CseNewsImage, CseEvent

admin.site.register(CseDepartment)
admin.site.register(CseNewsImage)
admin.site.register(CseEvent)