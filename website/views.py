from django.shortcuts import render
from website.models import BshAchievement, BshEvent, BshNews, BshTeacher, CivilAchievement, CivilEvent, CivilNews, CivilTeacher, CollegeNews, CseAchievement, CseNews, CseEvent, CseTeacher, EeeAchievement, EeeAchievement, EeeEvent, EeeNews, EeeTeacher, MbaAchievement, MbaEvent, MbaNews, MbaTeacher, McaAchievement, McaEvent, McaNews, McaNewsImage, McaTeacher, MechNews, MechAchievement, MechEvent, MechTeacher, Placement

# Create your views here.

def home(request):
  news = CollegeNews.objects.all()
  placements = Placement.objects.all().order_by('-created')[:8]
  context = { 'news' : news, 'placements' : placements}
  return render(request, 'website/home.html', context)

def college_news_main(request):
  news = CollegeNews.objects.all()
  context = { 'news' : news}
  return render(request, 'website/college_news_main.html', context)

def college_news(request, pk):
  collegeNews = CollegeNews.objects.get(id=pk)
  images = collegeNews.collegeimages.all().order_by('-created')
  context = {'news' : collegeNews, 'newsImages' : images}
  return render(request, 'website/college_news.html', context)

def placements(request):
  placements = Placement.objects.all()
  context = { 'placements' : placements }
  return render(request, 'website/placements.html', context)

def btech(request):
  context = {}
  return render(request, 'website/btech.html', context)

def mca(request):
  context = {}
  return render(request, 'website/mca.html', context)

def mba(request):
  context = {}
  return render(request, 'website/mba.html', context)

def poly(request):
  context = {}
  return render(request, 'website/poly.html', context)

def e_cse(request):
  context = {}
  return render(request, 'website/e-cse.html', context)

def e_civil(request):
  context = {}
  return render(request, 'website/e-civil.html', context)

def e_me(request):
  context = {}
  return render(request, 'website/e-me.html', context)

def e_eee(request):
  context = {}
  return render(request, 'website/e-eee.html', context)

def cse_dept(request):
  dept = CseNews.objects.all()
  context = { 'dept' : dept}
  return render(request, 'website/cse_dept.html', context)

def cse_news(request, pk):
  cseNews = CseNews.objects.get(id=pk)
  images = cseNews.images.all().order_by('-created')
  context = {'news' : cseNews, 'newsImages' : images}
  return render(request, 'website/cse_news.html', context)

def cse_events(request):
  events = CseEvent.objects.all()
  context = {'events' : events}
  return render(request, 'website/cse_events.html', context)

def cse_teachers(request):
  teachers = CseTeacher.objects.all()
  context = {'teachers' : teachers}
  return render(request, 'website/cse_teachers.html', context)

def cse_achievements(request):
  achievements = CseAchievement.objects.all()
  context = {'achievements' : achievements}
  return render(request, 'website/cse_achievements.html', context)

def mech_dept(request):
  dept = MechNews.objects.all()
  context = { 'dept' : dept}
  return render(request, 'website/mech_dept.html', context)

def mech_news(request, pk):
  mechNews = MechNews.objects.get(id=pk)
  images = mechNews.mechimages.all().order_by('-created')
  context = {'news' : mechNews, 'newsImages' : images}
  return render(request, 'website/mech_news.html', context)

def mech_events(request):
  events = MechEvent.objects.all()
  context = {'events' : events}
  return render(request, 'website/mech_events.html', context)

def mech_teachers(request):
  teachers = MechTeacher.objects.all()
  context = {'teachers' : teachers}
  return render(request, 'website/mech_teachers.html', context)

def mech_achievements(request):
  achievements = MechAchievement.objects.all()
  context = {'achievements' : achievements}
  return render(request, 'website/mech_achievements.html', context)

def civil_dept(request):
  dept = CivilNews.objects.all()
  context = { 'dept' : dept}
  return render(request, 'website/civil_dept.html', context)

def civil_news(request, pk):
  civilNews = CivilNews.objects.get(id=pk)
  images = civilNews.civilimages.all().order_by('-created')
  context = {'news' : civilNews, 'newsImages' : images}
  return render(request, 'website/civil_news.html', context)

def civil_events(request):
  events = CivilEvent.objects.all()
  context = {'events' : events}
  return render(request, 'website/civil_events.html', context)

def civil_teachers(request):
  teachers = CivilTeacher.objects.all()
  context = {'teachers' : teachers}
  return render(request, 'website/civil_teachers.html', context)

def civil_achievements(request):
  achievements = CivilAchievement.objects.all()
  context = {'achievements' : achievements}
  return render(request, 'website/civil_achievements.html', context)

def eee_dept(request):
  dept = EeeNews.objects.all()
  context = { 'dept' : dept}
  return render(request, 'website/eee_dept.html', context)

def eee_news(request, pk):
  eeeNews = EeeNews.objects.get(id=pk)
  images = eeeNews.eeeimages.all().order_by('-created')
  context = {'news' : eeeNews, 'newsImages' : images}
  return render(request, 'website/eee_news.html', context)

def eee_events(request):
  events = EeeEvent.objects.all()
  context = {'events' : events}
  return render(request, 'website/eee_events.html', context)

def eee_teachers(request):
  teachers = EeeTeacher.objects.all()
  context = {'teachers' : teachers}
  return render(request, 'website/eee_teachers.html', context)

def eee_achievements(request):
  achievements = EeeAchievement.objects.all()
  context = {'achievements' : achievements}
  return render(request, 'website/eee_achievements.html', context)

def bsh_dept(request):
  dept = BshNews.objects.all()
  context = { 'dept' : dept}
  return render(request, 'website/bsh_dept.html', context)

def bsh_news(request, pk):
  bshNews = BshNews.objects.get(id=pk)
  images = bshNews.bshimages.all().order_by('-created')
  context = {'news' : bshNews, 'newsImages' : images}
  return render(request, 'website/bsh_news.html', context)

def bsh_events(request):
  events = BshEvent.objects.all()
  context = {'events' : events}
  return render(request, 'website/bsh_events.html', context)

def bsh_teachers(request):
  teachers = BshTeacher.objects.all()
  context = {'teachers' : teachers}
  return render(request, 'website/bsh_teachers.html', context)

def bsh_achievements(request):
  achievements = BshAchievement.objects.all()
  context = {'achievements' : achievements}
  return render(request, 'website/bsh_achievements.html', context)

def mca_dept(request):
  dept = McaNews.objects.all()
  context = { 'dept' : dept}
  return render(request, 'website/mca_dept.html', context)

def mca_news(request, pk):
  mcaNews = McaNews.objects.get(id=pk)
  images = mcaNews.mcaimages.all().order_by('-created')
  context = {'news' : mcaNews, 'newsImages' : images}
  return render(request, 'website/mca_news.html', context)

def mca_events(request):
  events = McaEvent.objects.all()
  context = {'events' : events}
  return render(request, 'website/mca_events.html', context)

def mca_teachers(request):
  teachers = McaTeacher.objects.all()
  context = {'teachers' : teachers}
  return render(request, 'website/mca_teachers.html', context)

def mca_achievements(request):
  achievements = McaAchievement.objects.all()
  context = {'achievements' : achievements}
  return render(request, 'website/mca_achievements.html', context)

def eee_achievements(request):
  achievements = EeeAchievement.objects.all()
  context = {'achievements' : achievements}
  return render(request, 'website/eee_achievements.html', context)

def mba_dept(request):
  dept = McaNewsImage.objects.all()
  context = { 'dept' : dept}
  return render(request, 'website/mba_dept.html', context)

def mba_news(request, pk):
  mbaNews = MbaNews.objects.get(id=pk)
  images = mbaNews.mbaimages.all().order_by('-created')
  context = {'news' : mbaNews, 'newsImages' : images}
  return render(request, 'website/mba_news.html', context)

def mba_events(request):
  events = MbaEvent.objects.all()
  context = {'events' : events}
  return render(request, 'website/mba_events.html', context)

def mba_teachers(request):
  teachers = MbaTeacher.objects.all()
  context = {'teachers' : teachers}
  return render(request, 'website/mba_teachers.html', context)

def mba_achievements(request):
  achievements = MbaAchievement.objects.all()
  context = {'achievements' : achievements}
  return render(request, 'website/mba_achievements.html', context)

