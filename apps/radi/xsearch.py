import datetime
import json
from django.http import JsonResponse
from apps.radi.models import *
from apps.regi.models import Patient

now = datetime.datetime.now()
now_year = now.year
now_month = now.month
now_day = now.day
search_month = str(now_year) + "-" + str(now_month).zfill(2)
search_day = str(now_year) + "-" + str(now_month).zfill(2) + "-" + str(now_day).zfill(2)


def xray_pats_quarterly_monthly_this_year(request):                # OK
    if request.method == 'GET':
        data = []
        data1 = {}
        data2 = {}
        this_year_total = {}
        this_year_exams = XPatient.objects.all().filter(
            date_created__istartswith=now_year).count()
        yexam = XPatient.objects.all().filter(date_created__istartswith=now_year)
        m1 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "01").count()
        m2 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "02").count()
        m3 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "03").count()
        m4 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "04").count()
        m5 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "05").count()
        m6 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "06").count()
        m7 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "07").count()
        m8 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "08").count()
        m9 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "09").count()
        m10 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "10").count()
        m11 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "11").count()
        m12 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "12").count()

        jan_mar = m1 + m2 + m3
        apr_jun = m4 + m5 + m6
        jul_sep = m7 + m8 + m9
        oct_dec = m10 + m11 + m12

        # Quarterly
        if jan_mar:
            data1["jan_mar"] = jan_mar
        else:
            data1["jan_mar"] = 0
        if apr_jun:
            data1["apr_jun"] = apr_jun
        else:
            data1["apr_jun"] = 0
        if jul_sep:
            data1["jul_sep"] = jul_sep
        else:
            data1["jul_sep"] = 0
        if oct_dec:
            data1["oct_dec"] = oct_dec
        else:
            data1["oct_dec"] = 0

        # Monthly
        if m1:
            data2['jan'] = m1
        else:
            data2['jan'] = 0
        if m2:
            data2['feb'] = m2
        else:
            data2['feb'] = 0
        if m3:
            data2['mar'] = m3
        else:
            data2['mar'] = 0
        if m4:
            data2['apr'] = m4
        else:
            data2['apr'] =0
        if m5:
            data2['may'] = m5
        else:
            data2['may'] = 0
        if m6:
            data2['jun'] = m6
        else:
            data2['jun'] = 0
        if m7:
            data2['jul'] = m7
        else:
            data2['jul'] = 0
        if m8:
            data2['aug'] = m8
        else:
            data2['aug'] = 0
        if m9:
            data2['sep'] = m9
        else:
            data2['sep'] = 0
        if m10:
            data2['oct'] = m10
        else:
            data2['oct'] = 0
        if m11:
            data2['nov'] = m11
        else:
            data2['nov'] = 0
        if m12:
            data2['dec'] = m12
        else:
            data2['dec'] = 0

        this = str(now_year) + " " + "Total Patients"
        this_year_total[this] = this_year_exams
        data.append(this_year_total)
        data.append(data1)
        data.append(data2)

        if True:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse("None", safe=False)


def xray_exams_quarterly_monthly_this_year(request):                # OK
    if request.method == 'GET':
        data = []
        data1 = []
        data2 = []
        this_year_total = []
        this_year_exams = XExam.objects.all().filter(
            date_created__istartswith=now_year).count()
        this_year_total.append(this_year_exams)
        yexam = XExam.objects.all().filter(date_created__istartswith=now_year)
        m1 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "01").count()
        m2 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "02").count()
        m3 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "03").count()
        m4 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "04").count()
        m5 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "05").count()
        m6 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "06").count()
        m7 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "07").count()
        m8 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "08").count()
        m9 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "09").count()
        m10 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "10").count()
        m11 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "11").count()
        m12 = yexam.filter(date_created__istartswith=str(now_year) + "-" + "12").count()

        jan_mar = m1 + m2 + m3
        apr_jun = m4 + m5 + m6
        jul_sep = m7 + m8 + m9
        oct_dec = m10 + m11 + m12

        # Quarterly
        if jan_mar:
            data1.append(jan_mar)
        else:
            data1.append(0)
        if apr_jun:
            data1.append(apr_jun)
        else:
            data1.append(0)
        if jul_sep:
            data1.append(jul_sep)
        else:
            data1.append(0)
        if oct_dec:
            data1.append(oct_dec)
        else:
            data1.append(0)

        # Monthly
        if m1:
            data2.append(m1)
        else:
            data2.append(0)
        if m2:
            data2.append(m2)
        else:
            data2.append(0)
        if m3:
            data2.append(m3)
        else:
            data2.append(0)
        if m4:
            data2.append(m4)
        else:
            data2.append(0)
        if m5:
            data2.append(m5)
        else:
            data2.append(0)
        if m6:
            data2.append(m6)
        else:
            data2.append(0)
        if m7:
            data2.append(m7)
        else:
            data2.append(0)
        if m8:
            data2.append(m8)
        else:
            data2.append(0)
        if m9:
            data2.append(m9)
        else:
            data2.append(0)
        if m10:
            data2.append(m10)
        else:
            data2.append(0)
        if m11:
            data2.append(m11)
        else:
            data2.append(0)
        if m12:
            data2.append(m12)
        else:
            data2.append(0)

        data.append(this_year_total)
        data.append(data1)
        data.append(data2)


        '''print(data[1])
        print(data[1][0])
        print(data[1][1])
        print(data[1][2])
        print("=============")
        print(data[2])
        print(data[2][0])
        print(data[2][1])
        print(data[2][2])'''

        if True:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse("None", safe=False)


def xray_pats_quarterly_monthly_last_year(request):                # OK
    if request.method == 'GET':
        data = []
        data1 = {}
        data2 = {}
        last_year_total = {}
        last_year_exams = XPatient.objects.all().filter(
            date_created__istartswith=now_year - 1).count()
        yexam = XPatient.objects.all().filter(date_created__istartswith=now_year - 1)
        m1 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "01").count()
        m2 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "02").count()
        m3 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "03").count()
        m4 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "04").count()
        m5 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "05").count()
        m6 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "06").count()
        m7 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "07").count()
        m8 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "08").count()
        m9 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "09").count()
        m10 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "10").count()
        m11 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "11").count()
        m12 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "12").count()

        jan_mar = m1 + m2 + m3
        apr_jun = m4 + m5 + m6
        jul_sep = m7 + m8 + m9
        oct_dec = m10 + m11 + m12

        # Quarterly
        if jan_mar:
            data1["jan_mar"] = jan_mar
        else:
            data1["jan_mar"] = 0
        if apr_jun:
            data1["apr_jun"] = apr_jun
        else:
            data1["apr_jun"] = 0
        if jul_sep:
            data1["jul_sep"] = jul_sep
        else:
            data1["jul_sep"] = 0
        if oct_dec:
            data1["oct_dec"] = oct_dec
        else:
            data1["oct_dec"] = 0

        # Monthly
        if m1:
            data2['jan'] = m1
        else:
            data2['jan'] = 0
        if m2:
            data2['feb'] = m2
        else:
            data2['feb'] = 0
        if m3:
            data2['mar'] = m3
        else:
            data2['mar'] = 0
        if m4:
            data2['apr'] = m4
        else:
            data2['apr'] =0
        if m5:
            data2['may'] = m5
        else:
            data2['may'] = 0
        if m6:
            data2['jun'] = m6
        else:
            data2['jun'] = 0
        if m7:
            data2['jul'] = m7
        else:
            data2['jul'] = 0
        if m8:
            data2['aug'] = m8
        else:
            data2['aug'] = 0
        if m9:
            data2['sep'] = m9
        else:
            data2['sep'] = 0
        if m10:
            data2['oct'] = m10
        else:
            data2['oct'] = 0
        if m11:
            data2['nov'] = m11
        else:
            data2['nov'] = 0
        if m12:
            data2['dec'] = m12
        else:
            data2['dec'] = 0

        last = str(now_year - 1) + " " + "Total Patients"
        last_year_total[last] = last_year_exams
        data.append(last_year_total)
        data.append(data1)
        data.append(data2)

        if True:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse("None", safe=False)


def xray_pats_quarterly_monthly_last_year_bk(request):                # OK
    if request.method == 'GET':
        data = []
        data1 = []
        data2 = []
        this_year_total = []
        this_year_exams = XPatient.objects.all().filter(
            date_created__istartswith=now_year - 1).count()
        this_year_total.append(this_year_exams)
        yexam = XPatient.objects.all().filter(date_created__istartswith=now_year - 1)
        m1 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "01").count()
        m2 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "02").count()
        m3 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "03").count()
        m4 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "04").count()
        m5 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "05").count()
        m6 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "06").count()
        m7 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "07").count()
        m8 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "08").count()
        m9 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "09").count()
        m10 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "10").count()
        m11 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "11").count()
        m12 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "12").count()

        jan_mar = m1 + m2 + m3
        apr_jun = m4 + m5 + m6
        jul_sep = m7 + m8 + m9
        oct_dec = m10 + m11 + m12

        # Quarterly
        if jan_mar:
            data1.append(jan_mar)
        else:
            data1.append(0)
        if apr_jun:
            data1.append(apr_jun)
        else:
            data1.append(0)
        if jul_sep:
            data1.append(jul_sep)
        else:
            data1.append(0)
        if oct_dec:
            data1.append(oct_dec)
        else:
            data1.append(0)

        # Monthly
        if m1:
            data2.append(m1)
        else:
            data2.append(0)
        if m2:
            data2.append(m2)
        else:
            data2.append(0)
        if m3:
            data2.append(m3)
        else:
            data2.append(0)
        if m4:
            data2.append(m4)
        else:
            data2.append(0)
        if m5:
            data2.append(m5)
        else:
            data2.append(0)
        if m6:
            data2.append(m6)
        else:
            data2.append(0)
        if m7:
            data2.append(m7)
        else:
            data2.append(0)
        if m8:
            data2.append(m8)
        else:
            data2.append(0)
        if m9:
            data2.append(m9)
        else:
            data2.append(0)
        if m10:
            data2.append(m10)
        else:
            data2.append(0)
        if m11:
            data2.append(m11)
        else:
            data2.append(0)
        if m12:
            data2.append(m12)
        else:
            data2.append(0)

        data.append(this_year_total)
        data.append(data1)
        data.append(data2)

        if True:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse("None", safe=False)


def xray_exams_quarterly_monthly_last_year(request):                # OK
    if request.method == 'GET':
        data = []
        data1 = []
        data2 = []
        this_year_total = []
        this_year_exams = XExam.objects.all().filter(
            date_created__istartswith=now_year - 1).count()
        this_year_total.append(this_year_exams)
        yexam = XExam.objects.all().filter(date_created__istartswith=now_year - 1)
        m1 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "01").count()
        m2 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "02").count()
        m3 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "03").count()
        m4 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "04").count()
        m5 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "05").count()
        m6 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "06").count()
        m7 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "07").count()
        m8 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "08").count()
        m9 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "09").count()
        m10 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "10").count()
        m11 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "11").count()
        m12 = yexam.filter(date_created__istartswith=str(now_year - 1) + "-" + "12").count()

        jan_mar = m1 + m2 + m3
        apr_jun = m4 + m5 + m6
        jul_sep = m7 + m8 + m9
        oct_dec = m10 + m11 + m12

        # Quarterly
        if jan_mar:
            data1.append(jan_mar)
        else:
            data1.append(0)
        if apr_jun:
            data1.append(apr_jun)
        else:
            data1.append(0)
        if jul_sep:
            data1.append(jul_sep)
        else:
            data1.append(0)
        if oct_dec:
            data1.append(oct_dec)
        else:
            data1.append(0)

        # Monthly
        if m1:
            data2.append(m1)
        else:
            data2.append(0)
        if m2:
            data2.append(m2)
        else:
            data2.append(0)
        if m3:
            data2.append(m3)
        else:
            data2.append(0)
        if m4:
            data2.append(m4)
        else:
            data2.append(0)
        if m5:
            data2.append(m5)
        else:
            data2.append(0)
        if m6:
            data2.append(m6)
        else:
            data2.append(0)
        if m7:
            data2.append(m7)
        else:
            data2.append(0)
        if m8:
            data2.append(m8)
        else:
            data2.append(0)
        if m9:
            data2.append(m9)
        else:
            data2.append(0)
        if m10:
            data2.append(m10)
        else:
            data2.append(0)
        if m11:
            data2.append(m11)
        else:
            data2.append(0)
        if m12:
            data2.append(m12)
        else:
            data2.append(0)

        data.append(this_year_total)
        data.append(data1)
        data.append(data2)

        if True:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse("None", safe=False)


def search_patient(request):                        # OK
    if request.method == 'POST':
        qt = json.loads(request.body).get('queryType')
        search_str = json.loads(request.body).get('searchText')
        if qt == "sn":
            patient = Patient.objects.all().filter(sn__istartswith=search_str)
            if patient:
                datlist = list(patient.values())
                return JsonResponse([datlist], safe=False)
            else:
                return JsonResponse("", safe=False)

        if qt == "Phone":
            patient = Patient.objects.all().filter(Phone__istartswith=search_str)          # return list of qs
            if patient:
                datlist = list(patient.values())
                print(datlist)
                return JsonResponse([datlist], safe=False)
            else:
                return JsonResponse("", safe=False)


def search_xray_patient(request):
    if request.method == 'POST':
        qt = json.loads(request.body).get('queryType')
        search_str = json.loads(request.body).get('searchText')

        if qt == "xn":
            patient = XPatient.objects.all().filter(book_num__istartswith=search_str)
            print(patient)
            if patient:
                dataValues = patient.values()
                datlist = list(dataValues)
                p = 0
                for x in patient:
                    sn = x.patient.sn
                    full_n = x.patient.full_name
                    first_n = x.patient.first_name
                    last_n = x.patient.last_name
                    sex = x.patient.sex
                    age = x.patient.age
                    address = x.patient.address
                    ph = x.patient.Phone
                    date_created = x.patient.date_created.date()

                    datlist[p]["sn"] = sn
                    datlist[p]["full_name"] = full_n
                    datlist[p]["first_name"] = first_n
                    datlist[p]["last_name"] = last_n
                    datlist[p]["address"] = address
                    datlist[p]["age"] = age
                    datlist[p]["sex"] = sex
                    datlist[p]["Phone"] = ph
                    datlist[p]["date_created"] = date_created
                    p += 1
                return JsonResponse([datlist], safe=False)
            else:
                return JsonResponse("", safe=False)

        if qt == "Phone":
            patient = XPatient.objects.all().filter(patient_id__Phone__istartswith=search_str)
            if patient:
                dataValues = patient.values()
                datlist = list(dataValues)
                p = 0
                for x in patient:
                    sn = x.patient.sn
                    full_n = x.patient.full_name
                    first_n = x.patient.first_name
                    last_n = x.patient.last_name
                    sex = x.patient.sex
                    age = x.patient.age
                    address = x.patient.address
                    ph = x.patient.Phone
                    date_created = x.patient.date_created.date()

                    datlist[p]["sn"] = sn
                    datlist[p]["full_name"] = full_n
                    datlist[p]["first_name"] = first_n
                    datlist[p]["last_name"] = last_n
                    datlist[p]["address"] = address
                    datlist[p]["age"] = age
                    datlist[p]["sex"] = sex
                    datlist[p]["Phone"] = ph
                    datlist[p]["date_created"] = date_created
                    p += 1
                return JsonResponse([datlist], safe=False)
            else:
                return JsonResponse("", safe=False)


def search_xray_exam(request):
    if request.method == 'POST':
        qt = json.loads(request.body).get('queryType')
        search_str = json.loads(request.body).get('searchText')
        print(qt + "  " + search_str)

        if qt == "book_num":
            patient = XExam.objects.all().filter(book_num__istartswith=search_str)
            print(patient)
            if patient:
                dataValues = patient.values()
                datlist = list(dataValues)
                p = 0
                for x in patient:
                    un = x.patient.un
                    bn = x.book_num
                    full_n = x.patient.patient.full_name
                    sex = x.patient.patient.sex
                    age = x.patient.patient.age
                    address = x.patient.patient.address
                    ph = x.patient.patient.Phone
                    date_created = x.patient.patient.date_created.date()

                    datlist[p]["un"] = un
                    datlist[p]["book_num"] = bn
                    datlist[p]["full_name"] = full_n
                    datlist[p]["address"] = address
                    datlist[p]["age"] = age
                    datlist[p]["sex"] = sex
                    datlist[p]["Phone"] = ph
                    datlist[p]["date_created"] = date_created
                    p += 1
                print(datlist)
                return JsonResponse([datlist], safe=False)
            else:
                return JsonResponse("", safe=False)

        if qt == "Phone":
            patient = XPatient.objects.all().filter(patient_id__Phone__istartswith=search_str)
            if patient:
                dataValues = patient.values()
                datlist = list(dataValues)
                p = 0
                for x in patient:
                    sn = x.patient.sn
                    un = x.patient.un
                    full_n = x.patient.full_name
                    first_n = x.patient.first_name
                    last_n = x.patient.last_name
                    sex = x.patient.sex
                    age = x.patient.age
                    address = x.patient.address
                    ph = x.patient.Phone
                    date_created = x.date_created.date()

                    datlist[p]["sn"] = sn
                    datlist[p]["un"] = un
                    datlist[p]["full_name"] = full_n
                    datlist[p]["first_name"] = first_n
                    datlist[p]["last_name"] = last_n
                    datlist[p]["address"] = address
                    datlist[p]["age"] = age
                    datlist[p]["sex"] = sex
                    datlist[p]["Phone"] = ph
                    datlist[p]["date_created"] = date_created
                    p += 1
                return JsonResponse([datlist], safe=False)
            else:
                return JsonResponse("", safe=False)


def search_xray_test(request):
    if request.method == 'POST':
        try:
            print("search by cat-echo")
            print(request.POST)
            qt = RadiTestType.objects.filter(category__category_name=request.POST["category"])
            print(qt)
            if qt:
                qtList = list(qt.values())
                return JsonResponse([qtList], safe=False)
            else:
                return JsonResponse("", safe=False)
        except:
            pass
        try:
            print("search by book_num")
            print(request.POST["book_num"])
            exam = XExam.objects.get(book_num=request.POST["book_num"])
            print(exam)
            tests = XExamItem.objects.filter(xexam=exam)

            print(tests)
            if tests:
                tests_list = list(tests.values())
                print(tests_list)
                print(tests_list[0])
                print(tests_list[1])
                n = 0
                for x in tests:
                    tests_list[n]['utype'] = x.xtype.type_name
                    print(x.utype)
                    n += 1
                print(tests_list[0])
                print(tests_list[1])

                return JsonResponse([tests_list, 'VALID'], safe=False)
            else:
                return JsonResponse(["", "NON VALID"], safe=False)
        except:
            pass


def search_radi_test(request):
    if request.method == 'POST':
        cat = request.POST["category"]

        qt = RadiTestType.objects.filter(category=cat)
        if qt:
            qtVal = qt.values()
            qtList = list(qtVal)
            return JsonResponse([qtList], safe=False)
        else:
            return JsonResponse("", safe=False)


# ==================== Tests ==============================
def xray_pats_chart_1_this_year(request):  # OK
    if request.method == 'GET':
        data = []
        this = {}
        last = {}
        try:
            all_lp = XPatient.objects.all().count()
        except:
            all_lp = 0
        try:
            all_lp_this_year = XPatient.objects.filter(date_created__istartswith=str(now_year)).count()
        except:
            all_lp_this_year = 0
        try:
            all_lp_last_year = XPatient.objects.filter(date_created__istartswith=str(now_year - 1)).count()
        except:
            all_lp_last_year = 0

        lp_this = XPatient.objects.all().filter(date_created__istartswith=now_year)
        total_this = XPatient.objects.all().filter(date_created__istartswith=now_year).count()
        m1 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "01").count()
        m2 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "02").count()
        m3 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "03").count()
        m4 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "04").count()
        m5 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "05").count()
        m6 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "06").count()
        m7 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "07").count()
        m8 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "08").count()
        m9 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "09").count()
        m10 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "10").count()
        m11 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "11").count()
        m12 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "12").count()

        qtly = {}
        # Quarterly
        jan_mar = m1 + m2 + m3
        apr_jun = m4 + m5 + m6
        jul_sep = m7 + m8 + m9
        oct_dec = m10 + m11 + m12

        if jan_mar:
            qtly['jan_mar'] = jan_mar
        else:
            qtly['jan_mar'] = 0
        if apr_jun:
            qtly['apr_jun'] = apr_jun
        else:
            qtly['apr_jun'] = 0
        if jul_sep:
            qtly['jul_sep'] = jul_sep
        else:
            qtly['jul_sep'] = 0
        if oct_dec:
            qtly['oct_dec'] = oct_dec
        else:
            qtly['oct_dec'] = 0

        mthly = {}
        # Monthly
        if m1:
            mthly['jan'] = m1
        else:
            mthly['jan'] = '-'
        if m2:
            mthly['feb'] = m2
        else:
            mthly['feb'] = '-'
        if m3:
            mthly['mar'] = m3
        else:
            mthly['mar'] = '-'
        if m4:
            mthly['apr'] = m4
        else:
            mthly['apr'] = '-'
        if m5:
            mthly['may'] = m5
        else:
            mthly['may'] = '-'
        if m6:
            mthly['jun'] = m6
        else:
            mthly['jun'] = '-'
        if m7:
            mthly['jul'] = m7
        else:
            mthly['jul'] = '-'
        if m8:
            mthly['aug'] = m8
        else:
            mthly['aug'] = '-'
        if m9:
            mthly['sep'] = m9
        else:
            mthly['sep'] = '-'
        if m10:
            mthly['oct'] = m10
        else:
            mthly['oct'] = '-'
        if m11:
            mthly['nov'] = m11
        else:
            mthly['nov'] = '-'
        if m12:
            mthly['dec'] = m12
        else:
            mthly['dec'] = '-'

        this_s = str(now_year) + "_" + "Total_Patients"
        last_s = str(now_year - 1) + "_" + "Total_Patients"

        this[this_s] = all_lp_this_year
        this["quarterly"] = qtly
        this["monthly"] = mthly
        last[last_s] = all_lp_last_year

        data.append(this)
        data.append(last)
        print(data)
        return JsonResponse(data, safe=False)


def xray_exams_chart_1_this_year(request):  # OK
    if request.method == 'GET':
        data = []
        this = {}
        last = {}
        try:
            all_lp = XExam.objects.all().count()
        except:
            all_lp = 0
        try:
            all_lp_this_year = XExam.objects.filter(date_created__istartswith=str(now_year)).count()
        except:
            all_lp_this_year = 0

        lp_this = XExam.objects.all().filter(date_created__istartswith=now_year)
        m1 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "01").count()
        m2 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "02").count()
        m3 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "03").count()
        m4 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "04").count()
        m5 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "05").count()
        m6 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "06").count()
        m7 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "07").count()
        m8 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "08").count()
        m9 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "09").count()
        m10 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "10").count()
        m11 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "11").count()
        m12 = lp_this.filter(date_created__istartswith=str(now_year) + "-" + "12").count()

        qtly = {}
        # Quarterly
        jan_mar = m1 + m2 + m3
        apr_jun = m4 + m5 + m6
        jul_sep = m7 + m8 + m9
        oct_dec = m10 + m11 + m12

        if jan_mar:
            qtly['jan_mar'] = jan_mar
        else:
            qtly['jan_mar'] = '-'
        if apr_jun:
            qtly['apr_jun'] = apr_jun
        else:
            qtly['apr_jun'] = 0
        if jul_sep:
            qtly['jul_sep'] = jul_sep
        else:
            qtly['jul_sep'] = 0
        if oct_dec:
            qtly['oct_dec'] = oct_dec
        else:
            qtly['oct_dec'] = 0

        mthly = {}
        # Monthly
        if m1:
            mthly['jan'] = m1
        else:
            mthly['jan'] = '-'
        if m2:
            mthly['feb'] = m2
        else:
            mthly['feb'] = '-'
        if m3:
            mthly['mar'] = m3
        else:
            mthly['mar'] = '-'
        if m4:
            mthly['apr'] = m4
        else:
            mthly['apr'] = '-'
        if m5:
            mthly['may'] = m5
        else:
            mthly['may'] = '-'
        if m6:
            mthly['jun'] = m6
        else:
            mthly['jun'] = '-'
        if m7:
            mthly['jul'] = m7
        else:
            mthly['jul'] = '-'
        if m8:
            mthly['aug'] = m8
        else:
            mthly['aug'] = '-'
        if m9:
            mthly['sep'] = m9
        else:
            mthly['sep'] = '-'
        if m10:
            mthly['oct'] = m10
        else:
            mthly['oct'] = '-'
        if m11:
            mthly['nov'] = m11
        else:
            mthly['nov'] = '-'
        if m12:
            mthly['dec'] = m12
        else:
            mthly['dec'] = '-'

        this_s = str(now_year) + "_" + "Total_Exam"

        this[this_s] = all_lp_this_year
        this["quarterly"] = qtly
        this["monthly"] = mthly

        data.append(this)
        print(data)
        return JsonResponse(data, safe=False)


def xray_tests_stats_1_this_year(request):  # OK
    if request.method == 'GET':
        xray_test = []
        cat = RadiTestCategory.objects.all()
        type = RadiTestType.objects.all()
        type_u1 = type.filter(category=cat[2])
        type_u2 = type.filter(category=cat[3])
        xray_test.append(type_u1)
        xray_test.append(type_u2)

        type_list = []  # changes from name to query set in the try block
        name_list = []  # remains name e.g "HB", "CBC"
        for x in xray_test[0]:
            type_list.append(x.type_name)
            name_list.append(x.type_name)
        for y in xray_test[1]:
            type_list.append(y.type_name)
            name_list.append(y.type_name)

        try:
            all_test_this_year = XExamItem.objects.filter(date_created__istartswith=str(now_year))
            data_counts = {}
            tests_counts_year = {}
            tests_counts_qtly = {}
            tests_counts_month = {}

            for y in range(0, len(name_list)):
                type_list[y] = all_test_this_year.filter(xtype__type_name=name_list[y])
                count = type_list[y].count()
                m1 = type_list[y].filter(date_created__istartswith=str(now_year) + "-" + "01").count()
                m2 = type_list[y].filter(date_created__istartswith=str(now_year) + "-" + "02").count()
                m3 = type_list[y].filter(date_created__istartswith=str(now_year) + "-" + "03").count()
                m4 = type_list[y].filter(date_created__istartswith=str(now_year) + "-" + "04").count()
                m5 = type_list[y].filter(date_created__istartswith=str(now_year) + "-" + "05").count()
                m6 = type_list[y].filter(date_created__istartswith=str(now_year) + "-" + "06").count()
                m7 = type_list[y].filter(date_created__istartswith=str(now_year) + "-" + "07").count()
                m8 = type_list[y].filter(date_created__istartswith=str(now_year) + "-" + "08").count()
                m9 = type_list[y].filter(date_created__istartswith=str(now_year) + "-" + "09").count()
                m10 = type_list[y].filter(date_created__istartswith=str(now_year) + "-" + "10").count()
                m11 = type_list[y].filter(date_created__istartswith=str(now_year) + "-" + "11").count()
                m12 = type_list[y].filter(date_created__istartswith=str(now_year) + "-" + "12").count()
                tests_counts_year[name_list[y]] = count

                qtly = {}
                # Quarterly
                jan_mar = m1 + m2 + m3
                apr_jun = m4 + m5 + m6
                jul_sep = m7 + m8 + m9
                oct_dec = m10 + m11 + m12
                list_quarterly = ['jan_mar', 'apr_jun', 'jul_sep', 'oct_dec']
                list_quarterly_data = [jan_mar, apr_jun, jul_sep, oct_dec]

                i = 0
                for x in list_quarterly:
                    if list_quarterly_data[i]:
                        qtly[list_quarterly[i]] = list_quarterly_data[i]
                    else:
                        qtly[list_quarterly[i]] = '-'
                    i += 1

                tests_counts_qtly[name_list[y]] = {}
                tests_counts_qtly[name_list[y]] = qtly

                mthly = {}
                # Monthly
                list_months_data = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
                list_months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
                               'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
                i = 0
                for x in list_months:
                    if list_months_data[i]:
                        mthly[list_months[i]] = list_months_data[i]
                    else:
                        mthly[list_months[i]] = '-'
                    i += 1
                tests_counts_month[name_list[y]] = {}
                tests_counts_month[name_list[y]] = mthly
        except:
            print("error somewhere")

        data_counts['total_' + str(now.year)] = tests_counts_year
        data_counts['total_qtly'] = tests_counts_qtly
        data_counts['total_month'] = tests_counts_month
        data = []
        data.append(data_counts)
        print('=====================')

        return JsonResponse(data, safe=False)


def xray_tests_stats_2_this_year(request):  # OK
    if request.method == 'GET':
        xray_test_type = []
        type_qs = []
        cat = RadiTestCategory.objects.all()
        type = RadiTestType.objects.all()
        type_u1 = type.filter(category=cat[2])
        type_u2 = type.filter(category=cat[3])
        for x in type_u1:
            type_qs.append(x)
        for x in type_u2:
            type_qs.append(x)
        xray_test_type.append(type_u1)
        xray_test_type.append(type_u2)          # step 1a

        type_list = []  # changes from name to query set in the try block
        name_list = []  # remains name e.g "HB", "CBC"
        for x in xray_test_type[0]:
            type_list.append(x.type_name)
            name_list.append(x.type_name)
        for y in xray_test_type[1]:
            type_list.append(y.type_name)       # step 1b
            name_list.append(y.type_name)
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        ms = ['m01', 'm02', 'm03', 'm04', 'm05', 'm06', 'm07', 'm08', 'm09', 'm10', 'm11', 'm12']

        data_counts_detail = {}
        try:
            sex = ["MALE", "FEMALE"]
            age = ['0-1', "1-5", "5-15", "15-45", "45+"]
            age1 = [0, 1, 6, 16, 45, 150]
            all_test_this_year = XExamItem.objects.filter(date_created__istartswith=str(now_year))                  # step 2a
            all_test_this_year_count = all_test_this_year.count()    # step 2b
            w = 0
            for mt in months:
                mtDict = {}
                data_counts_detail[mt] = mtDict
                mt = all_test_this_year.filter(date_created__istartswith=str(now_year) + "-" + str(months.index(mt)+1).zfill(2))
                ms[w] = mt.count()

                w += 1
                y = 0
                for type in type_qs:
                    typeDict = {}
                    mtDict[type_list[y]] = typeDict
                    test_by_type_this_mth = mt.filter(xtype=type)                   # Ok - step
                    test_by_type_this_mth_count = test_by_type_this_mth.count()
                    y += 1
                    i = 0
                    j = 1
                    for age_range in age:
                        age_rangeDict = {}
                        typeDict[age_range] = age_rangeDict
                        test_by_age_this_mth = test_by_type_this_mth.filter(xexam__patient__patient__age__gte=age1[i],
                                                                            xexam__patient__patient__age__lt=age1[j])
                        i += 1
                        j += 1
                        p = 0
                        for gender_type in sex:
                            gender = test_by_age_this_mth.filter(xexam__patient__patient__sex=gender_type)
                            gender_count = gender.count()
                            if gender_count == 0:
                                age_rangeDict[gender_type] = '-'
                            else:
                                age_rangeDict[gender_type] = gender_count
                            p += 1
            data_counts = {}
            tests_counts_year = {}
            tests_counts_qtly = {}
            tests_counts_month = {}

            qtly = {}
            # Quarterly
            list_quarterly = ['jan_mar', 'apr_jun', 'jul_sep', 'oct_dec']
            jan_mar = ms[0] + ms[1] + ms[2]
            apr_jun = ms[3] + ms[4] + ms[5]
            jul_sep = ms[6] + ms[7] + ms[8]
            oct_dec = ms[9] + ms[10] + ms[11]
            list_months_data = [ms[0], ms[1], ms[2], ms[3], ms[4], ms[5], ms[6], ms[7], ms[8], ms[9], ms[10], ms[11]]
            list_quarterly_data = [jan_mar, apr_jun, jul_sep, oct_dec]

            i = 0
            for x in list_quarterly:
                if list_quarterly_data[i]:
                    qtly[list_quarterly[i]] = list_quarterly_data[i]
                else:
                    qtly[list_quarterly[i]] = '-'
                i += 1

            mthly = {}
            # Monthly
            i = 0
            for x in months:
                if list_months_data[i]:
                    mthly[months[i]] = list_months_data[i]
                else:
                    mthly[months[i]] = '-'
                i += 1

            for y in range(0, len(name_list)):
                type_list[y] = all_test_this_year.filter(xtype__type_name=name_list[y])
                count = type_list[y].count()

                tests_counts_year[name_list[y]] = count

        except:
            print("error somewhere")

        data_counts['total_' + str(now.year)] = all_test_this_year_count
        data_counts['total_qtly'] = qtly
        #data_counts['total_month'] = mthly
        data = []
        data.append(data_counts)
        data.append(data_counts_detail)
        print('=====================')
        print(data)

        return JsonResponse(data, safe=False)


def validate_code(request):
    if request.method == 'POST':
        code = request.POST["code"]
        staff = request.POST["staff"]

        if staff != "":
            qt = RadiStaff.objects.get(id=staff)
            if qt.code == code:
                print("validated")
                return JsonResponse("VALID", safe=False)
            else:
                return JsonResponse("NOT VALID", safe=False)
        else:
            return JsonResponse("STAFF NOT SELECTED", safe=False)