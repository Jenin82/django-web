from django.contrib import admin

# Register your models here.

from .models import CseAchievement, CseNews, CseNewsImage, CseEvent, CseTeacher, MechNews, MechNewsImage

admin.site.register(CseNews)
admin.site.register(CseNewsImage)
admin.site.register(CseEvent)
admin.site.register(CseTeacher)
admin.site.register(CseAchievement)

admin.site.register(MechNews)
admin.site.register(MechNewsImage)

