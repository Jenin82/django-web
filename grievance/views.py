from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm


# Create your views here.

def home(request):
  rooms = Room.objects.all()
  context = {'rooms': rooms}
  return render(request, "grievance/home.html", context)

def room(request, pk):
  room = Room.objects.get(id=pk)
  context = {'room': room}
  return render(request, "grievance/room.html", context)

def createRoom(request):
  form = RoomForm()
  context = {'form': form}
  if request.method == 'POST':
    form = RoomForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  return render(request, "grievance/room_form.html", context)

def deleteRoom(request, pk):
  room = Room.objects.get(id=pk)
  if request.method == 'POST':
    room.delete()
    return redirect('home')
  return render(request, "grievance/delete.html", {'obj': room})