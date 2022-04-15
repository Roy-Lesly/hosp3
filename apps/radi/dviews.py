from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *


def radiUserList(request):
    qs = RadiUser.objects.all()
    user = request.user
    i = 0
    for p in qs:
        if user.username == str(qs[i]):
            return True
        i += 1
    return False


# ======================= ECHO DASHBOARD =======================================
@login_required(login_url="/login/")
def u_index(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'ECHO DASH',
            "page_title": "ECHOGRAPHY",
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_udash.html', context)
    else:
        return render(request, 'radi/radi_welcome.html')


@login_required(login_url="/login/")
def u_statistics_0(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'ECHO DASH',
            "page_title": "ECHO STATS",
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_udash0.html', context)
    else:
        return render(request, 'radi/radi_welcome.html')


@login_required(login_url="/login/")
def u_statistics_1(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'ECHO DASH',
            "page_title": "ECHO STATS",
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_udash_page1.html', context)
    else:
        return render(request, 'radi/radi_welcome.html')


def u_statistics_2(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'ECHO DASH',
            "page_title": "ECHO STATS",
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_udash_page2.html', context)
    else:
        return render(request, 'radi/radi_welcome.html')


@login_required(login_url="/login/")
def u_income(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'ECHO DASH',
            "page_title": "ECHO STATS",
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_udash_page2.html', context)
    else:
        return render(request, 'radi/radi_welcome.html')\



@login_required(login_url="/login/")
def u_other(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'ECHO DASH',
            "page_title": "ECHO STATS",
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_dash_page3.html', context)
    else:
        return render(request, 'radi/radi_welcome.html')

        return render(request, 'labo/labo_welcome.html')

# ==============================================================================
# ======================= XRAY DASHBOARD =======================================
@login_required(login_url="/login/")
def x_index(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'XRAY DASH',
            "page_title": "XRAY",
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_xdash.html', context)
    else:
        return render(request, 'radi/radi_welcome.html')


@login_required(login_url="/login/")
def x_statistics_1(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'XRAY DASH',
            "page_title": "XRAY STATS",
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_xdash_page1.html', context)
    else:
        return render(request, 'radi/radi_welcome.html')


def x_statistics_2(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'XRAY DASH',
            "page_title": "XRAY STATS",
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_xdash_page2.html', context)
    else:
        return render(request, 'radi/radi_welcome.html')


@login_required(login_url="/login/")
def x_income(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'XRAY DASH',
            "page_title": "XRAY STATS",
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_xdash_page2.html', context)
    else:
        return render(request, 'radi/radi_welcome.html')\



@login_required(login_url="/login/")
def x_other(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'ECHO DASH',
            "page_title": "ECHO STATS",
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_dash_page3.html', context)
    else:
        return render(request, 'radi/radi_welcome.html')

        return render(request, 'labo/labo_welcome.html')