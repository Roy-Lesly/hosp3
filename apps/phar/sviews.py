import django
# from django.conf import settings
from django.shortcuts import render, redirect

# from .models import *
from .forms import *
from django.views import View
from django.contrib.auth.decorators import login_required


# Create your views here.
def pharUserList(request):
    allUser = PharUser.objects.all().order_by('username_id')
    userList = []
    for p in allUser:
        ps = str(p)
        userList.append(ps)
    user = request.user.username
    if user in userList:
        return True
    else:
        return False

