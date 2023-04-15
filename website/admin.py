from django.contrib import admin

# Register your models here.

from .models import CseDepartment, CseNewsImage, CseEvent, CseTeacher

admin.site.register(CseDepartment)
admin.site.register(CseNewsImage)
admin.site.register(CseEvent)
admin.site.register(CseTeacher)