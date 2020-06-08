from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Smer(models.Model):
    naziv_smera = models.CharField(max_length=500)
    
    class Meta:
        verbose_name_plural = 'Smerovi'
        ordering = ['naziv_smera']

    def __str__(self):
        return self.naziv_smera


class Profesor(models.Model):
    prezime_i_ime = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Profesori'
        ordering = ['prezime_i_ime']

    def __str__(self):
        return self.prezime_i_ime


class Predmet(models.Model):
    SEMESTAR = (
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        ('V', 'V'),
        ('VI', 'VI'),
        ('VII', 'VII'),
        ('VIII', 'VIII'),
    )
    VRSTA = (
        ('Obavezni', 'Obavezni'),
        ('Izborni', 'Izborni') 
    )

    sifra_predmeta = models.CharField(primary_key=True, max_length=20)
    naziv_predmeta = models.CharField(max_length=200)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, blank=True, null=True)
    datum_ispita = models.DateTimeField(blank=True, null=True)
    semestar = models.CharField(max_length=200, choices=SEMESTAR)
    espb_bodova = models.IntegerField(null=True)
    smer = models.ManyToManyField(Smer)
    vrsta_predmeta = models.CharField(max_length=200, choices=VRSTA, blank=True, null=True)
    prijava = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Predmeti'
        ordering = ['semestar', 'sifra_predmeta']

    def __str__(self):
        return self.sifra_predmeta + ', ' + self.naziv_predmeta + ', ' + self.semestar + ' semestar' 



class Student(models.Model):
    GODINA = (
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    ime_studenta = models.CharField(max_length=200)
    prezime_studenta = models.CharField(max_length=200)
    br_indexa = models.CharField(primary_key=True, max_length=10)
    jmbg = models.CharField(max_length=13)
    smer = models.ForeignKey(Smer, on_delete=models.CASCADE, blank=True, null=True)
    predmeti = models.ManyToManyField(Predmet)
    god_studija = models.CharField(max_length=200, choices=GODINA)

    class Meta:
        verbose_name_plural = 'Studenti'

    def __str__(self):
        return self.ime_studenta + ' ' + self.prezime_studenta + ', ' + self.smer.naziv_smera + ', ' + self.god_studija + ' god.'


# class Ispit(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
#     predmeti = models.ManyToManyField(Predmet)