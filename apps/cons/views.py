from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from .models import *
from .forms import *


# Create your views here.
def consUserList(request):
    allUser = ConsUser.objects.all().order_by('username_id')
    userList = []
    for p in allUser:
        userList.append(str(p))
    user = request.user.username
    if user in userList:
        return True
    else:
        return False


@login_required
def cons_welcome(request):
    check = consUserList(request)
    if check == True:
        context = {
            "title": 'Consultation Department',
            "page_title": 'Welcome to "Consultation"'
        }
        return render(request, 'cons/cons_welcome.html', context)
    else:
        return render(request, 'root/welcome.html')


# ====================== CONS Staff ==========================
@login_required(login_url="/login/")  # ok
def staff_List(request):
    check = consUserList(request)
    if check == True:
        context = {
            "title": 'Consultation Staff List',
            "page_title": "CONSULTATION",
            "cons_staff": ConsStaff.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'cons/main2/cons_staff.html', context)


@login_required(login_url="/login/")  # ok
def staff_Create(request):
    if request.method == 'POST':
        form = ConsStaffForm(request.POST)
        print(form.data)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({"data": "SAVED"}, safe=False)
            except:
                return JsonResponse({"data": "EXIST ALREADY"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
    form = ConsStaffForm()
    context = {
        'staff_form': form
    }
    html_form = render_to_string('cons/main2/staff_create.html', context, request=request)
    return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def staff_Update(request, id):
    check = consUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = ConsStaff.objects.get(id=id)
            form = ConsStaffForm(instance=rs)
            context = {
                "staff_update": form,
                "staff_id": rs.id
            }
            html_form = render_to_string('cons/main2/staff_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            ls = ConsStaff.objects.get(id=id)
            form = ConsStaffForm(request.POST, instance=ls)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)


@login_required(login_url="/login/")  # ok
def staff_Delete(request, id):
    check = consUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = ConsStaff.objects.get(id=id)
            context = {"staff_delete": rs, "staff_id": rs.id}
            html_form = render_to_string('cons/main2/staff_delete.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rs = ConsStaff.objects.get(id=id)
            if True:
                rs.delete()
                return JsonResponse({"data": "DELETED"}, safe=False)
            else:
                return JsonResponse({"data": "NOT DELETED"}, safe=False)


# ========================== Cons Patient ==========================
@login_required
def patient_create(request):
    if request.method == 'POST':
        sn = request.POST['patient']
        form = ConsPatientForm(request.POST)
        if form.is_valid():
            ConsPatient.objects.create(
                patient=Patient.objects.get(sn=sn),
            )
            return JsonResponse('Patient Created', safe=False)
        else:
            print("not valid")
            return JsonResponse('Patient Not Created', safe=False)

    elif request.method == 'GET':
        form = ConsPatientForm()
        patients = ConsPatient.objects.all()
        context = {
            "form": form,
            "patients": patients,
            "title": "CONS",
            "page_title": "CONSULTATION",
            "sub_title": "REGISTER NEW PATIENT"
        }
        return render(request, 'cons/main/cons_pat_create.html', context)


@login_required
def patient_list(request):
    patients = ConsPatient.objects.all()

    context = {"patients": patients,
               "title": "CONS",
               "page_title": "CONSULTATION",
               "sub_title": "CONSULTATION PATIENT LIST"}
    return render(request, 'cons/main/cons_pat_list.html', context)


@login_required
def patient_detail(request, slug):
    patient_detail = LaboPatient.objects.get(ln=slug)
    lexams = LaboExam.objects.all()
    lexams_patient = LaboExam.objects.all().filter(patient=patient_detail)

    if lexams_patient.exists():
        name = lexams_patient[0].patient.patient.first_name
        page_title = "Lab Pat " + name + " Detail"
        context = {"patient": patient_detail, "exams": lexams_patient,
                   "title": "Lab Detail", "page_title": page_title}
        return render(request, 'labo/main/labo-patientDetail.html', context)

    else:
        le = {'count': '0', 'lab_tests': '0','fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": patient_detail, "exams": lexams_patient,
                   "title": "LAB",
                   "page_title": "LABORATORY",
                   "sub_title": "LABORATORY PATIENT DETAIL"
                   }
        return render(request, 'labo/main/labo-patientDetail.html', context)


@login_required
def patient_update(request, slug):
    patient_detail = ConsPatient.objects.get(ln=slug)
    lexams = LaboExam.objects.all()
    lexams_patient = LaboExam.objects.all().filter(patient=patient_detail)

    if lexams_patient.exists():

        context = {"patient": patient_detail,
                   "exams": lexams_patient}
        return render(request, 'cons/main/cons-patientDetail.html', context)

    else:
        le = {'count': '0', 'lab_tests': '0','fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": patient_detail,
                   "exams": lexams_patient}
        return render(request, 'cons/main/cons-patientDetail.html', context)


@login_required
def patient_delete(request, slug):
    patient_detail = ConsPatient.objects.get(ln=slug)
    lexams = LaboExam.objects.all()
    lexams_patient = LaboExam.objects.all().filter(patient=patient_detail)

    if lexams_patient.exists():
        print(lexams)
        print(lexams_patient)
        print(lexams_patient[0].patient.ln)
        print(lexams_patient[0].patient.patient)
        #print(lexams_patient[0].patient.labslug)
        print(lexams_patient[0].labo_type.all())
        print(lexams_patient[0].fees)
        print(lexams_patient[0].count)
        context = {"patient": patient_detail,
                   "exams": lexams_patient}
        return render(request, 'cons/main/cons-patientDetail.html', context)

    # elif not lexams_patient.exists():
    else:
        print(False)
        le = {'count': '0', 'lab_tests': '0','fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": patient_detail,
                   "exams": lexams_patient,
                   }
        return render(request, 'cons/main/cons-patientDetail.html', context)

