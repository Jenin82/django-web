from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="g-home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('room/<str:pk>/resolved', views.statusResolved, name="resolved"),
    path('room/<str:pk>/reopened', views.statusReopen, name="reopen"),
	path('resolved/', views.homeResolved, name="resolved"),
	path('reopened/', views.homeReopen, name="reopened"),
	path('inprogress/', views.homeInProgress, name="inprogress"),
]