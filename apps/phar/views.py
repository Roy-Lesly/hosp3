import django
# from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect

# from .models import *
from django.template.loader import render_to_string

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


@login_required(login_url="/login/")
def pharWelcomeView(request):
    check = pharUserList(request)
    if check == True:
        context = {
            "title": 'PHARMACY Department',
            "page_title": "PHARMACY"
        }
        return render(request, 'phar/phar_welcome.html', context)
    else:
        return render(request, 'root/welcome.html')


class PharmHomeView(View):

    def get(self, request):
        context = {
            "title": 'Pharmacy',
            'page_title': 'PHARMACY',
            'subtitle': 'HOME PAGE',
            # "short_title": 'RH'
        }
        return render(request, 'phar/disp/phar_pat_list.html', context)


class StoreHomeView(View):

    def get(self, request):
        context = {
            "title": 'XRAY',
            # "short_title": 'PH',
            'page_title': 'XRAY',
            'subtitle': 'HOME PAGE',
        }
        return render(request, 'phar/store/store_home.html', context)


# ==================== Phar Dept ====================Dept
@login_required(login_url="/login/")    # ok
def dept_Create_Update(request, id=0):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            if id == 0:                     # Insert Operation
                form = PharDeptForm()
            else:                           # Update Operation
                ls = PharDept.objects.get(id=id)
                form = PharDeptForm(instance=ls)
            context = {
                "title": 'Register / Update Pharmacy Dept',
                "page_title": "PHARMACY",
                "dept_form": form
            }
            return render(request, 'phar/main/phar_Dept_form.html', context)
        if request.method == 'POST':
            if id == 0:
                form = PharDeptForm(request.POST)
            else:
                ps = PharDept.objects.get(id=id)
                form = PharDeptForm(request.POST, instance=ps)
            if form.is_valid():
                form.save()
            return redirect('phar:deptList')


@login_required(login_url="/login/")    # ok
def dept_List(request):
    check = pharUserList(request)
    if check == True:
        context = {
            "title": 'Medical Pharmacy Dept List',
            "page_title": "PHARMACY",
            "phar_dept": PharDept.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'phar/main/phar_dept.html', context)


@login_required(login_url="/login/")    # ok
def dept_Delete(request, id=0):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            if id == 0:  # Insert Operation
                return redirect('phar:deptList')
            else:
                ps = PharDept.objects.get(id=id)
                ps.delete()
            return redirect('phar:deptList')


# ==================== Phar Staff =========================
@login_required(login_url="/login/")  # ok
def staff_List(request):
    check = pharUserList(request)
    if check == True:
        context = {
            "title": 'Pharmacy Staff List',
            "page_title": "PHARMACY",
            "phar_staff": PharStaff.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'phar/main2/phar_staff.html', context)


@login_required(login_url="/login/")  # ok
def staff_Create(request):
    if request.method == 'POST':
        form = PharStaffForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({"data": "SAVED"}, safe=False)
            except:
                return JsonResponse({"data": "EXIST ALREADY"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
    form = PharStaffForm()
    html_form = render_to_string('phar/main2/staff_create.html', {'staff_form': form}, request=request)
    return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def staff_Update(request, id):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = PharStaff.objects.get(id=id)
            form = PharStaffForm(instance=rs)
            context = {
                "staff_update": form,
                "staff_id": rs.id
            }
            html_form = render_to_string('phar/main2/staff_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            ls = PharStaff.objects.get(id=id)
            form = PharStaffForm(request.POST, instance=ls)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)


@login_required(login_url="/login/")  # ok
def staff_Delete(request, id):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = PharStaff.objects.get(id=id)
            context = {
                "staff_delete": rs,
                "staff_id": rs.id
            }
            html_form = render_to_string('radi/main2/staff_delete.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rs = PharStaff.objects.get(id=id)
            if True:
                rs.delete()
                return JsonResponse({"data": "DELETED"}, safe=False)
            else:
                print('not deleted')
                return JsonResponse({"data": "NOT DELETED"}, safe=False)


# ================== Phar Drug Category =====================
@login_required(login_url="/login/")    # ok
def category_Create_Update(request, id=0):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            if id == 0:                     # Insert Operation
                form = PharDrugCategoryForm()
            else:                           # Update Operation
                pc = PharDrugCategory.objects.get(id=id)
                form = PharDrugCategoryForm(instance=pc)
            context = {
                "title": 'Register / Update Pharmacy Category',
                "page_title": "PHARMACY",
                "category_form": form
            }
            return render(request, 'phar/main/phar_category_form.html', context)
        if request.method == 'POST':
            if id == 0:
                form = PharDrugCategoryForm(request.POST)
            else:
                lc = PharDrugCategory.objects.get(id=id)
                form = PharDrugCategoryForm(request.POST, instance=lc)
            if form.is_valid():
                form.save()
            return redirect('phar:categoryList')


@login_required(login_url="/login/")    # ok
def category_List(request):
    check = pharUserList(request)
    if check == True:
        context = {
            "title": 'Medical Pharmacy Category List',
            "page_title": "PHARMACY",
            "phar_category": PharDrugCategory.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'phar/main/phar_category.html', context)


@login_required(login_url="/login/")    # ok
def category_Delete(request, id=0):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            if id == 0:
                return redirect('phar:categoryList')
            else:
                pc = PharDrugCategory.objects.get(id=id)
                pc.delete()
            return redirect('phar:categoryList')


# ==================== Pharm Drug Type =====================
@login_required(login_url="/login/")    # ok
def type_Create_Update(request, id=0):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            if id == 0:                     # Insert Operation
                form = PharDrugTypeForm()
            else:                           # Update Operation
                lt = PharDrugType.objects.get(id=id)
                form = PharDrugTypeForm(instance=lt)
            context = {
                "title": 'Register / Update Pharmacy Exam',
                "page_title": "PHARMACY",
                "type_form": form
            }
            return render(request, 'phar/main/phar_type_form.html', context)
        if request.method == 'POST':
            if id == 0:
                form = PharDrugTypeForm(request.POST)
            else:
                pt = PharDrugType.objects.get(id=id)
                form = PharDrugTypeForm(request.POST, instance=pt)
            if form.is_valid():
                form.save()
            return redirect('phar:typeList')


@login_required(login_url="/login/")    # ok
def type_List(request):
    check = pharUserList(request)
    if check == True:
        context = {
            "title": 'Medical Pharmacy Type List',
            "page_title": "PHARMACY",
            "phar_drug": PharDrugType.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'phar/main/phar_type.html', context)


@login_required(login_url="/login/")    # ok
def type_Delete(request, id=0):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            if id == 0:
                return redirect('phar:typeList')
            else:
                pt = PharDrugType.objects.get(id=id)
                pt.delete()
            return redirect('phar:typeList')

