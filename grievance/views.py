from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Room
from .forms import RoomForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def loginPage(request):
  if request.user.is_authenticated:
    return redirect('home')
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username , password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse("home"))
    else:
      return render(request, "grievance/login.html", {
				"message": "Invalid username or password"
			})
    
  return render(request, "grievance/login.html") 

def logoutPage(request):
  logout(request)
  return render(request, "grievance/login.html", {
		"message": "Logged out"
	})

@login_required(login_url='login')
def home(request):
  rooms = Room.objects.all()
  context = {'rooms': rooms}
  return render(request, 'grievance/home.html', context)
  
def room(request, pk):
  room = Room.objects.get(id=pk)
  context = {'room': room}
  return render(request, "grievance/room.html", context)

@login_required(login_url='login')
def createRoom(request):
  room = Room()
  context = {'room': room}
  if request.method == 'POST':
    title = request.POST["title"]
    description = request.POST["description"]
    room.host = request.user
    room.name = title
    room.description = description
    room.save()
    return redirect('g-home')
  
  # form = RoomForm()
  # context = {'form': form}
  # if request.method == 'POST':
  #   form = RoomForm(request.POST)
  #   if form.is_valid():
  #     room = form.save(commit=False)
  #     room.host = request.user
  #     room.save()
  #     return redirect('g-home')
  return render(request, "grievance/room_form.html", context)

def deleteRoom(request, pk):
  room = Room.objects.get(id=pk)
  if request.user != room.host:
    return HttpResponse('You are not allowed to delete someone else grievance')
  if request.method == 'POST':
    room.delete()
    return redirect('g-home')
  return render(request, "grievance/delete.html", {'obj': room})

