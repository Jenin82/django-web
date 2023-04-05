from django.shortcuts import render

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

def cse(request):
  context = {}
  return render(request, 'website/cse.html', context)

def civil(request):
  context = {}
  return render(request, 'website/civil.html', context)