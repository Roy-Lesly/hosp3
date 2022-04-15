from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


def mateUserList(request):
    qs = MateUser.objects.all()
    user = request.user
    i = 0
    for p in qs:
        if user.username == str(qs[i]):
            return True
        i += 1
    return False


@login_required(login_url="/login/")
def mateWelcomeView(request):
    check = mateUserList(request)
    if check == True:
        context = {
            "title": 'MATERNITY Department',
            "page_title": 'Welcome to "MATERNITY"'
        }
        return render(request, 'mate/mate_welcome.html', context)
    else:
        return render(request, 'root/welcome.html')


# ==================== Mate Staff ===========================
@login_required(login_url="/login/")  # ok
def staff_List(request):
    check = mateUserList(request)
    if check == True:
        context = {
            "title": 'Maternity Staff List',
            "page_title": "MATERNITY",
            "mate_staff": MateStaff.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'mate/main2/mate_staff.html', context)


@login_required(login_url="/login/")  # ok
def staff_Create(request):
    if request.method == 'POST':
        form = MateStaffForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({"data": "SAVED"}, safe=False)
            except:
                return JsonResponse({"data": "EXIST ALREADY"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
    form = MateStaffForm()
    context = {
        'staff_form': form
    }
    html_form = render_to_string('mate/main2/staff_create.html', context, request=request)
    return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def staff_Update(request, id):
    check = mateUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = MateStaff.objects.get(id=id)
            form = MateStaffForm(instance=rs)
            context = {
                "staff_update": form,
                "staff_id": rs.id
            }
            html_form = render_to_string('mate/main2/staff_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            ls = MateStaff.objects.get(id=id)
            form = MateStaffForm(request.POST, instance=ls)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)


@login_required(login_url="/login/")  # ok
def staff_Delete(request, id):
    check = mateUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = MateStaff.objects.get(id=id)
            context = {
                "staff_delete": rs,
                "staff_id": rs.id
            }
            html_form = render_to_string('mate/main2/staff_delete.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rs = MateStaff.objects.get(id=id)
            if True:
                rs.delete()
                return JsonResponse({"data": "DELETED"}, safe=False)
            else:
                return JsonResponse({"data": "NOT DELETED"}, safe=False)

