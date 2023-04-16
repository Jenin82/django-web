from django.contrib import admin

# Register your models here.

from .models import CseNews, CseNewsImage, CseEvent, CseTeacher

admin.site.register(CseNews)
admin.site.register(CseNewsImage)
admin.site.register(CseEvent)
admin.site.register(CseTeacher)