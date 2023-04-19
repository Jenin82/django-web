from django.contrib import admin

# Register your models here.

from .models import CivilNews, CseAchievement, CseNews, CseNewsImage, CseEvent, CseTeacher, MechAchievement, MechEvent, MechNews, MechNewsImage, MechTeacher

admin.site.register(CseNews)
admin.site.register(CseNewsImage)
admin.site.register(CseEvent)
admin.site.register(CseTeacher)
admin.site.register(CseAchievement)

admin.site.register(MechNews)
admin.site.register(MechNewsImage)
admin.site.register(MechEvent)
admin.site.register(MechTeacher)
admin.site.register(MechAchievement)

admin.site.register(CivilNews)
