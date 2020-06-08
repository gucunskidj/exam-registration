from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('br_indexa', 'ime_studenta', 'prezime_studenta', 'smer', 'god_studija' )
    list_filter = ('smer', 'god_studija', 'predmeti')
    search_fields = ['ime_studenta', 'prezime_studenta', 'br_indexa']

class PredmetAdmin(admin.ModelAdmin):
    list_display = ('naziv_predmeta', 'profesor', 'semestar', 'vrsta_predmeta')
    list_filter = ('smer', 'semestar', 'profesor')
    search_fields = ['naziv_predmeta']


admin.site.register(Smer)
admin.site.register(Profesor)
admin.site.register(Predmet, PredmetAdmin)
admin.site.register(Student, StudentAdmin)