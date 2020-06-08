from django.urls import path
from . import views

#from django.contrib.auth import views as auth_views IND



urlpatterns = [
    path('', views.loginPage, name='login'),
    path('prijavi_ispite/', views.prijavi_ispite, name='prijavi_ispite'),
    path('prijavljeni_ispiti/', views.prijavljeni_ispiti, name='prijavljeni_ispiti'),
    path('logout/', views.logoutUser, name='logout'),
]