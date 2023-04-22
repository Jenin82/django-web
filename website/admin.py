from django.contrib import admin

# Register your models here.

from .models import BshAchievement, BshEvent, BshNews, BshNewsImage, BshTeacher, CivilAchievement, CivilEvent, CivilNews, CivilNewsImage, CivilTeacher, CollegeNews, CollegeNewsImage, CseAchievement, CseNews, CseNewsImage, CseEvent, CseTeacher, EeeAchievement, EeeAchievement, EeeEvent, EeeNews, EeeNewsImage, EeeTeacher, MbaAchievement, MbaEvent, MbaNews, MbaNewsImage, MbaTeacher, McaAchievement, McaEvent, McaNews, McaNewsImage, McaTeacher, MechAchievement, MechEvent, MechNews, MechNewsImage, MechTeacher
admin.site.register(CollegeNews)
admin.site.register(CollegeNewsImage)

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
admin.site.register(EeeTeacher)
admin.site.register(EeeAchievement)


admin.site.register(BshNews)
admin.site.register(BshNewsImage)
admin.site.register(BshEvent)
admin.site.register(BshTeacher)
admin.site.register(BshAchievement)

admin.site.register(McaNews)
admin.site.register(McaNewsImage)
admin.site.register(McaEvent)
admin.site.register(McaTeacher)
admin.site.register(McaAchievement)

admin.site.register(MbaNews)
admin.site.register(MbaNewsImage)
admin.site.register(MbaEvent)
admin.site.register(MbaTeacher)
admin.site.register(MbaAchievement)
