from django import forms
from .models import UserExtended,Procesor,PlytaGlowna,Ram,Dysk,Obudowa,Monitor,Chlodzenie,Zestaw,KartaGraficzna


class RegisterForm(forms.Form):
   login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}) ,required=True)
   imie = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
   nazwisko = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
   email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)


class LoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}) ,required=True)

class DodajDoZestawuForm (forms.Form):
    procesor = forms.ModelChoiceField(queryset=Procesor.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    kartagraficzna = forms.ModelChoiceField(queryset=KartaGraficzna.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    ram = forms.ModelChoiceField(queryset=Ram.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    plytaglowna = forms.ModelChoiceField(queryset=PlytaGlowna.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    dysk = forms.ModelChoiceField(queryset=Dysk.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    obudowa = forms.ModelChoiceField(queryset=Obudowa.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    monitor = forms.ModelChoiceField(queryset=Monitor.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    chlodzenie = forms.ModelChoiceField(queryset=Chlodzenie.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))