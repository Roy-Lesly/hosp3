import datetime
import django
from django.http import request, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.template.loader import render_to_string

from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


def laboUserList(request):
    qs = LaboUser.objects.all()
    user = request.user
    i = 0
    for p in qs:
        if user.username == str(qs[i]):
            return True
        i += 1
    return False


@login_required(login_url="/login/")    # ok
def laboWelcomeView(request):
    check = laboUserList(request)
    if check == True:
        context = {
            "title": 'Medical Laboratory Department',
            "page_title": "LABORATORY",
        }
        if request.method == 'GET':
            return render(request, 'labo/labo_welcome.html', context)
        else:
            render(request, 'root/welcome.html')

    else:
        return render(request, 'root/welcome.html')


@login_required(login_url="/login/") # ok
def laboHomeView(request):
    check = laboUserList(request)
    patients = LaboPatient.objects.all()
    if check == True:
        context = {
            "title": 'LAB HOME',
            "page_title": "LABORATORY",
            "sub_title": "Home Page",
            "patients": patients,
        }
        return render(request, 'labo/main/labo_pat_list.html', context)
    else:
        return render(request, 'root/welcome.html')


# ==================== FBVs =====================================
# ========================== Labo Patient ==========================
@login_required
def patient_create(request):
    if request.method == 'POST':
        sn = request.POST['patient']
        form = LaboPatientForm(request.POST)
        if form.is_valid():
            LaboPatient.objects.create(
                patient=Patient.objects.get(sn=sn),
            )
            return JsonResponse('Patient Created', safe=False)
        else:
            return JsonResponse('Patient Not Created', safe=False)

    elif request.method == 'GET':
        form = LaboPatientForm()
        patients = LaboPatient.objects.all()
        context = {
            "form": form,
            "patients": patients,
            "title": "LAB",
            "page_title": "LABORATORY",
            "sub_title": "REGISTER NEW PATIENT"
        }
        return render(request, 'labo/main/labo_pat_create.html', context)


@login_required
def patient_list(request):
    patients = LaboPatient.objects.all()
    lexams = LaboExam.objects.all()
    lexams_patient = LaboExam.objects.all().filter(patient=patient_detail)

    context = {"patients": patients, "exams": lexams_patient,
               "title": "LAB",
               "page_title": "LABORATORY",
               "sub_title": "LABORATORY PATIENT LIST"}
    return render(request, 'labo/main/labo_pat_list.html', context)


@login_required
def patient_detail(request, slug):
    patient_detail = LaboPatient.objects.get(ln=slug)
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
    patient_detail = LaboPatient.objects.get(ln=slug)
    lexams = LaboExam.objects.all()
    lexams_patient = LaboExam.objects.all().filter(patient=patient_detail)

    if lexams_patient.exists():

        context = {"patient": patient_detail,
                   "exams": lexams_patient}
        return render(request, 'labo/main/labo-patientDetail.html', context)

    # elif not lexams_patient.exists():
    else:
        le = {'count': '0', 'lab_tests': '0','fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": patient_detail,
                   "exams": lexams_patient}
        return render(request, 'labo/main/labo-patientDetail.html', context)


@login_required
def patient_delete(request, slug):
    patient_detail = LaboPatient.objects.get(ln=slug)
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
        return render(request, 'labo/main/labo-patientDetail.html', context)

    # elif not lexams_patient.exists():
    else:
        print(False)
        le = {'count': '0', 'lab_tests': '0','fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": patient_detail,
                   "exams": lexams_patient,
                   }
        return render(request, 'labo/main/labo-patientDetail.html', context)


# --------------------- Labo Exam ---------------------------
@login_required
def exam_create(request):
    if request.method == 'POST':
        form = LaboExamForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse('EXAM CREATED', safe=False)
            except:
                return JsonResponse('EXAM ALREADY EXIST', safe=False)
        else:
            return JsonResponse('EXAM NOT CREATED', safe=False)
    else:
        form = LaboExamForm()
        cat = LaboTestCategory.objects.all()
        context = {"form": form, "title": 'LAB', "page_title": 'LABORATORY', "category": cat,
                   "sub_title": "REGISTER NEW EXAM"}

    return render(request, 'labo/main/labo_exam_create.html', context)


@login_required
def exam_list(request):
    exams = LaboExam.objects.all()

    context = {"exams": exams,
               "title": "LAB",
               "page_title": "LABORATORY",
               "sub_title": "LABORATORY EXAM LIST"
               }
    return render(request, 'labo/main/labo_exam_list.html', context)


@login_required
def exam_detail(request, slug):
    patient_detail = LaboPatient.objects.get(ln=slug)
    lexams = LaboExam.objects.all()
    lexams_patient = LaboExam.objects.all().filter(patient=patient_detail)

    if lexams_patient.exists():
        context = {"patient": patient_detail,
                   "exams": lexams_patient}
        return render(request, 'labo/main/labo-patientDetail.html', context)

    else:
        print(False)
        le = {'count': '0', 'lab_tests': '0','fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": patient_detail,
                   "exams": lexams_patient}
        return render(request, 'labo/main/labo-patientDetail.html', context)


# -------------------- Labo Test (Exam Item) -------------------------
@login_required
def new_test_in_new_exam(request):
    if request.method == 'POST':
        if True:
            try:
                a = LaboExamItem.objects.create(
                    lexam=LaboExam.objects.order_by('date_created').last(),
                    ltype=LaboTestType.objects.get(id=request.POST['ltype']),
                    paid=request.POST['paid']
                )
                a.save()
                return JsonResponse('EXAM ITEM CREATED', safe=False)
            except:
                return JsonResponse('EXAM ITEM ALREADY EXIST', safe=False)
        else:
            return JsonResponse('EXAM ITEM NOT CREATED', safe=False)


@login_required
def exam_item_create(request):
    if request.method == 'POST':
        if True:
            try:
                a = LaboExamItem.objects.create(
                    lexam=LaboExam.objects.get(book_num=request.POST['lexam']),
                    ltype=LaboTestType.objects.get(id=request.POST['ltype']),
                    paid=request.POST['paid']
                )
                a.save()
                return JsonResponse('EXAM ITEM CREATED', safe=False)
            except:
                return JsonResponse('EXAM ITEM ALREADY EXIST', safe=False)
        else:
            return JsonResponse('EXAM ITEM NOT CREATED', safe=False)
    else:
        category = LaboTestCategory.objects.all()
        context = {
            "category": category,
            "title": "LAB",
            "page_title": "LABORATORY",
            "sub_title": "REGISTER NEW LAB TEST"
        }
        return render(request, 'labo/main/labo_exam_item_create.html', context)
    return render(request, 'labo/main/labo_exam_item_create.html', context)


@login_required
def exam_item_update(request, id):
    test = LaboExamItem.objects.get(id=id)
    form = LaboExamItemForm(instance=test)
    if request.method == 'POST':
        form = LaboExamItemForm(request.POST, instance=test)
        if form.is_valid():
            if True:
                form.save()
            return redirect('labo:laboExamItemList')
    context = {"form": form, "result": test, "title": "Lab Update List", "page_title": "LABORATORY" }
    return render(request, 'labo/main/labo_exam_item_update.html', context)


# --------------------- Labo Result ---------------------------
@login_required
def result_Create(request):
    if request.method == 'POST':
        form = LaboFindingForm(request.POST)
        '''print(form.data)
        print("ltype " + request.POST['ltype'])
        print(LaboExam.objects.get(book_num=request.POST['lexam'])),
        print(LaboExamItem.objects.get(id=request.POST['ltype'])),
        print(LaboStaff.objects.get(id=request.POST['staff'])),
        print(request.POST['findings'])'''
        # print(form.data)
        if True:
            try:
                a = LaboFinding.objects.create(
                    lab_exam=LaboExam.objects.get(book_num=request.POST['lexam']),
                    lab_test=LaboExamItem.objects.get(id=request.POST['ltype']),
                    staff=LaboStaff.objects.get(id=request.POST['staff']),
                    findings=request.POST['findings']
                )
                a.save()
                return JsonResponse('RESULT CREATED', safe=False)
            except:
                return JsonResponse('RESULT ALREADY EXIST', safe=False)
        else:
            print('result form NOT valid')
            return JsonResponse('RESULT NOT CREATED', safe=False)
    else:
        form = LaboFindingForm()
        staff = LaboStaff.objects.all()
        context = {
            "form": form,
            "staff": staff,
            "title": "LAB",
            "page_title": "LABORATORY",
            "sub_title": "REGISTER NEW RESULT"
        }
        return render(request, 'labo/main/labo_result_create.html', context)
    return render(request, 'labo/main/labo_result_create.html', context)


@login_required
def result_List(request):
    result_items = LaboFinding.objects.all()
    form = LaboFindingForm()
    context = {"result_items": result_items,
               "form": form,
               "title": "LAB",
               "page_title": "LABORATORY",
               "sub_title": "LABORATORY RESULTS LIST"
               }
    return render(request, 'labo/main/labo_result_list.html', context)


@login_required
def result_Update(request, id):
    check = laboUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = LaboFinding.objects.get(id=id)
            form = LaboFindingForm(instance=rs)
            context = {
                "result_update": form,
                "result_id": rs.id
            }
            html_form = render_to_string('labo/main/labo_result_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            ls = LaboFinding.objects.get(id=id)
            form = LaboFindingForm(request.POST, instance=ls)
            print(form.errors)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)


@login_required
def result_Detail(request, id):
    result_detail = LaboFinding.objects.get(id=id)
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
        return render(request, 'labo/main/labo-patientDetail.html', context)

    # elif not lexams_patient.exists():
    else:
        print(False)
        le = {'count': '0', 'lab_tests': '0','fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": patient_detail,
                   "exams": lexams_patient}
        return render(request, 'labo/main/labo-patientDetail.html', context)


@login_required(login_url="/login/")  # ok
def result_Delete(request, id):
    check = laboUserList(request)
    if check == True:
        if request.method == 'GET':
            lf = LaboFinding.objects.get(id=id)
            context = {
                "result_delete": lf,
                "result_id": lf.id
            }
            html_form = render_to_string('labo/main/labo_result_delete.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            lf = LaboFinding.objects.get(id=id)
            if True:
                lf.delete()
                return JsonResponse({"data": "DELETED"}, safe=False)
            else:
                return JsonResponse({"data": "NOT DELETED"}, safe=False)


# ========================= Labo Staff ==========================
@login_required(login_url="/login/")  # ok
def staff_List(request):
    check = laboUserList(request)
    if check == True:
        context = {
            "title": 'Laboratory Staff List',
            "page_title": "LABORATORY",
            "labo_staff": LaboStaff.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'labo/main2/labo_staff.html', context)


@login_required(login_url="/login/")  # ok
def staff_Create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        full_name = request.POST['full_name']
        address = request.POST['address']
        sex = request.POST['sex']
        dob = request.POST['dob']
        age = request.POST['age']
        Phone = request.POST['Phone']
        title = request.POST['title']
        print('first_name: ' + first_name, 'last_name: ' + last_name, 'full_name: ' + full_name,
              'address: ' + address, 'sex: ' + sex, 'dob: ' + dob, 'age: ' + age,
              'Phone: ' + Phone, 'title: ' + title)

        form = LaboStaffForm(request.POST)
        print(form.data)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({"data": "SAVED"}, safe=False)
            except:
                return JsonResponse({"data": "EXIST ALREADY"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
    form = LaboStaffForm()
    context = {
        'staff_form': form
    }
    html_form = render_to_string('labo/main2/staff_create.html', context, request=request)
    return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def staff_Update(request, id):
    check = laboUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = LaboStaff.objects.get(id=id)
            form = LaboStaffForm(instance=rs)
            context = {
                "staff_update": form,
                "staff_id": rs.id
            }
            html_form = render_to_string('labo/main2/staff_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            ls = LaboStaff.objects.get(id=id)
            form = LaboStaffForm(request.POST, instance=ls)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)


@login_required(login_url="/login/")  # ok
def staff_Delete(request, id):
    check = laboUserList(request)
    if check == True:
        if request.method == 'GET':
            # Delete Operation
            rs = LaboStaff.objects.get(id=id)
            context = {
                "staff_delete": rs,
                "staff_id": rs.id
            }
            html_form = render_to_string('labo/main2/staff_delete.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rs = LaboStaff.objects.get(id=id)
            if True:
                rs.delete()
                return JsonResponse({"data": "DELETED"}, safe=False)
            else:
                return JsonResponse({"data": "NOT DELETED"}, safe=False)


# ========================== Labo Exam Category ==========================
@login_required(login_url="/login/")    # ok
def category_List(request):
    check = laboUserList(request)
    if check == True:
        context = {
            "title": 'Medical Test Category List',
            "page_title": "LABORATORY",
            "labo_category": LaboTestCategory.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'labo/main2/labo_category.html', context)


@login_required(login_url="/login/")  # ok
def category_Create(request):
    if request.method == 'POST':
        form = LaboTestCategoryForm(request.POST)
        print(form.data)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({"data": "SAVED"}, safe=False)
            except:
                return JsonResponse({"data": "ALREADY EXIST"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
    form = LaboTestCategoryForm()
    context = {
        'category_form': form
    }
    html_form = render_to_string('labo/main2/category_create.html', context, request=request)
    return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def category_Update(request, id):
    check = laboUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = LaboTestCategory.objects.get(id=id)
            form = LaboTestCategoryForm(instance=rs)
            context = {
                "category_update": form,
                "category_id": rs.id
            }
            html_form = render_to_string('labo/main2/category_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            ls = LaboTestCategory.objects.get(id=id)
            form = LaboTestCategoryForm(request.POST, instance=ls)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)


@login_required(login_url="/login/")  # ok
def category_Delete(request, id):
    check = laboUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = LaboTestCategory.objects.get(id=id)
            context = {
                "category_delete": rs,
                "category_id": rs.id
            }
            html_form = render_to_string('labo/main2/category_delete.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rs = LaboTestCategory.objects.get(id=id)
            if True:
                rs.delete()
                return JsonResponse({"data": "DELETED"}, safe=False)
            else:
                return JsonResponse({"data": "NOT DELETED"}, safe=False)


# ---------------------- Labo Exam Type ---------------------
@login_required(login_url="/login/")    # ok
def type_List(request):
    check = laboUserList(request)
    if check == True:
        context = {
            "title": 'Medical Laboratory Test List',
            "page_title": "LABORATORY",
            "labo_type": LaboTestType.objects.all()
        }
        if request.method == 'GET':
            return render(request, 'labo/main2/labo_type.html', context)


@login_required(login_url="/login/")  # ok
def type_Create(request):
    if request.method == 'POST':
        form = LaboTestTypeForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            return JsonResponse({"data": "SAVED"}, safe=False)
        else:
            return JsonResponse({"data": "NOT SAVED"}, safe=False)
    form = LaboTestTypeForm()
    context = {
        'type_form': form
    }
    html_form = render_to_string('labo/main2/type_create.html', context, request=request)
    return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def type_Update(request, id):
    check = laboUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = LaboTestType.objects.get(id=id)
            form = LaboTestTypeForm(instance=rs)
            context = {
                "type_update": form,
                "type_id": rs.id
            }
            html_form = render_to_string('labo/main2/type_update.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            ls = LaboTestType.objects.get(id=id)
            form = LaboTestTypeForm(request.POST, instance=ls)
            if form.is_valid():
                form.save()
                return JsonResponse({"data": "UPDATED"}, safe=False)


@login_required(login_url="/login/")  # ok
def type_Delete(request, id):
    check = laboUserList(request)
    if check == True:
        if request.method == 'GET':
            rs = LaboTestType.objects.get(id=id)
            context = {
                "type_delete": rs,
                "type_id": rs.id
            }
            html_form = render_to_string('labo/main2/type_delete.html', context, request=request)
            return JsonResponse({"html_form": html_form})
        if request.method == 'POST':
            rs = LaboTestType.objects.get(id=id)
            if True:
                rs.delete()
                return JsonResponse({"data": "DELETED"}, safe=False)
            else:
                return JsonResponse({"data": "NOT DELETED"}, safe=False)
