from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.

def userProfile(request, pk):
  user = User.objects.get(id=pk)
  context = {'user': user}
  return render(request, "user/profile.html", context)


def loginPage(request):
  if request.user.is_authenticated:
    return redirect('request.META.HTTP_REFERER')
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username , password=password)
    if user is not None:
      login(request, user)
      if 'next' in request.POST:
        return HttpResponseRedirect(request.POST.get('next'))
      else:
        return render(request, "website/home.html")
    else:
      return render(request, "user/login.html", {
				"message": "Invalid username or password"
			})
    
  return render(request, "user/login.html") 


def logoutPage(request):
  logout(request)
  return render(request, "website/home.html", {
		"message": "Logged out"
	})