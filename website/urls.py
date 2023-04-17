from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('btech/', views.btech, name="btech"),
    path('mca/', views.mca, name="mca"),
    path('mba/', views.mba, name="mba"),
    path('poly/', views.poly, name="poly"),
    path('e_cse/', views.e_cse, name="cse"),
    path('e_civil/', views.e_civil, name="civil"),
    path('e_me/', views.e_me, name="me"),
    path('e_eee/', views.e_eee, name="eee"),
    
    path('cse_dept/', views.cse_dept, name="d-cse"),
    path('cse_news/<str:pk>/', views.cse_news, name="cse-news"),
    path('cse_events/', views.cse_events, name="cse-events"),
    path('cse_teachers/', views.cse_teachers, name="cse-teachers"),
    path('cse_achievements/', views.cse_achievements, name="cse-achievements"),
    
]

