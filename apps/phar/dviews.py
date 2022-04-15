import django
# from django.conf import settings
from django.http import JsonResponse
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


class PharHomeView(View):

    def get(self, request):
        context = {
            "title": 'Pharmacy',
            'page_title': 'PHARMACY',
            'subtitle': 'HOME PAGE',
            # "short_title": 'RH'
        }
        return render(request, 'phar/disp/disp_home.html', context)


# =================== Phar Patient =========================
@login_required
def patient_create(request):
    if request.method == 'POST':
        sn = request.POST['patient']
        form = PharPatientForm(request.POST)
        if form.is_valid():
            PharPatient.objects.create(
                patient=Patient.objects.get(sn=sn),
            )
            return JsonResponse('Patient Created', safe=False)
        else:
            return JsonResponse('Patient Not Created', safe=False)

    elif request.method == 'GET':
        form = PharPatientForm()
        patients = PharPatient.objects.all()
        context = {
            "form": form,
            "patients": patients,
            "title": "LAB",
            "page_title": "PHARMACY",
            "sub_title": "REGISTER NEW PATIENT"
        }
        return render(request, 'phar/main/phar_pat_create.html', context)


@login_required
def patient_list(request):
    patients = PharPatient.objects.all()
    presc = PharPrescription.objects.all()

    context = {"patients": patients, "presc": presc,
               "title": "PHAR",
               "page_title": "PHARMACY",
               "sub_title": "PHARMACY PATIENT LIST"}
    return render(request, 'phar/main/phar_pat_list.html', context)


@login_required
def patient_detail(request, slug):
    patient = PharPatient.objects.get(ln=slug)
    phar_presc = PharPrescription.objects.all().filter(patient=patient)

    if patient.exists():
        name = patient[0].patient.patient.first_name
        page_title = "Phar Pat " + name + " Detail"
        context = {"patient": patient_detail, "exams": phar_presc,
                   "title": "Phar Detail", "page_title": page_title}
        return render(request, 'phar/main/phar-patientDetail.html', context)

    else:
        le = {'count': '0', 'lab_tests': '0','fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": patient, "exams": phar_presc,
                   "title": "PHAR",
                   "page_title": "PHARMACY",
                   "sub_title": "PHARMACY PATIENT DETAIL"
                   }
        return render(request, 'phar/main/labo-patientDetail.html', context)


@login_required
def patient_update(request, slug):
    patient = PharPatient.objects.get(ln=slug)
    presc = PharPrescription.objects.all()
    phar_presc = PharPrescription.objects.all().filter(patient=patient)

    if patient.exists():
        context = {"patient": patient,
                   "phar_presc": phar_presc}
        return render(request, 'phar/main/labo-patientDetail.html', context)

    else:
        le = {'count': '0', 'lab_tests': '0','fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": patient,
                   "phar_presc": phar_presc}
        return render(request, 'phar/main/labo-patientDetail.html', context)


@login_required
def patient_delete(request, slug):
    patient = PharPatient.objects.get(ln=slug)
    phar_presc = PharPrescription.objects.all().filter(patient=patient)

    if patient.exists():
        context = {"patient": patient_detail,
                   "phar_presc": phar_presc}
        return render(request, 'phar/main/labo-patientDetail.html', context)

    else:
        print(False)
        le = {'count': '0', 'lab_tests': '0','fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": patient_detail,
                   "phar_presc": phar_presc,
                   }
        return render(request, 'phar/main/labo-patientDetail.html', context)


# ==================== Pharm Prescription =====================
@login_required(login_url="/login/")    # ok
def prescription_Create_Update(request, id=0):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            if id == 0:                     # Insert Operation
                form = PharPrescriptionForm()
            else:                           # Update Operation
                lt = PharPrescription.objects.get(id=id)
                form = PharPrescriptionForm(instance=lt)
            context = {
                "title": 'Register / Update Pharmacy Prescription',
                "page_title": "PHARMACY",
                "type_form": form
            }
            return render(request, 'phar/main/phar_presc_create.html', context)
        if request.method == 'POST':
            if id == 0:
                form = PharPrescriptionForm(request.POST)
            else:
                pt = PharPrescription.objects.get(id=id)
                form = PharPrescriptionForm(request.POST, instance=pt)
            if form.is_valid():
                form.save()
            return redirect('phar:prescriptionList')


@login_required(login_url="/login/")    # ok
def prescription_List(request):
    check = pharUserList(request)
    if check == True:
        context = {
            "title": 'Medical Pharmacy Prescription List',
            "page_title": "PHARMACY",
            "phar_type": PharPrescription.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'phar/main/phar_presc_list.html', context)


@login_required(login_url="/login/")    # ok
def prescription_Delete(request, id=0):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            if id == 0:
                return redirect('phar:prescriptionList')
            else:
                pt = PharPrescription.objects.get(id=id)
                pt.delete()
            return redirect('phar:prescriptionList')


# ==================== Pharm Prescription Item =====================
@login_required(login_url="/login/")    # ok
def prescription_item_Create_Update(request, id=0):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            if id == 0:                     # Insert Operation
                form = PharPrescriptionItemForm()
            else:                           # Update Operation
                lt = PharPrescriptionItem.objects.get(id=id)
                form = PharPrescriptionItemForm(instance=lt)
            context = {
                "title": 'Register / Update Pharmacy PrescriptionItem',
                "page_title": "PHARMACY",
                "type_form": form
            }
            return render(request, 'phar/main2/phar_prescriptionItem_form.html', context)
        if request.method == 'POST':
            if id == 0:
                form = PharPrescriptionItemForm(request.POST)
            else:
                pt = PharDrugType.objects.get(id=id)
                form = PharPrescriptionItemForm(request.POST, instance=pt)
            if form.is_valid():
                form.save()
            return redirect('phar:typeList')


@login_required(login_url="/login/")    # ok
def prescription_item_List(request):
    check = pharUserList(request)
    if check == True:
        context = {
            "title": 'Medical Pharmacy Type List',
            "page_title": "PHARMACY",
            "phar_type": PharPrescriptionItem.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'phar/main2/phar_category.html', context)


@login_required(login_url="/login/")    # ok
def prescription_item_Delete(request, id=0):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            if id == 0:
                return redirect('phar:typeList')
            else:
                pt = PharPrescriptionItem.objects.get(id=id)
                pt.delete()
            return redirect('phar:typeList')


# ==================== Pharm Drug Dispensed =====================
@login_required(login_url="/login/")    # ok
def drug_dispensed_Create_Update(request, id=0):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            if id == 0:                     # Insert Operation
                form = PharDrugDispensedForm()
            else:                           # Update Operation
                lt = PharDrugDispensed.objects.get(id=id)
                form = PharDrugDispensedForm(instance=lt)
            context = {
                "title": 'Register / Update Pharmacy Exam',
                "page_title": "PHARMACY",
                "type_form": form
            }
            return render(request, 'phar/main2/phar_type_form.html', context)
        if request.method == 'POST':
            if id == 0:
                form = PharDrugDispensedForm(request.POST)
            else:
                pt = PharDrugDispensed.objects.get(id=id)
                form = PharDrugDispensedForm(request.POST, instance=pt)
            if form.is_valid():
                form.save()
            return redirect('phar:typeList')


@login_required(login_url="/login/")    # ok
def drug_dispensed_List(request):
    check = pharUserList(request)
    if check == True:
        context = {
            "title": 'Medical Pharmacy DrugDispensed List',
            "page_title": "PHARMACY",
            "phar_type": PharDrugDispensed.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'phar/main2/phar_category.html', context)


@login_required(login_url="/login/")    # ok
def drug_dispensed_Delete(request, id=0):
    check = pharUserList(request)
    if check == True:
        if request.method == 'GET':
            if id == 0:
                return redirect('phar:typeList')
            else:
                pt = PharDrugDispensed.objects.get(id=id)
                pt.delete()
            return redirect('phar:drugDispensedList')
