from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User


# Create your views here.


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('prijavi_ispite')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('prijavi_ispite')
            else:
                messages.info(request, '*Uneli ste pogresan username ili password') 

        context = {}
        return render(request, 'login/loginform.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def prijavi_ispite(request):

    username = request.user

    studenti = Student.objects.filter(user=username)

    predmeti = Predmet.objects.filter(student__br_indexa=username)

    # if request.method == 'GET':
    #     checkbox = request.GET.get('ckb')
    #     request.session['checkbox'] = checkbox
    
    

    context = {
        'predmeti': predmeti,
        'studenti': studenti,
        # 'checkbox': checkbox,
    }

    return render(request, 'login/homepage.html', context)


@login_required(login_url='login')
def prijavljeni_ispiti(request): 

    username = request.user

    predmeti = Predmet.objects.filter(student__br_indexa=username)

    #checkbox = ''

    # if request.method == 'POST':
    #     checkbox = request.session['checkbox']
    
    # checkbox = request.session['checkbox']
    

    context = {
        'predmeti': predmeti,
        # 'checkbox': checkbox,
    }

    return render(request, 'login/prijavljeni_ispiti.html', context)