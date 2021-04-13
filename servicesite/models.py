from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class UserExtended(models.Model):
    class Meta: verbose_name_plural = 'UsersExtended'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imie = models.CharField(verbose_name=u"imie", max_length=50)
    nazwisko = models.CharField(verbose_name=u"nazwisko", max_length=50)
    email = models.CharField(verbose_name=u"email", max_length=150)

    def __str__(self):
        return self.user.username
class Procesor(models.Model):
    class Meta: verbose_name_plural = 'Procesor'
    nazwa = models.CharField(verbose_name='procesor', max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nazwa
class KartaGraficzna(models.Model):
    class Meta: verbose_name_plural = 'KartaGraficzna'
    nazwa = models.CharField(verbose_name='kartagraficzna', max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nazwa
class Ram(models.Model):
    class Meta: verbose_name_plural = 'Ram'
    nazwa = models.CharField(verbose_name='ram', max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nazwa
class PlytaGlowna(models.Model):
    class Meta: verbose_name_plural = 'PlytaGlowna'
    nazwa = models.CharField(verbose_name='plytaglowna', max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nazwa
class Dysk(models.Model):
    class Meta: verbose_name_plural = 'Dysk'
    nazwa = models.CharField(verbose_name='dsyk', max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nazwa
class Obudowa(models.Model):
    class Meta: verbose_name_plural = 'Obudowa'
    nazwa = models.CharField(verbose_name='obudowa', max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nazwa
class Monitor(models.Model):
    class Meta: verbose_name_plural = 'Monitor'
    nazwa = models.CharField(verbose_name='monitor', max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nazwa
class Chlodzenie(models.Model):
    class Meta: verbose_name_plural = 'Chlodzenie'
    nazwa = models.CharField(verbose_name='chlodzenie', max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nazwa

class Zestaw(models.Model):
    procesor = models.ForeignKey(Procesor, on_delete=models.CASCADE)
    kartagraficzna = models.ForeignKey(KartaGraficzna, on_delete=models.CASCADE)
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    plytaglowna = models.ForeignKey(PlytaGlowna, on_delete=models.CASCADE)
    dysk = models.ForeignKey(Dysk, on_delete=models.CASCADE)
    obudowa = models.ForeignKey(Obudowa, on_delete=models.CASCADE)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    chlodzenie = models.ForeignKey(Chlodzenie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    user_extended = models.ForeignKey(UserExtended, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    cena_total = models.DecimalField(max_digits=15, decimal_places=2)

    def get_object_price(self):
        return self.cena_total

    def calculate_price(self):
        return  self.procesor.cena + self.kartagraficzna.cena + self.ram.cena + self.plytaglowna.cena + self.dysk.cena + self.obudowa.cena + self.chlodzenie.cena + self.monitor.cena



class Biblioteka(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Zestaw)

    def get_items(self):
        return self.items.all()




