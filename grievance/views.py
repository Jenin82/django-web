from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Message, Room
from .forms import RoomForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import allowed_users



# Create your views here.

@login_required(login_url='login')
def home(request):
  rooms = Room.objects.all()
  context = {'rooms': rooms}
  return render(request, 'grievance/home.html', context)
@login_required(login_url='login')
def homeResolved(request):
  rooms = Room.objects.all()
  context = {'rooms': rooms}
  return render(request, 'grievance/resolved.html', context)
@login_required(login_url='login')
def homeInProgress(request):
  rooms = Room.objects.all()
  context = {'rooms': rooms}
  return render(request, 'grievance/inprogress.html', context)
@login_required(login_url='login')
def homeReopen(request):
  rooms = Room.objects.all()
  context = {'rooms': rooms}
  return render(request, 'grievance/reopened.html', context)
  
def room(request, pk):
  room = Room.objects.get(id=pk)
  room_messages = room.message_set.all().order_by('created')
  
  
  if request.method == 'POST':
    message = Message.objects.create(
			user = request.user,
			room = room,
			body = request.POST.get('body')
		)
    return redirect('room', pk=room.id)
  
  
  context = {'room': room, 'room_messages': room_messages}
  return render(request, "grievance/room.html", context)

@login_required(login_url='login')
def createRoom(request):
  room = Room()
  context = {'room': room}
  if request.method == 'POST':
    title = request.POST["title"]
    description = request.POST["description"]
    room.host = request.user
    room.status = 'In-progress'
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

# @allowed_users(allowed_roles=['grievance_committee'])
def statusResolved(request, pk):
  room = Room.objects.get(id=pk)
  room.status = 'Resolved'
  room.save()
  return redirect('g-home')

def statusReopen(request, pk):
  room = Room.objects.get(id=pk)
  room.status = 'Re-opened'
  room.save()
  return redirect('g-home')
