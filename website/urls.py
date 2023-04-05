from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('btech/', views.btech, name="btech"),
    path('mca/', views.mca, name="mca"),
    path('mba/', views.mba, name="mba"),
    path('poly/', views.poly, name="poly"),
    path('cse/', views.cse, name="cse"),
    path('civil/', views.civil, name="civil"),
    
	
]

