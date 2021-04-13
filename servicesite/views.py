from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import UserExtended,Procesor,PlytaGlowna,Ram,Dysk,Obudowa,Monitor,Chlodzenie,Zestaw,KartaGraficzna,Biblioteka
from .forms import RegisterForm,LoginForm,DodajDoZestawuForm

def mainSite(request):
    uzytkownik = request.user
    kontekst = {'uzytkownik': uzytkownik}
    return render(request, 'main.html', kontekst)

def onas(request):
    uzytkownik = request.user
    kontekst = {'uzytkownik': uzytkownik}
    return render(request, 'about.html', kontekst)

def kontakt(request):
    uzytkownik = request.user
    kontekst = {'uzytkownik': uzytkownik}
    return render(request, 'contact.html', kontekst)

def register(request):
 if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
        login = request.POST["login"]
        password = request.POST["password"]
        imie = request.POST["imie"]
        nazwisko = request.POST["nazwisko"]
        email = request.POST["email"]
        user, created = User.objects.get_or_create(username=login)
        if (created):
            user.set_password(password)
            user.save()
            user_extended, created_extended = UserExtended.objects.get_or_create(user=user, imie=imie,
                                                                                 nazwisko=nazwisko, email=email)
            user_extended.save()
            messages.success(request, "Pomyślnie zarejestrowano")
            return redirect('/servicesite/logowanie')
        else:
            messages.warning(request, "Użytkownik już istnieje")

    else:
        return redirect('/servicesite/rejestracja')

    if (not request.user.is_authenticated):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    else:
        return redirect('/servicesite/rejestracja')

 else:
     uzytkownik = request.user
     form = RegisterForm()
     context = {'form': form,
                'uzytkownik' : uzytkownik}
     return render(request, 'register.html', context)

def logowanie(request):
    uzytkownik = request.user
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["login"]
            password = request.POST["password"]
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)

                messages.success(request, "Pomyślnie zalogowano")
                return redirect('/servicesite')
            else:
                messages.warning(request, "Nieprawidłowe dane")
                return redirect('/servicesite/logowanie')
        else:
            return redirect('/servicesite/logowanie')

        if (request.user.is_authenticated):
            messages.warning(request, "Już jesteś zalogowany")
            return render(request, 'login.html')
        else:
            kontekst = {'form': form,
                       'uzytkownik': uzytkownik}
            return render(request, 'login.html', kontekst)
    else:
        form = LoginForm()
        kontekst = {'form': form,
                    'uzytkownik': uzytkownik}

        return render(request, 'login.html', kontekst)

def logoutz(request):
    if (request.user.is_authenticated):
        logout(request)
        messages.success(request, "Wylogowano pomyślnie")
        return redirect('/servicesite')

def makecomp(request):
    if (request.user.is_authenticated):
        uzytkownik = request.user
        form = DodajDoZestawuForm(request.POST)
        kontekst = {
            'uzytkownik': uzytkownik,
            'form': form,
        }
        return render(request, 'makecomp.html', kontekst)
    else:
        messages.warning(request, "Aby złożyć swój zestaw należy się zalogować")
        return redirect('/servicesite/logowanie')

def wyswietl_zestawy(request):
    if request.user.is_authenticated:

        uzytkownik = request.user
        biblioteka = Biblioteka.objects.filter(user=request.user)
        uzytkownik_extended = UserExtended.objects.get(user=uzytkownik.id)

        if biblioteka.exists():
            biblio = biblioteka[0]

            kontekst = {
                'uzytkownik' : uzytkownik,
                'uzytkownik_extended' : uzytkownik_extended,
                'biblio': biblio
            }

            return render(request, 'biblio.html', kontekst)
        else:
            kontekst1 = {

                'uzytkownik': uzytkownik,
                'uzytkownik_extended': uzytkownik_extended,
            }

            return render(request, 'biblio.html', kontekst1)
    else:
        messages.warning(request, "Aby przeglądać koszyk należy się zalogować")
        return redirect('/servicesite/logowanie')

def zestaw_dodajdobiblio(request):
    if request.method == 'POST':
        form = DodajDoZestawuForm (request.POST)

        if form.is_valid():
            cleandata=form.cleaned_data
            procesor = get_object_or_404(Procesor, nazwa = cleandata.get('procesor'))
            kartagraficzna = get_object_or_404(KartaGraficzna, nazwa = cleandata.get('kartagraficzna'))
            ram = get_object_or_404(Ram, nazwa=cleandata.get('ram'))
            plytaglowna = get_object_or_404(PlytaGlowna, nazwa=cleandata.get('plytaglowna'))
            dysk = get_object_or_404(Dysk, nazwa=cleandata.get('dysk'))
            monitor = get_object_or_404(Monitor, nazwa=cleandata.get('monitor'))
            obudowa = get_object_or_404(Obudowa, nazwa=cleandata.get('obudowa'))
            chlodzenie = get_object_or_404(Chlodzenie, nazwa=cleandata.get('chlodzenie'))
            uzyt_extended = UserExtended.objects.get(user=request.user.id)

            zestaw, created = Zestaw.objects.get_or_create(user=request.user, user_extended=uzyt_extended,  procesor = procesor, plytaglowna = plytaglowna,  kartagraficzna = kartagraficzna,ram = ram, dysk = dysk, monitor = monitor, obudowa = obudowa, chlodzenie = chlodzenie, cena_total= procesor.cena + kartagraficzna.cena + ram.cena + plytaglowna.cena + dysk.cena + obudowa.cena + chlodzenie.cena + monitor.cena)


            biblio = Biblioteka.objects.filter(user=request.user)

            if biblio.exists():
                biblio = biblio[0]
                biblio.items.add(zestaw)
                biblio.save()
            else:
                biblio = Biblioteka.objects.create(user=request.user)
                biblio.items.add(zestaw)
                biblio.save()
        else:
                messages.warning(request, "Blad dodawania")
    return redirect('/servicesite/makecomputer')




