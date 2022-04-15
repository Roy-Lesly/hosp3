from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string

from .models import *
from .forms import *


# Create your views here.
def radiUserList(request):
    qs = RadiUser.objects.all()
    user = request.user
    i = 0
    for p in qs:
        if user.username == str(qs[i]):
            return True
        i += 1
    return False


@login_required(login_url="/login/")
def radiWelcomeView(request):
    check = radiUserList(request)
    if check == True:
        context = {
            # "title": 'Medical Radiology Department',
            "title": 'RADIOLOGY INFORMATION SYSTEM',
            "page_title": "RADIOLOGY",
            "sub_title": "Home Page",
        }
        return render(request, 'radi/radi_welcome.html', context)
    else:
        return render(request, 'root/welcome.html')


@login_required(login_url="/login/")
def echoHomeView(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'Ultras88ound',
            'subtitle': 'Echo HOME PAGE',
        }
        return render(request, 'radio/echo/echo_home.html', context)
    else:
        return render(request, 'root/welcome.html')


# ==================== Radio Staff ==========================
@login_required(login_url="/login/")  # ok
def staff_List(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'Radiology Staff List',
            "page_title": "RADIOLOGY",
            "radi_staff": RadiStaff.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_staff.html', context)


@login_required(login_url="/login/")  # ok
def staff_Create(request):
    if request.method == 'POST':
        form = RadiStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"data": "SAVED"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
        return redirect('regi:staffList')
    form = RadiStaffForm()
    html_form = render_to_string('radi/main2/staff_create.html', {'staff_form': form}, request=request)
    return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def staff_Update(request, id):
    check = radiUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = RadiStaff.objects.get(id=id)
            form = RadiStaffForm(instance=rs)
            context = {
                "staff_update": form,
                "staff_id": rs.id
            }
            html_form = render_to_string('radi/main2/staff_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            ls = RadiStaff.objects.get(id=id)
            form = RadiStaffForm(request.POST, instance=ls)
            print(form.data)
            print(form.errors)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)


@login_required(login_url="/login/")  # ok
def staff_Delete(request, id):
    check = radiUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = RadiStaff.objects.get(id=id)
            context = {
                "staff_delete": rs,
                "staff_id": rs.id
            }
            html_form = render_to_string('radi/main2/staff_delete.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rs = RadiStaff.objects.get(id=id)
            if True:
                rs.delete()
                return JsonResponse({"data": "DELETED"}, safe=False)
            else:
                print('not deleted')
                return JsonResponse({"data": "NOT DELETED"}, safe=False)


# ===================== Radio Exam Category =====================
@login_required(login_url="/login/")    # ok
def category_List(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'Medical Radiology Category List',
            "page_title": "RADIOLOGY",
            "radi_category": RadiTestCategory.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_category.html', context)


@login_required(login_url="/login/")    # ok
def category_Create(request):
    if request.method == 'POST':
        form = RadiTestCategoryForm(request.POST)
        print(form.data)
        print(form.errors)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({"data": "SAVED"}, safe=False)
            except:
                return JsonResponse({"data": "EXIST ALREADY"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
    form = RadiTestCategoryForm()
    html_form = render_to_string('radi/main2/category_create.html', {'category_form': form}, request=request)
    return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def category_Update(request, id):
    check = radiUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = RadiTestCategory.objects.get(id=id)
            form = RadiTestCategoryForm(instance=rs)
            context = {
                "category_update": form,
                "category_id": rs.id
            }
            html_form = render_to_string('radi/main2/category_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            ls = RadiTestCategory.objects.get(id=id)
            form = RadiTestCategoryForm(request.POST, instance=ls)
            print(form.data)
            print(form.errors)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)


@login_required(login_url="/login/")    # ok
def category_Delete(request, id):
    check = radiUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = RadiTestCategory.objects.get(id=id)
            context = {
                "category_delete": rs,
                "category_id": rs.id
            }
            html_form = render_to_string('radi/main2/category_delete.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rs = RadiTestCategory.objects.get(id=id)
            if True:
                rs.delete()
                return JsonResponse({"data": "DELETED"}, safe=False)
            else:
                print('not deleted')
                return JsonResponse({"data": "NOT DELETED"}, safe=False)


# ======================== Radio Exam Type ========================
@login_required(login_url="/login/")    # ok
def type_List(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'Medical Radiology Exam List',
            "page_title": "RADIOLOGY",
            "radi_type": RadiTestType.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_type.html', context)


@login_required(login_url="/login/")    # ok
def type_Create(request):
    if request.method == 'POST':
        form = RadiTypeForm(request.POST)
        print(form.data)
        print(form.errors)
        if form.is_valid():
            form.save()
            return JsonResponse({"data": "SAVED"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
        return redirect('regi:staffList')
    form = RadiTypeForm()
    html_form = render_to_string('radi/main2/type_create.html', {'type_form': form}, request=request)
    return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def type_Update(request, id):
    check = radiUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = RadiTestType.objects.get(id=id)
            form = RadiTypeForm(instance=rs)
            context = {
                "type_update": form,
                "type_id": rs.id
            }
            html_form = render_to_string('radi/main2/type_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            ls = RadiTestType.objects.get(id=id)
            form = RadiTypeForm(request.POST, instance=ls)
            print(form.data)
            print(form.errors)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)


@login_required(login_url="/login/")    # ok
def type_Delete(request, id):
    check = radiUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = RadiTestType.objects.get(id=id)
            context = {
                "type_delete": rs,
                "type_id": rs.id
            }
            html_form = render_to_string('radi/main2/type_delete.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rs = RadiTestType.objects.get(id=id)
            if True:
                rs.delete()
                return JsonResponse({"data": "DELETED"}, safe=False)
            else:
                print('not deleted')
                return JsonResponse({"data": "NOT DELETED"}, safe=False)


# ======================== Radio Department ========================
@login_required(login_url="/login/")    # ok
def dept_List(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'Medical Radiology Department List',
            "page_title": "RADIOLOGY",
            "radi_dept": RadiDept.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_dept.html', context)


@login_required(login_url="/login/")    # ok
def dept_Create(request):
    if request.method == 'POST':
        form = RadiDeptForm(request.POST)
        print(form.data)
        print(form.errors)
        if form.is_valid():
            form.save()
            return JsonResponse({"data": "SAVED"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
    form = RadiDeptForm()
    html_form = render_to_string('radi/main2/dept_create.html', {'dept_form': form}, request=request)
    return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def dept_Update(request, id):
    check = radiUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = RadiDept.objects.get(id=id)
            form = RadiDeptForm(instance=rs)
            context = {
                "dept_update": form,
                "dept_id": rs.id
            }
            html_form = render_to_string('radi/main2/dept_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            ls = RadiDept.objects.get(id=id)
            form = RadiDeptForm(request.POST, instance=ls)
            print(form.data)
            print(form.errors)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)
            else:
                return JsonResponse({"data": "CANNOT UPDATE"}, safe=False)


@login_required(login_url="/login/")  # ok
def patient_Create_Modal_Detail_u(request, book_num):
    '''
    This is to Display Patient Details after creation
    '''
    if request.method == 'POST':
        form = RegPatientForm(request.POST)
        print(form.data)
        print(form.errors)

        try:
            saved_patient = Patient.objects.get(reg_num=request.POST['reg_num'])
            sn = saved_patient.sn
            full_name = saved_patient.full_name
            address = saved_patient.address
            age = saved_patient.age
            phone = saved_patient.Phone
            pat = [sn, full_name, address, age, phone]
            res = {'data': 'SAVED', 'patient': pat}
            print('saved')
            print(pat)
            return JsonResponse(res, safe=False)
        except:
            pass
        if form.is_valid():
            try:
                obj = form.save(commit=False)
                obj.reg_num = request.POST['reg_num2']
                obj.save()
                print("regi Pat saved")
                print(request.POST['reg_num2'])
                saved_patient = Patient.objects.all().get(reg_num=request.POST['reg_num2'])
                sn = saved_patient.sn
                full_name = saved_patient.full_name
                address = saved_patient.address
                age = saved_patient.age
                phone = saved_patient.Phone
                pat = [sn, full_name, address, age, phone]
                res = {'data': 'SAVED', 'patient': pat}
                print(pat)
                return JsonResponse(res, safe=False)
            except:
                res = {'data': 'EXIST ALREADY', 'patient': []}
                return JsonResponse(res, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
    print("modal1")
    print(book_num)
    exam_num_list = []
    uexam1 = UExam.objects.get(book_num=book_num)
    uexam2 = UExam.objects.filter(book_num=book_num).values_list('patient', flat=True)
    upat1 = UPatient.objects.filter(un__in=uexam2)
    upat2 = UPatient.objects.filter(un__in=uexam2).values_list('patient', flat=True)
    us_num = uexam1.patient_id
    ex = UExam.objects.filter(patient_id=us_num)
    pat1 = Patient.objects.filter(sn__in=upat2)
    for x in ex:
        exam_num_list.append(x.book_num)
    print(exam_num_list)
    print("xxxxxxxxxxxxxxxxx")
    print(uexam1)
    print(uexam2)   # unique U patient num
    print("===============")
    print(upat1)
    print(upat2)    # unique sn
    print(upat2[0])    # unique sn

    context = {"sn": upat2[0], "us_num": us_num, "exam_num": exam_num_list}
    html_form = render_to_string('radi/noti/echo_pat_create_details.html', context, request=request)
    return JsonResponse({"html_form": html_form})


# ========================== HANDING OVER ==========================
'''@login_required(login_url="/login/")  # ok
def handing_Create(request):
    if request.method == 'POST':
        print(request.POST)
        form = RadiHandingForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return JsonResponse({"data": "SAVED"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
        return redirect('radi:HandingList')
    form = RadiHandingForm()
    html_form = render_to_string('radi/main/radi_handing_create.html', {'handing_form': form}, request=request)
    return JsonResponse({"html_form": html_form})'''

@login_required(login_url="/login/")  # ok
def handing_Create(request):
    if request.method == 'GET':
        form = RadiHandingForm()
        context = {
            "title": 'Handing Over History',
            "page_title": "RADIOLOGY",
            "handing_form": form
        }
        return render(request, 'radi/main/radi_handing_create.html', context)
    if request.method == 'POST':
        print(request.POST)
        form = RadiHandingForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return JsonResponse({"data": "SAVED"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
        return redirect('radi:HandingList')
    form = RadiHandingForm()
    html_form = render_to_string('radi/main/radi_handing_create.html', {'handing_form': form}, request=request)
    return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def handing_List(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'Handing Over History',
            "page_title": "RADIOLOGY",
            "radi_handing": RadiHanding.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'radi/main/radi_handing_list.html', context)


@login_required(login_url="/login/")  # ok
def handing_Update(request, id):
    check = radiUserList(request)
    if check == True:
        if request.method == 'GET':
            rh = RadiHanding.objects.get(id=id)
            form = RadiHandingForm(instance=rh)
            context = {
                "handing_update": form,
                "handing_id": rh.id
            }
            html_form = render_to_string('radi/main/handing_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rh = RadiHanding.objects.get(id=id)
            form = RadiHandingForm(request.POST, instance=rh)
            print(form.data)
            print(form.errors)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)


@login_required(login_url="/login/")    # ok
def handing_Delete(request, id):
    check = radiUserList(request)
    if check == True:
        if request.method == 'GET':
            rh = RadiHanding.objects.get(id=id)
            context = {
                "handing_delete": rh,
                "handing_id": rh.id
            }
            html_form = render_to_string('radi/main/handing_delete.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rh = RadiHanding.objects.get(id=id)
            if True:
                rh.delete()
                return JsonResponse({"data": "DELETED"}, safe=False)
            else:
                print('not deleted')
                return JsonResponse({"data": "NOT DELETED"}, safe=False)


# ========================== MAINTENANCE ==========================
@login_required(login_url="/login/")  # ok
def maintenance_Create(request):
    if request.method == 'POST':
        form = HandingForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"data": "SAVED"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
        return redirect('radi:HandingList')
    form = HandingForm()
    html_form = render_to_string('radi/main/handing_create.html', {'handing_form': form}, request=request)
    return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def maintenance_List(request):
    check = radiUserList(request)
    if check == True:
        context = {
            "title": 'Handing Over History',
            "page_title": "RADIOLOGY",
            "radi_handing": RadiHanding.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'radi/main2/radi_handing.html', context)


@login_required(login_url="/login/")  # ok
def maintenance_Update(request, id):
    check = radiUserList(request)
    if check == True:
        if request.method == 'GET':
            rh = RadiHanding.objects.get(id=id)
            form = RadiHandingForm(instance=rh)
            context = {
                "handing_update": form,
                "handing_id": rh.id
            }
            html_form = render_to_string('radi/main/handing_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rh = RadiHanding.objects.get(id=id)
            form = RadiHandingForm(request.POST, instance=rh)
            print(form.data)
            print(form.errors)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)


@login_required(login_url="/login/")    # ok
def maintenance_Delete(request, id):
    check = radiUserList(request)
    if check == True:
        if request.method == 'GET':
            rh = RadiHanding.objects.get(id=id)
            context = {
                "handing_delete": rh,
                "handing_id": rh.id
            }
            html_form = render_to_string('radi/main/handing_delete.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rh = RadiHanding.objects.get(id=id)
            if True:
                rh.delete()
                return JsonResponse({"data": "DELETED"}, safe=False)
            else:
                print('not deleted')
                return JsonResponse({"data": "NOT DELETED"}, safe=False)