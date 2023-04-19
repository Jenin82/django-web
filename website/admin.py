from django.contrib import admin

# Register your models here.

from .models import CivilAchievement, CivilEvent, CivilNews, CivilNewsImage, CivilTeacher, CseAchievement, CseNews, CseNewsImage, CseEvent, CseTeacher, EeeEvent, EeeNews, EeeNewsImage, MechAchievement, MechEvent, MechNews, MechNewsImage, MechTeacher

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
admin.site.register(CivilEvent)
admin.site.register(CivilTeacher)
admin.site.register(CivilAchievement)

admin.site.register(EeeNews)
admin.site.register(EeeNewsImage)
admin.site.register(EeeEvent)
