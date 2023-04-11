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
    path('dept_cse/', views.dept_cse, name="d-cse"),
]

