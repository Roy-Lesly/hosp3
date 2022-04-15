import datetime

import django
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .models import *
from .forms import *
from .forms_result import *

from docxtpl import DocxTemplate
from calendar import monthrange, monthcalendar

now = datetime.datetime.now()


def radiUserList(request):
    qs = RadiUser.objects.all()
    user = request.user
    i = 0
    for p in qs:
        if user.username == str(qs[i]):
            return True
        i += 1
    return False


@login_required(login_url="/login/")  # ok
def echoHomeView(request):
    check = radiUserList(request)
    pats = UPatient.objects.all()
    if check == True:
        context = {
            'pats': pats,
            "title": 'ECHO HOME',
            "page_title": "ECHOGRAPHY",
            "sub_title": "Home Page",
        }
        return render(request, 'radi/echo/echo_pat_create.html', context)
    else:
        return render(request, 'root/welcome.html')


# --------------------- Echo Patient ---------------------------
@login_required(login_url="/login/")
def u_patient_create(request, un=0):
    if request.method == 'GET':
        mon_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        months = {}
        for x in range(0, 12):
            g = monthrange(2022, x + 1)
            h = []
            for i in range(1, g[1] + 1):
                h.append(i)
            months[mon_name[x]] = [x + 1], [g[1]], h
        print(months)
        print("p create")
        form1 = UPatientForm()
        form2 = UExamForm()
        form3 = UExamItemForm()
        cat = RadiTestCategory.objects.filter(category_name__startswith='ECHO')
        print(cat)
        pts = UExam.objects.all().values_list('patient', flat=True)
        ex = UExamItem.objects.all().values_list('uexam', flat=True)
        upat = UPatient.objects.exclude(un__in=pts)
        uexam = UExam.objects.exclude(book_num__in=ex)
        form = UExamForm()
        cat = RadiTestCategory.objects.all()
        context = {
            "info1": "Patients With NO Exams", "cont1": upat.count(),
            "info2": "Exams With No Procedures", "cont2": uexam.count(),
            'category': cat,
            'form1': form1, 'form2': form2, 'form3': form3,
            "title": "ECHO",
            "page_title": "ECHOGRAPHY",
            "sub_title": "REGISTER NEW PATIENT"
        }
        return render(request, "radi/echo/echo_pat_create.html", context)
    else:
        form = UPatientForm(request.POST)
        print("u_pat_create_view =====================")
        print(form.data)
        print(form.errors)
        pat = Patient.objects.get(sn=request.POST['patient'])
        print("Pat =============")
        print(pat)
        try:
            print("try")
            upat = UPatient.objects.get(patient=pat)
            res = {'data': 'PAT and UPAT EXIST', 'patient': [upat.un, upat.patient.sn, upat.patient.reg_num[1:6]]}
            print(res)
            return JsonResponse(res, safe=False)
        except:
            print("p only")
        if form.is_valid():
            form.save()
            print("saved")
            saved_u_patient = UPatient.objects.get(patient__sn=request.POST['patient'])
            un = saved_u_patient.un
            sn = saved_u_patient.patient.sn
            book_num = saved_u_patient.patient.reg_num
            fn = saved_u_patient.patient.full_name
            if len(book_num) < 5:
                bn = str(book_num).zfill(5) + '_' + str(datetime.date.today().year)[2:4]
            elif len(book_num) == 5:
                bn = str(book_num) + '_' + str(datetime.date.today().year)[2:4]
            else:
                bn = book_num
            pat = [un, sn, bn, fn]
            res = {'data': 'SAVED', 'patient': pat}
            print(pat)
            return JsonResponse(res, safe=False)
        print("Not Try and Not Valid")
        res = {"data":"EXIST ALREADY"}
        return JsonResponse(res, safe=False)


@login_required(login_url="/login/")
def u_patient_detail(request, slug):
    upat = UPatient.objects.get(un=slug)
    exam = UExam.objects.filter(patient=upat)
    context = {
        'u_patient_detail': upat,
        'u_patient_exam': exam,
        'title': 'Ultrasound'
    }
    return render(request, "radi/echo/echo_pat_detail.html", context)


@login_required(login_url="/login/")
def u_patient_list(request):
    pats = UPatient.objects.all()
    context = {
        'pats': pats,
        'title': 'Ultrasound',
        "title": "ECHO",
        "page_title": "ECHOGRAPHY",
        "sub_title": "ECHOGRAPHY PATIENT LIST"
    }
    return render(request, "radi/echo/echo_pat_list.html", context)


@login_required(login_url="/login/")
def u_patient_delete(request, un):
    now = datetime.datetime.today()
    upat = UPatient.objects.get(un=un)
    upat_date = upat.date_created
    if now.day == upat_date.day:
        if (now.hour - upat_date.hour) < 6:
            upat.delete()
    return redirect('/radi/echoPatientList')


# ==================== Echo Exam =======================
@login_required
def u_exam_create(request):
    if request.method == 'POST':
        form = UExamForm(request.POST)
        print(form.data)
        print(form.errors)
        try:
            saved_uexam = UExam.objects.get(book_num=request.POST['book_num2'])
            bn = request.POST['book_num2']
            pat = [bn]
            res = {'data': 'DUPLICATE', 'patient': pat}
            print(pat)
            print("try")
            return JsonResponse(res, safe=False)
        except:
            pass
        if form.is_valid():
            try:
                obj = form.save(commit=False)
                obj.book_num = request.POST['book_num2']
                obj.save()
                print('uexam saved')
                info = [request.POST['book_num2']]
                return JsonResponse({'data': 'SAVED', 'info': info}, safe=False)
            except:
                print("exist already")
                save_exam = UExam.objects.get(book_num=request.POST['book_num2'])
                info = [request.POST['book_num2']]
                print(info)
                return JsonResponse({'data': 'ALREADY SAVED', 'info': info}, safe=False)

        print("FORM NOT VALID ===========================")
        return JsonResponse({'data': 'NOT VALID'}, safe=False)

    else:
        cat = RadiTestCategory.objects.all()
        pts = UExam.objects.all().values_list('patient', flat=True)
        ex = UExamItem.objects.all().values_list('uexam', flat=True)
        upat = UPatient.objects.exclude(un__in=pts)
        uexam = UExam.objects.exclude(book_num__in=ex)
        form = UExamForm()
        cat = RadiTestCategory.objects.all()
        context = {
            "info1": "Patients With NO Exams", "cont1": upat.count(),
            "info2": "Exams With No Procedures", "cont2": uexam.count(),
            "form": form,
            "category": cat,
            "title": "ECHO",
            "page_title": "ECHOGRAPHY",
            "sub_title": "REGISTER NEW EXAM"
        }
        return render(request, 'radi/echo/echo_exam_create.html', context)


@login_required
def u_exam_list(request):
    exams = UExam.objects.all()[::-1][:1000]
    '''examitems = UExamItem.objects.all()
    male_obs = examitems.filter(utype__type_name="OBSTETRIC 6").filter(
        uexam__patient__patient__sex="MALE") | examitems.filter(utype__type_name="OBSTETRIC 10").filter(
        uexam__patient__patient__sex="MALE")
    print("examitems.count()")
    print(examitems.count())
    print("======== Exam List ==========")
    print("male_obs")
    print(male_obs)
    print(male_obs.count())'''
    context = {
        "exams": exams,
        "title": "ECHO",
        "page_title": "ECHOGRAPHY",
        "sub_title": "ECHOGRAPHY EXAM LIST"
    }
    return render(request, 'radi/echo/echo_exam_list.html', context)


@login_required
def u_exam_update(request, slug):
    uexam = UExam.objects.get(book_num=slug)
    patient = uexam.patient
    patient_id = uexam.patient_id
    ward = uexam.ward
    ward2 = ["Medical Ward", "Surgical Ward", "Children's Ward", "Maternity", "OPD", "Other"]
    exam_id = uexam.book_num
    prescriber = uexam.prescriber
    data = {'uexam': uexam, 'exam_id': exam_id, "patient": patient,
            "patient_id": patient_id, 'prescriber': prescriber, 'ward': ward}
    if request.method == 'POST':
        form = UExamForm(request.POST, instance=uexam)
        print(form.data)
        print(form.data["book_num"])
        print(form.errors)
        if form.is_valid():
            if True:
                instance = form.save(commit=False)
                instance.book_num = form.data["book_num2"]
                instance.prescriber = form.data["prescriber"]
                instance.save(update_fields=["book_num", "prescriber"])
                print("updated")
                return JsonResponse("EXAM UPDATED", safe=False)
    context = {"ward": ward2, "form": data, "uexam": uexam, "title": "Echo Update List", "page_title": "ECHOGRAPHY"}
    return render(request, 'radi/echo/echo_exam_update.html', context)


@login_required
def u_exam_detail(request, slug):
    uexam = UExam.objects.get(book_num=slug)
    print("exam_detail")
    test = UExamItem.objects.filter(uexam=uexam)
    test1 = UExamItem.objects.filter(uexam__patient__un=uexam.patient.un)
    print(test1)
    print(test)
    test_dict = {}
    for x in test:
        test_dict[x.id] = x.utype.type_name
    for x in test1:
        test_dict[x.id] = x.utype.type_name, x.date_created
    print(test_dict)

    if uexam:
        context = {
            "test": test_dict,
            "sn": uexam.patient.patient.sn,
            "un": uexam.patient.un,
            "bn": uexam.book_num,
            "ward": uexam.ward,
            "address": uexam.patient.patient.address,
            "pat_name": uexam.patient.patient.full_name,
            "phone": uexam.patient.patient.Phone,
            "date_created": uexam.date_created,
            "date_updated": uexam.date_updated,
        }
        html_form = render_to_string('radi/noti/modal_echo_exam_detail.html', request=request)
        return JsonResponse({"html_form": html_form, "context": context})

    else:
        print(False)
        le = {'count': '0', 'lab_tests': '0', 'fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": result_detail,
                   "exams": exams_patient}
        return render(request, 'radi/main/echo_result_detail.html', context)


# ==================== Echo Exam Item =======================
@login_required
def u_exam_item_create(request):
    if request.method == 'POST':
        form = UExamItemForm(request.POST)
        print(form.data)
        print(form.errors)
        uexam = UExam.objects.filter(book_num=request.POST['uexam'])
        print(uexam)
        if uexam:
            try:
                s = UExamItem.objects.filter(utype_id=request.POST['utype'])
                t = s.get(uexam=uexam)
                print(s)
                print(t)
                print('TRAPPED')
                return JsonResponse({'data': 'TRAPPED'}, safe=True)
            except:
                if form.is_valid():
                    try:
                        print('Saved Exam item')
                        form.save()
                        return JsonResponse({'data': 'SAVED'}, safe=False)
                    except:
                        print('DUPLICATE')
                        return JsonResponse({'data': 'DUPLICATE'}, safe=False)
                else:
                    return JsonResponse({'data': 'EXIST ALREADY'}, safe=False)
    else:
        form = UExamItemForm()
        cat = RadiTestCategory.objects.all()
        pts = UExam.objects.all().values_list('patient', flat=True)
        ex = UExamItem.objects.all().values_list('uexam', flat=True)
        upat = UPatient.objects.exclude(un__in=pts)
        uexam = UExam.objects.exclude(book_num__in=ex)
        print(ex)
        print(upat)
        print(uexam)
        context = {
            "info1": "Patients With NO Exams", "cont1": upat.count(),
            "info2": "Exams With No Procedures", "cont2": uexam.count(),
            "info3": "Exams With No Procedures", "cont3": uexam.count(),
            "form": form,
            "category": cat,
            "title": "ECHO",
            "page_title": "ECHOGRAPHY",
            "sub_title": "REGISTER NEW ECHO TEST"
        }
        return render(request, 'radi/echo/echo_exam_item_create.html', context)


@login_required
def u_exam_item_list(request):          # View Last 1000 Exam Items
    examitem = UExamItem.objects.all()[::-1][:1000]
    context = {
        "examItem": examitem,
        "title": "ECHO",
        "page_title": "ECHOGRAPHY",
        "sub_title": "Last 1000 ECHOGRAPHY PROCEDURES"
    }
    return render(request, 'radi/echo/echo_exam_item_list.html', context)


@login_required
def u_exam_item_list_all(request):          # View Last 1000 Exam Items
    #examitem = UExamItem.objects.all()[::-1][:1000]
    examitem = UExamItem.objects.all()
    context = {
        "examItem": examitem,
        "title": "ECHO",
        "page_title": "ECHOGRAPHY",
        "sub_title": "Last 1000 ECHOGRAPHY PROCEDURES"
    }
    return render(request, 'radi/echo/echo_exam_item_list.html', context)


@login_required
def u_exam_item_update(request, id):
    uexamitem = UExamItem.objects.get(id=id)
    id = uexamitem.id
    uexam = uexamitem.uexam
    utype = uexamitem.utype
    paid = uexamitem.paid
    date_created = uexamitem.date_created

    cat = RadiTestCategory.objects.filter(department__name="Echo")
    tests = RadiTestType.objects.filter(category__department__name="Echo")
    cats = [cat_name for cat_name in cat]

    print(tests)
    print(cats)

    ward = ["Medical Ward", "Surgical Ward", "Children's Ward", "Maternity", "OPD", "Other"]
    data = {'id': id, "utype": utype, "uexam": uexam, 'paid': paid, "category": cats, 'date_created': date_created}
    if request.method == 'POST':
        form = UExamItemForm(request.POST, instance=uexamitem)
        print(form.data)
        print(form.errors)
        if form.is_valid():
            if True:
                form.save()
                print("updated")
                return JsonResponse("EXAM UPDATED", safe=False)
    context = {"form": data, "uexamitem": uexamitem, "category": cats, "title": "Procedure Update List", "page_title": "ECHOGRAPHY"}
    return render(request, 'radi/echo/echo_exam_item_update.html', context)


# --------------------- Echo Result ---------------------------
@login_required
def u_result_create(request):
    if request.method == 'POST':
        form = UFindingForm(request.POST)
        print(form.data)
        print(form.errors)

        staff = request.POST["staff"]
        code = request.POST["code"]
        qt = RadiStaff.objects.get(id=staff)
        # if qt.code == code:
        if True:
            if form.is_valid():
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
        cat = RadiTestCategory.objects.all()
        pts = UExam.objects.all().values_list('patient', flat=True)
        form = UExamForm()
        cat = RadiTestCategory.objects.all()
        category = RadiTestCategory.objects.all()
        utype = RadiTestType.objects.all()
        uexam2 = UExam.objects.all()
        staff = RadiStaff.objects.all()
        context = {
            "form": ObstetricForm(),
            "echoTest": utype,
            "bookNum": uexam2,
            "category": category,
            "staff": staff,
            "title": "ECHO",
            "page_title": "ECHOGRAPHY",
            "sub_title": "REGISTER NEW PATIENT"
        }
        return render(request, 'radi/echo/echo_result_create.html', context)


@login_required(login_url="/login/")  # ok
def result_create_confirm_u(request):
    if request.method == 'GET':
        context = {}
        html_form = render_to_string('radi/noti/echo_result_confirmation.html', context, request=request)
        return JsonResponse({"html_form": html_form})


@login_required(login_url="/login/")  # ok
def write_results(request):
    print(request.POST)
    id_finding = request.POST["utype"]
    form_type = request.POST["form_type"]
    book_num = request.POST["uexam"]
    exam = UExam.objects.get(book_num=book_num)
    context = {
        "sn": exam.patient.patient.sn,
        "un": exam.patient.un,
        "book_num": book_num,
        "full_name": exam.patient.patient.full_name,
        "dob": exam.patient.patient.dob,
        "age": int(((now.date() - exam.patient.patient.dob).days)/365),
        "address": exam.patient.patient.address,
        "sex": exam.patient.patient.sex,
        "phone": exam.patient.patient.Phone,
        "staff": RadiStaff.objects.get(id=request.POST["staff"]).full_name,
        "prescriber": exam.prescriber,
        "date_created": UFinding.objects.get(u_test=id_finding).date_created,
    }
    if request.method == "POST":
        if form_type == "OBSTETRIC":
            form = ObstetricForm(context)
            html_form = render_to_string('radi/result/result_obstetric.html', {"form": form}, request=request)
            return JsonResponse({"state": "SUCCESS", "html_form": html_form})
        elif form_type == "ABDOMINAL":
            form = AbdominalForm(context)
            html_form = render_to_string('radi/result/result_abdominal.html', {"form": form}, request=request)
            return JsonResponse({"state": "SUCCESS", "html_form": html_form})
        elif form_type == "F-PELVIC":
            form = FPelvicForm(context)
            html_form = render_to_string('radi/result/result_female_pelvic.html', {"form": form}, request=request)
            return JsonResponse({"state": "SUCCESS", "html_form": html_form})
        elif form_type == "M-PELVIC":
            form = MPelvicForm(context)
            html_form = render_to_string('radi/result/result_male_pelvic.html', {"form": form}, request=request)
            return JsonResponse({"state": "SUCCESS", "html_form": html_form})
        elif form_type == "SMALL-PARTS":
            form = SmallPartsForm(context)
            html_form = render_to_string('radi/result/result_small_parts.html', {"form": form}, request=request)
            return JsonResponse({"state": "SUCCESS", "html_form": html_form})
        elif form_type == "DOPPLER":
            form = DopplerForm(context)
            html_form = render_to_string('radi/result/result_doppler.html', {"form": form}, request=request)
            return JsonResponse({"state": "SUCCESS", "html_form": html_form})
        elif form_type == "CARDIAC":
            form = CardiacForm(context)
            html_form = render_to_string('radi/result/result_cardiac.html', {"form": form}, request=request)
            return JsonResponse({"state": "SUCCESS", "html_form": html_form})


@login_required
def u_result_list(request):
    result = UFinding.objects.all()[::1][:1000]

    context = {"result": result,
               "title": "ECHO",
               "page_title": "ECHOGRAPHY",
               "sub_title": "Last 1000 ULTRASOUND RESULT LIST"
               }
    return render(request, 'radi/echo/echo_result_list.html', context)


@login_required
def u_result_list_all(request):
    #result = UFinding.objects.all()[::1][:1000]
    result = UFinding.objects.all()

    context = {"result": result,
               "title": "ECHO",
               "page_title": "ECHOGRAPHY",
               "sub_title": "Last 1000 ULTRASOUND RESULT LIST"
               }
    return render(request, 'radi/echo/echo_result_list.html', context)


@login_required
def u_result_update(request, id):
    result = UFinding.objects.get(id=id)
    findings = result.findings
    findings_id = result.id
    staff = result.staff.full_name
    staff_id = result.staff.id
    u_test = result.u_test.utype
    u_test_id = result.u_test.id
    uexam = result.uexam.book_num
    uexam_id = result.uexam.book_num
    print(findings, staff, uexam, u_test)
    print(staff_id, uexam_id, u_test_id)
    data = {'findings': findings, 'findings_id': findings_id, 'staff': staff, 'uexam': uexam, 'u_test': u_test,
            'staff_id': staff_id, 'uexam': uexam, 'u_test_id': u_test_id}
    if request.method == 'POST':
        form = UFindingForm(request.POST, instance=result)
        print(form.data)
        print(form.errors)
        if form.is_valid():
            if True:
                form.save()
                print("updated")
                return JsonResponse("FINDING UPDATED", safe=False)
    context = {"form": data, "result": result, "title": "Echo Update List", "page_title": "ECHOGRAPHY"}
    return render(request, 'radi/echo/echo_result_update.html', context)


@login_required
def u_result_detail(request, id):
    ufinding = UFinding.objects.get(id=id)
    print("result_detail")


    if ufinding:
        context = {
            "sn": ufinding.uexam.patient.patient.sn,
            "un": ufinding.uexam.patient.un,
            "bn": ufinding.uexam_id,
            "test": ufinding.u_test.utype.type_name,
            "phone": ufinding.uexam.patient.patient.Phone,
            "pat_name": ufinding.uexam.patient.patient.full_name,
            "staff": ufinding.staff.full_name,
            "findings": ufinding.findings,
            "date_created": ufinding.date_created,
            "date_updated": ufinding.date_updated,
        }
        html_form = render_to_string('radi/noti/modal_echo_result_detail.html', request=request)
        return JsonResponse({"html_form": html_form, "context": context})

    else:
        print(False)
        le = {'count': '0', 'lab_tests': '0', 'fees': '0', 'ys': '0', 'date_created': 'None'}
        context = {"patient": result_detail,
                   "exams": exams_patient}
        return render(request, 'radi/main/echo_result_detail.html', context)


# ========================== RESULT FORMS ==================================
@login_required
def result_obstetric(request):
    if request.method == 'POST':
        form = ObstetricForm(request.POST)
        print(form.data)
        print(form.errors)
        # ==================== FILLING OBSTETRIC FORM =======================
        data = {
            "book_num": request.POST["book_num"],
            "full_name": request.POST["full_name"],
            "address": request.POST["address"],
            "sex": request.POST["sex"],
            "prescriber": request.POST["prescriber"],
            "staff": request.POST["staff"],
            "date_created": request.POST["date_created"],
        }
        try:
            pass
        except:
            pass
        print("==================== GENERATING OBS REPORT ======================")
        doc = DocxTemplate("word_templates/forms/obs.docx")
        context = data
        doc.render(context)
        doc.save("../Hosp3/word_templates/results/" + request.POST["book_num"] + request.POST["full_name"] + ".docx")
        print("==================== REPORT GENERATED ======================")
        return JsonResponse("GENERATED", safe=False)
        try:
            pass
        except:
            print("================== REPORT NOT GENERATED ====================")
            return JsonResponse("ERROR", safe=False)
    else:
        form = ObstetricForm()
        cat = RadiTestCategory.objects.all()
        pts = UExam.objects.all().values_list('patient', flat=True)
        ex = UExamItem.objects.all().values_list('uexam', flat=True)
        upat = UPatient.objects.exclude(un__in=pts)
        uexam = UExam.objects.exclude(book_num__in=ex)
        context = {
            "info1": "Patients With NO Exams", "cont1": upat.count(),
            "info2": "Exams With No Procedures", "cont2": uexam.count(),
            "info3": "Exams With No Procedures", "cont3": uexam.count(),
            "form": form,
            "category": cat,
            "title": "ECHO",
            "page_title": "ECHOGRAPHY",
            "sub_title": "REGISTER NEW ECHO TEST"
        }
        return render(request, 'radi/result/result_obstetric.html', context)


@login_required
def result_female_pelvis(request):
    if request.method == 'POST':
        form = FemalePelvisForm(request.POST)
        print(form.data)
        print(form.errors)
        uexam = UExam.objects.filter(book_num=request.POST['uexam'])
        print(uexam)
        if uexam:
            try:
                s = UExamItem.objects.filter(utype_id=request.POST['utype'])
                t = s.get(uexam=uexam)
                print(s)
                print(t)
                print('TRAPPED')
                return JsonResponse({'data': 'TRAPPED'}, safe=True)
            except:
                if form.is_valid():
                    try:
                        print('Saved Exam item')
                        form.save()
                        return JsonResponse({'data': 'SAVED'}, safe=False)
                    except:
                        print('DUPLICATE')
                        return JsonResponse({'data': 'DUPLICATE'}, safe=False)
                else:
                    return JsonResponse({'data': 'EXIST ALREADY'}, safe=False)
    else:
        form = FemalePelvisForm()
        cat = RadiTestCategory.objects.all()
        pts = UExam.objects.all().values_list('patient', flat=True)
        ex = UExamItem.objects.all().values_list('uexam', flat=True)
        upat = UPatient.objects.exclude(un__in=pts)
        uexam = UExam.objects.exclude(book_num__in=ex)
        context = {
            "info1": "Patients With NO Exams", "cont1": upat.count(),
            "info2": "Exams With No Procedures", "cont2": uexam.count(),
            "info3": "Exams With No Procedures", "cont3": uexam.count(),
            "form": form,
            "category": cat,
            "title": "ECHO",
            "page_title": "ECHOGRAPHY",
            "sub_title": "REGISTER NEW ECHO TEST"
        }
        return render(request, 'radi/result/result_female_pelvis.html', context)


@login_required(login_url="/login/")  # ok
def generate_report(request):
    if request.method == "POST":
        form_type = request.POST["form_type"]
        post = {}
        print(request.POST)
        for key in request.POST:
            post[key] = request.POST[key]
        print("1. ====================== POPPING =======================")
        post.pop("csrfmiddlewaretoken")
        post.pop("form_type")
        full_name = (post.pop("full_name")).center(46, ' ')
        age = (post.pop("age")).center(6, ' ')
        sex = (post.pop("sex")).center(14, ' ')
        address = (post.pop("address")).center(36, ' ')
        phone = (post.pop("phone")).center(30, ' ')
        presc = (post.pop("presc")).center(29, ' ')
        indic = (post.pop("indic")).center(90, ' ')

        if form_type == "OBSTETRIC":
            presen = (post.pop("presen")).center(71, ' ')
            lmp = (post.pop("lmp")).center(24, ' ')
            fhr = (post.pop("fhr")).center(11, ' ')
            fetmov = ((post.pop("fetmov1")).ljust(5, ' ') + (post.pop("fetmov2")).rjust(5, ' ')).center(80, ' ')
            afi1 = (post.pop("afi1")).center(23, ' ')
            afi2 = (post.pop("afi2")).center(54, ' ')
            afi3 = (post.pop("afi3")).center(23, ' ')
            appearance = (post.pop("appearance")).center(110, ' ')
            gs1 = (post.pop("gs1")).rjust(5, '_')
            crl1 = (post.pop("crl1")).rjust(5, '_')
            fl1 = (post.pop("fl1")).rjust(5, '_')
            gs2 = (post.pop("gs2")).rjust(5, '_')
            crl2 = (post.pop("crl2")).rjust(5, '_')
            fl2 = (post.pop("fl2")).rjust(5, '_')

            print("2. ==================== APPENDING OBS ======================")
            post["lmp"] = lmp
            post["presen"] = presen
            post["fhr"] = fhr
            post["fetmov"] = fetmov
            post["afi1"] = afi1
            post["afi2"] = afi2
            post["afi3"] = afi3
            post["appearance"] = appearance
            post["gs1"] = gs1
            post["crl1"] = crl1
            post["fl1"] = fl1
            post["gs2"] = gs2
            post["crl2"] = crl2
            post["fl2"] = fl2
            post["date"] = datetime.date.today().strftime("%d-%b-%Y")
        elif form_type == "ABDOMINAL":
            pass
        elif form_type == "F-PELVIC":
            pass
        elif form_type == "M-PELVIC":
            pass
        elif form_type == "SMALL-PARTS":
            pass
        elif form_type == "DOPPLER":
            pass
        elif form_type == "CARDIAC":
            pass

        print("3. ==================== APPENDING FORM ======================")
        post["full_name"] = full_name
        post["address"] = address
        post["indic"] = indic
        post["sex"] = sex
        post["age"] = age
        post["phone"] = phone
        post["presc"] = presc
        post["indic"] = indic

        if form_type == "OBSTETRIC":
            print("4. ==================== GENERATING OBST REPORT ======================")
            context = post
            doc = DocxTemplate("word_templates/forms/1obs.docx")
        elif form_type == "ABDOMINAL":
            print("4. ==================== GENERATING ABDO REPORT ======================")
            context = post
            doc = DocxTemplate("word_templates/forms2/2abd.docx")
        elif form_type == "F-PELVIC":
            print("4. ==================== GENERATING F-PEL REPORT ======================")
            context = post
            doc = DocxTemplate("word_templates/forms/3f_pelvic.docx")
        elif form_type == "M-PELVIC":
            print("4. ==================== GENERATING M-PEL REPORT ======================")
            context = post
            doc = DocxTemplate("word_templates/forms/4m_pelvic.docx")
        elif form_type == "SMALL-PART":
            print("4. ==================== GENERATING S/P REPORT ======================")
            context = post
            doc = DocxTemplate("word_templates/forms/5small_p.docx")
        elif form_type == "DOPPLER":
            print("4. ==================== GENERATING DOP REPORT ======================")
            context = post
            doc = DocxTemplate("word_templates/forms/6dop.docx")
        elif form_type == "CARDIAC":
            print("4. ==================== GENERATING DOP REPORT ======================")
            context = post
            doc = DocxTemplate("word_templates/forms/6card.docx")

        print("5. ==================== GENERATING REPORT======================")
        doc.render(context)
        doc.save("../Hosp3/word_templates/results/" + request.POST["book_num"] + request.POST["full_name"] + ".docx")
        doc.save("../Users/ULTRASOUND/Desktop/results/" + request.POST["book_num"]  + request.POST["full_name"] + ".docx")
        print("6. ==================== REPORT GENERATED ======================")


        return JsonResponse("GENERATED", safe=False)
    print("================== RESULTS NOT GENERATED ====================")
    return JsonResponse("ERROR", safe=False)
