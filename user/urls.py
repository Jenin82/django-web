from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:pk>/', views.userProfile, name="user-profile"),
		path('login/', views.loginPage, name="login"),
		path('logout/', views.logoutPage, name="logout"),
    
]

