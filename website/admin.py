from django.contrib import admin

# Register your models here.

<<<<<<< HEAD
from .models import CivilAchievement, CivilEvent, CivilNews, CivilNewsImage, CivilTeacher, CseAchievement, CseNews, CseNewsImage, CseEvent, CseTeacher, EeeAchievement, EeeEvent, EeeNews, EeeNewsImage, EeeTeacher, MechAchievement, MechEvent, MechNews, MechNewsImage, MechTeacher
=======
from .models import BshAchievement, BshEvent, BshNews, BshNewsImage, BshTeacher, CivilAchievement, CivilEvent, CivilNews, CivilNewsImage, CivilTeacher, CollegeNews, CollegeNewsImage, CseAchievement, CseNews, CseNewsImage, CseEvent, CseTeacher, EeeAchievement, EeeEvent, EeeNews, EeeNewsImage, EeeTeacher, McaAchievement, McaEvent, McaNews, McaNewsImage, McaTeacher, MechAchievement, MechEvent, MechNews, MechNewsImage, MechTeacher
admin.site.register(CollegeNews)
admin.site.register(CollegeNewsImage)
>>>>>>> a83d6a46d5169ba5223559e5ebb24828957c38af

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
<<<<<<< HEAD
=======


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
>>>>>>> a83d6a46d5169ba5223559e5ebb24828957c38af
