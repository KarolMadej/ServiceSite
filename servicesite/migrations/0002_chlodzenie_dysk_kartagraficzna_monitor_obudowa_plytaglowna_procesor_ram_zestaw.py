# Generated by Django 3.0.2 on 2020-01-23 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicesite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chlodzenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100, verbose_name='chlodzenie')),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Chlodzenie',
            },
        ),
        migrations.CreateModel(
            name='Dysk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100, verbose_name='dsyk')),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Dysk',
            },
        ),
        migrations.CreateModel(
            name='KartaGraficzna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100, verbose_name='kartagraficzna')),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'KartaGraficzna',
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100, verbose_name='monitor')),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Monitor',
            },
        ),
        migrations.CreateModel(
            name='Obudowa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100, verbose_name='obudowa')),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Obudowa',
            },
        ),
        migrations.CreateModel(
            name='PlytaGlowna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100, verbose_name='plytaglowna')),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'PlytaGlowna',
            },
        ),
        migrations.CreateModel(
            name='Procesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100, verbose_name='procesor')),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Procesor',
            },
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100, verbose_name='ram')),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Ram',
            },
        ),
        migrations.CreateModel(
            name='Zestaw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('cena_total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('chlodzenie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicesite.Chlodzenie')),
                ('dysk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicesite.Dysk')),
                ('kartagraficzna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicesite.KartaGraficzna')),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicesite.Monitor')),
                ('obudowa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicesite.Obudowa')),
                ('plytaglowna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicesite.PlytaGlowna')),
                ('procesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicesite.Procesor')),
                ('ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicesite.Ram')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_extended', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicesite.UserExtended')),
            ],
        ),
    ]
