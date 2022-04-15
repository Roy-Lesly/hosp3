import datetime
import random
from datetime import datetime as dt

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .forms import *
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
now = datetime.datetime.today()

def regiUserList(request):
    allUser = RegiUser.objects.all().order_by('username_id')
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
def regiWelcomeView(request):
    check = regiUserList(request)
    if check == True:
        context = {
            "title": 'Registration Department',
            "page_title": 'REGISTRATION'
        }
        return render(request, 'regi/regi_welcome.html', context)
    else:
        print("Not Department User")
        return render(request, 'root/welcome.html')


@login_required(login_url="/login/")
def regiRegistration(request):
    check = regiUserList(request)
    if check == True:
        context = {
            "title": 'Registration Department',
            "page_title": "REGISTRATION"
        }
        return render(request, 'regi/reg/regi_pat_create.html', context)
    else:
        return render(request, 'root/welcome.html')


@login_required(login_url="/login/")
def regiPayment(request):
    check = regiUserList(request)
    if check == True:
        context = {
            "title": 'Registration Department',
            "page_title": "REGISTRATION"
        }
        return render(request, 'regi/reg/regi_pat_create.html', context)
    else:
        return render(request, 'root/welcome.html')


# ==================== Regi Patieent ==========================
@login_required(login_url="/login/")  # ok
def patient_List(request):
    check = regiUserList(request)
    if check == True:
        context = {
            "title": 'Registration Patient List',
            "page_title": "REGISTRATION",
            "sub_title": "REGISTRATION",
            "patients": Patient.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'regi/reg/regi_pat_list.html', context)


@login_required(login_url="/login/")  # ok
def patient_Create(request):
    if request.method == 'POST':
        form = RegPatientForm(request.POST)
        full_name = str(request.POST['first_name']).upper() + " " + str(request.POST['last_name']).upper()
        if Patient.objects.filter(reg_num=request.POST['reg_num']):
            return JsonResponse({"data": "REG NUM EXIST ALREADY"}, safe=False)
        elif Patient.objects.filter(full_name=full_name):
            return JsonResponse({"data": "FULL NAME EXIST ALREADY"}, safe=False)
        elif len(request.POST['Phone']) != 9:
            return JsonResponse({"data": "INVALID PHONE NUMBER"}, safe=False)
        elif Patient.objects.filter(Phone=request.POST['Phone']):
            return JsonResponse({"data": "PHONE EXIST ALREADY"}, safe=False)
        if form.is_valid():
            form.save()
            return JsonResponse({"data": "SAVED"}, safe=False)
        else:
            print(form.data)
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
        return redirect('regi:staffList')
    form = RegPatientForm()
    context = {'patient_form': form, 'title': 'Registration', 'page_title': 'REGISTRATION',
               'sub_title': 'NEW PATIENT REGISTRATION' }
    return render(request, 'regi/reg/regi_pat_create.html', context)


@login_required(login_url="/login/")  # ok
def patient_Update(request, id):
    check = regiUserList(request)
    if check == True:
        if request.method == 'GET':
            rp = Patient.objects.get(sn=id)
            form = RegPatientForm(instance=rp)
            context = {
                "patient_update": form,
                "patient_id": rp.sn
            }
            html_form = render_to_string('regi/reg/regi_pat_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rp = Patient.objects.get(sn=id)
            form = RegPatientForm(request.POST, instance=rp)
            print(form.errors)
            if len(request.POST['Phone']) != 9:
                return JsonResponse({"data": "INVALID PHONE NUMBER"}, safe=False)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)
            else:
                return JsonResponse({"data": "NOT UPDATED"}, safe=False)


@login_required(login_url="/login/")  # ok
def patient_Delete(request, id):
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


def checkRegNum(request):
    if request.is_ajax and request.method == "GET":
        reg_num = request.GET.get("reg_num", None)
        qs = Patient.objects.all().filter(reg_num=reg_num)
        if qs.exists():
            print("exist")
            return JsonResponse({"Not valid": True}, status=200)
        else:
            print("not exist")
            return JsonResponse({"Valid": True}, status=200)


class RegRegistrationView(LoginRequiredMixin, View):
    login_url = reverse_lazy('authentication:login')

    def get(self, request):
        context = {
            "title": 'Registration',
            'page_title': 'REGISTRATION',
        }
        return render(request, 'regi/reg/regi_pat_list.html', context)


class RegPaymentView(LoginRequiredMixin, View):
    login_url = reverse_lazy('authentication:login')

    def get(self, request):
        context = {
            "title": 'Payment',
            'page_title': 'PAYMENT',
            'subtitle': 'HOME PAGE',
        }
        return render(request, 'regi/pay/regP_home.html', context)


# --------------------- Regi Staff -------------------------
@login_required(login_url="/login/")  # ok
def staff_List(request):
    check = regiUserList(request)
    if check == True:
        context = {
            "title": 'Registration Staff List',
            "page_title": "REGISTRATION",
            "regi_staff": RegiStaff.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'regi/main2/regi_staff.html', context)


@login_required(login_url="/login/")  # ok
def staff_Create(request):
    if request.method == 'POST':
        form = RegiStaffForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({"data": "SAVED"}, safe=False)
            except:
                return JsonResponse({"data": "EXIST ALREADY"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
        return redirect('regi:staffList')
    form = RegiStaffForm()
    context = {'staff_form': form}
    html_form = render_to_string('regi/main2/staff_create.html', context, request=request)
    return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def staff_Update(request, id):
    check = regiUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = RegiStaff.objects.get(id=id)
            form = RegiStaffForm(instance=rs)
            context = {
                "staff_update": form,
                "staff_id": rs.id
            }
            html_form = render_to_string('regi/main2/staff_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            ls = RegiStaff.objects.get(id=id)
            form = RegiStaffForm(request.POST, instance=ls)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)


@login_required(login_url="/login/")  # ok
def staff_Delete(request, id):
    check = regiUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = RegiStaff.objects.get(id=id)
            context = {
                "staff_delete": rs,
                "staff_id": rs.id
            }
            html_form = render_to_string('regi/main2/staff_delete.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rs = RegiStaff.objects.get(id=id)
            if True:
                rs.delete()
                return JsonResponse({"data": "DELETED"}, safe=False)
            else:
                return JsonResponse({"data": "NOT DELETED"}, safe=False)


def patSearch(request):
    if request.method == 'GET':
        print("get")
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')

        patients = XExam.objects.all().filter(patient_id__date_created__istartswith=search_str) \
                   | XExam.objects.all().filter(ex_sn__istartswith=search_str)

        '''patients = Patient.objects.all().filter(
            first_name__istartswith=search_str) | Patient.objects.all().filter(
                sn__startswith=search_str) | Patient.objects.all().filter(
                    last_name__istartswith=search_str)'''
        # data = list(patients.values())
        if patients.exists():
            data = serializers.serialize("json", patients)
            return JsonResponse(data, safe=False)
        else:
            data = 'No Patients Found! ...'
            return JsonResponse(data, safe=False)


# ------------------------- Modals -------------------------
@login_required(login_url="/login/")  # ok
def patient_Create_Modal_u(request):
    '''
    This is to create Reg Patient From Echo
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
        n = random.randrange(1000, 9999)
        if len(request.POST["Phone"]) < 9:
            res = {'data': 'INVALID PHONE NUMBER', 'patient': ""}
            return JsonResponse(res, safe=False)
        if form.is_valid():
            try:
                obj = form.save(commit=False)
                obj.reg_num = request.POST['reg_num2']
                print(request.POST["Phone"])
                obj.save()
                print("regi Pat saved")
                #saved_patient = Patient.objects.all().order_by('date_created').last()
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
    form = RegPatientForm()
    html_form = render_to_string('regi/main2/modal_regi_upat_create.html', {'pat_form': form}, request=request)
    return JsonResponse({"html_form": html_form})


@login_required
def patient_update(request, sn):
    pat = Patient.objects.get(sn=sn)
    sn = pat.sn
    reg_num = pat.reg_num
    full_name = pat.full_name
    first_name = pat.first_name
    last_name = pat.last_name
    address = pat.address
    sex = pat.sex
    dob = pat.dob.strftime("%Y-%m-%d")
    phone = pat.Phone
    data = {'sn': sn, 'reg_num': reg_num, "full_name": full_name, "first_name": first_name,
            "last_name": last_name, "sex": sex, 'phone': phone, 'address': address,"dob":dob}
    if request.method == 'POST':
        form = RegPatientForm(request.POST, instance=pat)
        form1 = request.POST
        print("request.POST1")
        print(form1)
        if form.is_valid():
            if True:
                print("form.data")
                print(form.data)
                print(form.errors)
                instance = form.save(commit=False)
                instance.reg_num = form.data["reg_num2"]
                instance.address = form.data["address"]
                instance.sex = form.data["sex"]
                dob = form.data["dob"]
                instance.dob = dt.strptime(dob, "%Y-%m-%d").date()
                instance.Phone = form.data["Phone"]
                instance.first_name = form.data["first_name"]
                instance.last_name = form.data["last_name"]
                instance.full_name = form.data["first_name"] + " " + form.data["last_name"]
                instance.save(update_fields=["full_name", "first_name", "last_name", "address", "dob", "sex", "Phone"])
                print("updated")
                return JsonResponse("EXAM UPDATED", safe=False)
    context = {"form": data, "title": "Echo Update Patient", "page_title": "ECHOGRAPHY"}
    return render(request, 'regi/main2/patient_update.html', context)


def patient_Create_Modal_x(request):
    '''
    This is to create Reg Patient From Xray
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
                saved_patient = Patient.objects.all().order_by('date_created').last()
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
    form = RegPatientForm()
    html_form = render_to_string('regi/main2/modal_regi_xpat_create.html', {'pat_form': form}, request=request)
    return JsonResponse({"html_form": html_form})
