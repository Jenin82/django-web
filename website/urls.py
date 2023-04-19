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
    
    path('mech_dept/', views.mech_dept, name="d-mech"),
    path('mech_news/<str:pk>/', views.mech_news, name="mech-news"),
    path('mech_events/', views.mech_events, name="mech-events"),
    path('mech_teachers/', views.mech_teachers, name="mech-teachers"),
    path('mech_achievements/', views.mech_achievements, name="mech-achievements"),

    path('civil_dept/', views.civil_dept, name="d-civil"),
    path('civil_news/<str:pk>/', views.civil_news, name="civil-news"),
    path('civil_events/', views.civil_events, name="civil-events"),
    path('civil_teachers/', views.mech_teachers, name="mech-teachers"),
    path('civil_achievements/', views.mech_achievements, name="mech-achievements"),

    path('eee_dept/', views.eee_dept, name="d-eee"),
    path('eee_news/<str:pk>/', views.mech_news, name="mech-news"),
    path('eee_events/', views.mech_events, name="mech-events"),
    path('eee_teachers/', views.mech_teachers, name="mech-teachers"),
    path('eee_achievements/', views.mech_achievements, name="mech-achievements"),


    
    
]

