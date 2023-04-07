from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def userProfile(request, pk):
  user = User.objects.get(id=pk)
  context = {'user': user}
  return render(request, "user/profile.html", context)