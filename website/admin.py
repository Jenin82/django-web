from django.contrib import admin

# Register your models here.

from .models import CivilNews, CivilNewsImage, CseAchievement, CseNews, CseNewsImage, CseEvent, CseTeacher, EeeNews, EeeNewsImage, MechAchievement, MechEvent, MechNews, MechNewsImage, MechTeacher

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
admin.site.register(CivilNewsImage)



admin.site.register(EeeNews)
admin.site.register(EeeNewsImage)
