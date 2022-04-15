from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *


def laboUserList(request):
    qs = LaboUser.objects.all()
    user = request.user
    i = 0
    for p in qs:
        if user.username == str(qs[i]):
            return True
        i += 1
    return False


@login_required(login_url="/login/")
def index(request):
    check = laboUserList(request)
    if check == True:
        context = {
            "title": 'LAB DASH',
            "page_title": "LABORATORY",
        }
        if request.method == 'GET':
            return render(request, 'labo/main2/labo_dash.html', context)
    else:
        return render(request, 'labo/labo_welcome.html')\



@login_required(login_url="/login/")
def statistics(request):
    check = laboUserList(request)
    if check == True:
        context = {
            "title": 'LAB DASH',
            "page_title": "LABO STATS",
        }
        if request.method == 'GET':
            return render(request, 'labo/main2/labo_dash_page1.html', context)
    else:
        return render(request, 'labo/labo_welcome.html')\



@login_required(login_url="/login/")
def income(request):
    check = laboUserList(request)
    if check == True:
        context = {
            "title": 'LABO DASH',
            "page_title": "LABO STATS",
        }
        if request.method == 'GET':
            return render(request, 'labo/main2/labo_dash_page2.html', context)
    else:
        return render(request, 'labo/labo_welcome.html')\



@login_required(login_url="/login/")
def other(request):
    check = laboUserList(request)
    if check == True:
        context = {
            "title": 'LABO DASH',
            "page_title": "LABO STATS",
        }
        if request.method == 'GET':
            return render(request, 'labo/main2/labo_dash_page3.html', context)
    else:
        return render(request, 'labo/labo_welcome.html')