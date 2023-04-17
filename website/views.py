from django.shortcuts import render

from website.models import CseNews, CseEvent, CseTeacher

# Create your views here.

def home(request):
  context = {}
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
  events = CseEvent.objects.all()
  context = {'events' : events}
  return render(request, 'website/cse_achievements.html', context)
