from django.shortcuts import render

from website.models import CseAchievement, CseNews, CseEvent, CseTeacher, MechNews

# Create your views here.

def home(request):
  number = 1000
  context = {'number': number}
  return render(request, 'website/home.html', context)

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