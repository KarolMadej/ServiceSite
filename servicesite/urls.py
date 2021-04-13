from django.urls import path

from . import views

urlpatterns = [
path('/', views.mainSite, name='mainSite'),
path('/rejestracja', views.register, name='rejestracja'),
path('/logowanie', views.logowanie, name='logowanie'),
path('/wyloguj', views.logoutz, name='wyloguj'),
path('/makecomputer', views.makecomp, name='makecomputer'),
path('/zestawy', views.wyswietl_zestawy, name='zestawy'),
path('/dodaj', views.zestaw_dodajdobiblio, name='dodaj'),
path('/onas', views.onas, name='onas'),
path('/kontakt', views.kontakt, name='kontakt'),

]