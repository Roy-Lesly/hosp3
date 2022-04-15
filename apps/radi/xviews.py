import datetime

import django
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


now = datetime.datetime.now()


def radUserList(request):
    qs = RadiUser.objects.all()
    user = request.user
    i = 0
    for p in qs:
        if user.username == str(qs[i]):
            return True
        i += 1
    return False


def radiUserList(request):
    qs = RadiUser.objects.all()
    user = request.user
    i = 0
    for p in qs:
        if user.username == str(qs[i]):
            return True
        i += 1
    return False


@login_required(login_url="/login/") # ok
def xrayHomeView(request):
    check = radiUserList(request)
    pats = XPatient.objects.all()
    if check == True:
        context = {
            'pats': pats,
            "title": 'XRAY HOME',
            "page_title": "XRAY",
            "sub_title": "Home Page",
        }
        return render(request, 'radi/xray/xray_pat_list.html', context)
    else:
        return render(request, 'root/welcome.html')


# --------------------- Xray Patient ---------------------------
@login_required(login_url="/login/")
def x_patient_create(request, un=0):
    if request.method == 'GET':
        form1 = XPatientForm()
        form2 = XExamForm()
        form3 = XExamItemForm()
        cat = RadiTestCategory.objects.filter(category_name__startswith='XRAY')
        context = {
            'category': cat,
            'form1': form1, 'form2': form2, 'form3': form3,
            "title": "XRAY",
            "page_title": "XRAY",
            "sub_title": "REGISTER NEW PATIENT"
        }
        return render(request, "radi/xray/xray_pat_create.html", context)
    else:
        form = XPatientForm(request.POST)
        print(form.data)
        print(form.errors)
        try:
            saved_u_patient = XPatient.objects.get(patient=request.POST['patient'])
            xn = saved_u_patient.xn
            sn = saved_u_patient.patient.sn
            book_num = saved_u_patient.patient.reg_num
            fn = saved_u_patient.patient.full_name
            phone = saved_u_patient.patient.Phone
            pat = [xn, sn, book_num, fn, phone]
            res = {'data': 'TRAPPED', 'patient': pat}
            print(pat)
            print('TRAPPED')
            return JsonResponse(res, safe=False)
        except:
            pass
        if form.is_valid():
            try:
                form.save()
                print("saved x pat")
                saved_x_patient = XPatient.objects.get(patient=request.POST['patient'])
                print(saved_x_patient)
                xn = saved_x_patient.xn
                sn = saved_x_patient.patient.sn
                bn = saved_x_patient.patient.reg_num
                fn = saved_x_patient.patient.full_name
                phone = saved_x_patient.patient.Phone
                pat = [xn, sn, bn, fn, phone]
                res = {'data': 'SAVED', 'patient': pat}
                print(res)
                print(pat)
                return JsonResponse(res, safe=False)
            except:
                res = {'data': 'EXIST ALREADY', 'patient': []}
                return JsonResponse(res, safe=False)
        return JsonResponse("NOT SAVED", safe=False)


@login_required(login_url="/login/")
def x_patient_detail(request, slug):
    xpat = UPatient.objects.get(un=slug)
    exam = UExam.objects.filter(patient=xpat)
    context = {
        'x_patient_detail': xpat,
        'x_patient_exam': exam,
        'title': 'Xray'
    }
    return render(request, "radi/xray/xray_pat_detail.html", context)


@login_required(login_url="/login/")
def x_patient_list(request):
    pats = XPatient.objects.all()
    context = {
        'pats': pats,
        'title': 'Xray',
        "title": "XRAY",
        "page_title": "XRAY",
        "sub_title": "XRAY PATIENT LIST"
    }
    return render(request, "radi/xray/xray_pat_list.html", context)


@login_required(login_url="/login/")
def x_patient_delete(request, un):
    now = datetime.datetime.today()
    xpat = XPatient.objects.get(un=un)
    xpat_date = xpat.date_created
    if now.day == xpat_date.day:
        if (now.hour - xpat_date.hour) < 6:
            xpat.delete()
    return redirect('/radi/xrayPatientList')


# ==================== Xray Exam =======================
@login_required
def x_exam_create(request):
    if request.method == 'POST':
        form = XExamForm(request.POST)
        print(form.data)
        print(request.POST['book_num'])
        print(form.errors)
        print('XR' + (request.POST['book_num'])[1:9])
        try:
            save_exam = XExam.objects.get(book_num='XR' + (request.POST['book_num'])[1:9])
            print('trapped')
            info = [save_exam.book_num, 'TRAPPED Exam']
            return JsonResponse({'data': 'SAVED', 'info': info}, safe=False)
        except:
            pass
        if form.is_valid():
            try:
                form.save()
                print('saved')
                save_exam = XExam.objects.get(book_num=request.POST['book_num'])
                print(save_exam.book_num)
                info = [save_exam.book_num, 'SAVED Exam']
                return JsonResponse({'data': 'SAVED', 'info': info}, safe=False)
            except:
                print("duplicate")
                save_exam = XExam.objects.all().order_by("date_created").last()
                info = [save_exam.book_num, 'Exam EXIST ALREADY']
                return JsonResponse({'data': 'EXIST ALREADY', 'info': info}, safe=False)
        else:
            info = ['', 'Exam NOT SAVED']
            return JsonResponse({'data': 'NOT SAVED', 'info': info}, safe=False)
        return JsonResponse({'data': 'Exam Form NOT VALID'}, safe=False)

    else:
        form = XExamForm()
        cat = RadiTestCategory.objects.all()
        context = {
            "form": form,
            "category": cat,
            "title": "XRAY",
            "page_title": "XRAY",
            "sub_title": "REGISTER NEW EXAM"
        }
        return render(request, 'radi/xray/xray_exam_create.html', context)


@login_required
def x_exam_list(request):
    exams = XExam.objects.all()

    context = {
        "exams": exams,
        "title": "XRAY",
        "page_title": "XRAY",
        "sub_title": "XRAY EXAM LIST"
    }
    return render(request, 'radi/xray/xray_exam_list.html', context)


@login_required
def x_exam_detail(request, slug):
    patient_detail = XPatient.objects.get(xn=slug)
    xexams = XExam.objects.all()
    xexams_patient = XExam.objects.all().filter(patient=patient_detail)

    if xexams_patient.exists():

        return render(request, 'radi/main/echo_pat_detail.html', context)

    # elif not lexams_patient.exists():
    else:
        print(False)
        le = {'count': '0', 'x_tests': '0','fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": patient_detail,
                   "exams": xexams_patient}
        return render(request, 'radi/xray/xray_pat_detail.html', context)


# ==================== Xray Exam Item =======================
@login_required
def x_exam_item_create(request):
    if request.method == 'POST':
        form = XExamItemForm(request.POST)
        print(form.data)
        print(form.errors)
        save = XExam.objects.filter(book_num=request.POST['xexam'])
        print(save)
        if save:
            try:
                save = XExamItem.objects.get(xtype_id=request.POST['xtype'])
                print(save)
                print('trapped')
                info = [save.book_num, 'TRAPPED Exam Item']
                return JsonResponse({'data': 'TRAPPED', 'info': info}, safe=True)
            except:
                if form.is_valid():
                    try:
                        form.save()
                        print('Saved Exam item')
                        save_exam = XExamItem.objects.filter(book_num=request.POST['book_num'])
                        info = [save_exam.book_num, 'SAVED Exam Item']
                        return JsonResponse({'data': 'SAVED', 'info': info}, safe=False)
                    except:
                        print('exist already')
                        return JsonResponse({'data': 'EXIST ALREADY'}, safe=False)
                else:
                    return JsonResponse({'data': 'EXIST ALREADY'}, safe=False)
    else:
        form = XExamItemForm()
        cat = RadiTestCategory.objects.all()
        print(cat)
        context = {
            "form": form,
            "category": cat,
            "title": "XRAY",
            "page_title": "XRAY",
            "sub_title": "REGISTER NEW XRAY TEST"
        }
        return render(request, 'radi/xray/xray_exam_item_create.html', context)


@login_required
def x_exam_item_list(request):
    exams = XExam.objects.all()

    context = {
        "exams": exams,
        "title": "XRAY",
        "page_title": "XRAY",
        "sub_title": "XRAY EXAM LIST"
    }
    return render(request, 'radi/xray/xray_exam_list.html', context)


# --------------------- Xray Result ---------------------------
@login_required
def x_result_create(request):
    if request.method == 'POST':
        form = XFindingForm(request.POST)
        print(form.data)
        print(form.errors)
        staff = request.POST["staff"]
        code = request.POST["code"]
        qt = RadiStaff.objects.get(id=staff)
        if qt.code == code:
            if True:
                print("valid form")
                try:
                    form.save()
                    print('saved')
                    return JsonResponse('SAVED', safe=False)
                except:
                    print('exist already')
                    return JsonResponse('EXIST ALREADY', safe=False)
            else:
                print('not saved')
                return JsonResponse('NOT SAVED', safe=False)
        else:
            return JsonResponse('WRONG CODE', safe=False)
    else:
        category = RadiTestCategory.objects.all()
        xtype = RadiTestType.objects.all()
        xexam = XExam.objects.all()
        staff = RadiStaff.objects.all()
        context = {
            "xrayTest": xtype,
            "bookNum": xexam,
            "category": category,
            "staff": staff,
            "title": "XRAY",
            "page_title": "XRAY",
            "sub_title": "REGISTER NEW PATIENT"
        }
        return render(request, 'radi/xray/xray_result_create.html', context)


@login_required
def x_result_list(request):
    result = XFinding.objects.all()

    context = {"result": result,
               "title": "XRAY",
               "page_title": "XRAY",
               "sub_title": "REGISTER XRAY RESULT"
               }
    return render(request, 'radi/xray/xray_result_list.html', context)


@login_required
def x_result_update(request, id):
    result = XFinding.objects.get(id=id)
    form = XFindingForm(instance=result)
    if request.method == 'POST':
        form = XFindingForm(request.POST, instance=result)
        if form.is_valid():
            if True:
                form.save()
                print("updated")
            return redirect('radi:xrayResultList')
    context = { "form": form, "result": result, "title": "Xray Update List", "page_title": "XRAY" }
    return render(request, 'radi/xray/xray_result_update.html', context)


@login_required
def x_result_detail(request, id):
    result_detail = XFinding.objects.get(id=id)
    exams = XExam.objects.all()
    exams_patient = XExam.objects.all().filter(patient=result_detail)

    if exams_patient.exists():
        print(exams)
        print(exams_patient)
        print(exams_patient[0].patient.ln)
        print(exams_patient[0].patient.patient)
        #print(exams_patient[0].patient.labslug)
        print(exams_patient[0].labo_type.all())
        print(exams_patient[0].fees)
        print(exams_patient[0].count)
        context = {"patient": result_detail,
                   "exams": exams_patient}
        return render(request, 'radi/main/labo-patientDetail.html', context)

    # elif not lexams_patient.exists():
    else:
        print(False)
        le = {'count': '0', 'lab_tests': '0','fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": result_detail,
                   "exams": exams_patient}
        return render(request, 'labo/main/labo-patientDetail.html', context)
