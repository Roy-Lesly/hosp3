import datetime
import calendar
import json
from django.http import JsonResponse
from apps.radi.models import *
from apps.regi.models import Patient
from django.template.loader import render_to_string


now = datetime.datetime.now()
now_year = now.year
now_month = now.month
now_day = now.day
search_month = str(now_year) + "-" + str(now_month).zfill(2)
search_day = str(now_year) + "-" + str(now_month).zfill(2) + "-" + str(now_day).zfill(2)
c = calendar.Calendar()
list_months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']


def echo_pats_quarterly_monthly_this_year(request):                # OK
    if request.method == 'GET':
        data = []
        data1 = {}
        data2 = {}
        this_year_total = {}
        this_year_exams = LaboPatient.objects.all().filter(
            date_created__istartswith=now_year).count()
        yexam = LaboPatient.objects.all().filter(date_created__istartswith=now_year)
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


def echo_exams_quarterly_monthly_this_year(request):                # OK
    if request.method == 'GET':
        data = []
        data1 = []
        data2 = []
        this_year_total = []
        this_year_exams = LaboExam.objects.all().filter(
            date_created__istartswith=now_year).count()
        this_year_total.append(this_year_exams)
        yexam = LaboExam.objects.all().filter(date_created__istartswith=now_year)
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


def echo_pats_quarterly_monthly_last_year(request):                # OK
    if request.method == 'GET':
        data = []
        data1 = {}
        data2 = {}
        last_year_total = {}
        last_year_exams = LaboPatient.objects.all().filter(
            date_created__istartswith=now_year - 1).count()
        yexam = LaboPatient.objects.all().filter(date_created__istartswith=now_year - 1)
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


def echo_pats_quarterly_monthly_last_year_bk(request):                # OK
    if request.method == 'GET':
        data = []
        data1 = []
        data2 = []
        this_year_total = []
        this_year_exams = LaboPatient.objects.all().filter(
            date_created__istartswith=now_year - 1).count()
        this_year_total.append(this_year_exams)
        yexam = LaboPatient.objects.all().filter(date_created__istartswith=now_year - 1)
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


def echo_exams_quarterly_monthly_last_year(request):                # OK
    if request.method == 'GET':
        data = []
        data1 = []
        data2 = []
        this_year_total = []
        this_year_exams = LaboExam.objects.all().filter(
            date_created__istartswith=now_year - 1).count()
        this_year_total.append(this_year_exams)
        yexam = LaboExam.objects.all().filter(date_created__istartswith=now_year - 1)
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


def search_patient(request):
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


def search_echo_patient(request):
    if request.method == 'POST':
        qt = json.loads(request.body).get('queryType')
        search_str = json.loads(request.body).get('searchText')

        if qt == "un":
            # patient = UPatient.objects.all().filter(un__istartswith=search_str)
            patient = UPatient.objects.all().filter(book_num__istartswith=search_str)
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
            patient = UPatient.objects.all().filter(patient_id__Phone__istartswith=search_str)
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


def search_echo_exam(request):
    if request.method == 'POST':
        qt = json.loads(request.body).get('queryType')
        search_str = json.loads(request.body).get('searchText')
        print(qt + "  " + search_str)

        if qt == "book_num":
            uexam = UExam.objects.all().filter(book_num__istartswith=search_str)
            print(uexam)
            if uexam:
                dataValues = uexam.values()
                datlist = list(dataValues)
                p = 0
                for x in uexam:
                    sn = x.patient.patient.sn
                    un = x.patient.un
                    bn = x.book_num
                    full_n = x.patient.patient.full_name
                    sex = x.patient.patient.sex
                    age = x.patient.patient.age
                    address = x.patient.patient.address
                    ph = x.patient.patient.Phone
                    date_created = x.patient.patient.date_created.date()

                    datlist[p]["sn"] = sn
                    datlist[p]["un"] = un
                    datlist[p]["bn"] = bn
                    datlist[p]["full_name"] = full_n
                    datlist[p]["address"] = address
                    datlist[p]["age"] = age
                    datlist[p]["sex"] = sex
                    datlist[p]["Phone"] = ph
                    datlist[p]["date_created"] = date_created
                    p += 1
                #print(datlist)
                return JsonResponse([datlist], safe=False)
            else:
                return JsonResponse("", safe=False)

        if qt == "Phone":
            uexam = UExam.objects.all().filter(patient_id__patient_id__Phone__istartswith=search_str)
            #print(uexam)
            if uexam:
                dataValues = uexam.values()
                datlist = list(dataValues)
                p = 0
                for x in uexam:
                    sn = x.patient.patient.sn
                    un = x.patient.un
                    bn = x.book_num
                    full_n = x.patient.patient.full_name
                    sex = x.patient.patient.sex
                    age = x.patient.patient.age
                    address = x.patient.patient.address
                    ph = x.patient.patient.Phone
                    date_created = x.patient.patient.date_created.date()

                    datlist[p]["sn"] = sn
                    datlist[p]["un"] = un
                    datlist[p]["bn"] = bn
                    datlist[p]["full_name"] = full_n
                    datlist[p]["address"] = address
                    datlist[p]["age"] = age
                    datlist[p]["sex"] = sex
                    datlist[p]["Phone"] = ph
                    datlist[p]["date_created"] = date_created
                    p += 1
                #print(datlist)
                return JsonResponse([datlist], safe=False)
            else:
                return JsonResponse("", safe=False)


def search_echo_test(request):
    if request.method == 'POST':
        print(request.POST)
        try:
            #print("search by cat-echo")
            #print(request.POST)
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
            #print("search by book_num")
            #print(request.POST["book_num"])
            exam = UExam.objects.get(book_num=request.POST["book_num"])
            #print(exam)
            tests = UExamItem.objects.filter(uexam=exam)

            print(tests)
            if tests:
                tests_list = list(tests.values())
                #print(tests_list)
                #print(tests_list[0])
                #print(tests_list[1])
                n = 0
                for x in tests:
                    tests_list[n]['utype'] = x.utype.type_name
                    #print(x.utype)
                    n += 1
                #print(tests_list[0])
                #print(tests_list[1])
                print('===============')
                #print(tests_list)

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
def echo_exams_stats_0_this_month(request):  # OK
    #mths_name = [calendar.month_name[i] for i in range(1, len(calendar.month_abbr))]    # Full Name
    #mths_abbr = [calendar.month_abbr[i] for i in range(1, len(calendar.month_abbr))]    # Abbr Name
    #mths_num = [i for i in range(1, len(calendar.month_abbr))]                          # Month Number
    mth_days = [day for day in c.itermonthdays(now_year, now_month) if day != 0]        # Month Day Number

    if request.method == 'GET':
        try:
            uexam = UExam.objects.all().count()
        except:
            uexam = 0
        try:
            uexam_this_month = UExam.objects.filter(date_created__month=str(now_month))
            uexamitem_this_month = UExamItem.objects.filter(date_created__month=str(now_month))
            #mth_d_count_list = []
            mth_d_count_dict = {}
            paid = []
            t_sum = 0
            for day in mth_days:
                cou = uexam_this_month.filter(date_created__day=day).count()
                today_items = uexamitem_this_month.filter(date_created__day=day)
                paid_day = []
                sum = 0
                for item in today_items:
                    paid_day.append(item.paid)
                    sum += int(item.paid)
                paid.append(sum)
                t_sum += sum
                mth_d_count_dict["d" + str(day)] = cou
            paid.append(t_sum)
            mth_d_count_dict["tot"] = uexam_this_month.count()
            mth_d_count_dict["month"] = now.strftime("%B").upper()
            mth_d_count_dict["paid"] = paid
        except:
            return JsonResponse("", safe=False)

        return JsonResponse(mth_d_count_dict, safe=False)


def echo_pats_chart_1_this_year(request):  # OK
    if request.method == 'GET':
        data = []
        this = {}
        last = {}
        try:
            all_lp = UPatient.objects.all().count()
        except:
            all_lp = 0
        try:
            all_lp_this_year = UPatient.objects.filter(date_created__istartswith=str(now_year)).count()
        except:
            all_lp_this_year = 0
        try:
            all_lp_last_year = UPatient.objects.filter(date_created__istartswith=str(now_year - 1)).count()
        except:
            all_lp_last_year = 0

        lp_this = UPatient.objects.all().filter(date_created__istartswith=now_year)
        total_this = UPatient.objects.all().filter(date_created__istartswith=now_year).count()
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


def echo_exams_chart_1_this_year(request):  # OK
    if request.method == 'GET':
        data = []
        this = {}
        last = {}
        try:
            all_lp = UExam.objects.all().count()
        except:
            all_lp = 0
        try:
            all_lp_this_year = UExam.objects.filter(date_created__istartswith=str(now_year)).count()
        except:
            all_lp_this_year = 0

        lp_this = UExam.objects.all().filter(date_created__istartswith=now_year)
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


def echo_tests_stats_1_this_year(request):  # OK
    if request.method == 'GET':
        echo_test = []
        cat = RadiTestCategory.objects.all()
        type = RadiTestType.objects.all()
        type_u1 = type.filter(category=cat[0])
        type_u2 = type.filter(category=cat[1])
        echo_test.append(type_u1)
        echo_test.append(type_u2)

        type_list = []  # changes from name to query set in the try block
        name_list = []  # remains name e.g "HB", "CBC"
        for x in echo_test[0]:
            type_list.append(x.type_name)
            name_list.append(x.type_name)
        for y in echo_test[1]:
            type_list.append(y.type_name)
            name_list.append(y.type_name)

        try:
            all_test_this_year = UExamItem.objects.filter(date_created__istartswith=str(now_year))
            data_counts = {}
            tests_counts_year = {}
            tests_counts_qtly = {}
            tests_counts_month = {}

            for y in range(0, len(name_list)):
                type_list[y] = all_test_this_year.filter(utype__type_name=name_list[y])
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

                i = 0
                for x in list_months:
                    if list_months_data[i]:
                        mthly[list_months[i]] = list_months_data[i]
                    else:
                        mthly[list_months[i]] = '-'
                    i += 1
                tests_counts_month[name_list[y]] = {}
                tests_counts_month[name_list[y]] = mthly
            print(tests_counts_year)
        except:
            print("error somewhere")

        data_counts['total_' + str(now.year)] = tests_counts_year
        data_counts['total_qtly'] = tests_counts_qtly
        data_counts['total_month'] = tests_counts_month
        data = []
        data.append(data_counts)
        print('=========1============')
        # print(data)

        return JsonResponse(data, safe=False)


def echo_tests_stats_2_this_year(request):  # OK
    if request.method == 'GET':
        echo_test_type = []
        type_qs = []
        cat = RadiTestCategory.objects.all()
        type = RadiTestType.objects.all()
        type_u1 = type.filter(category=cat[0])
        type_u2 = type.filter(category=cat[1])
        for x in type_u1:
            type_qs.append(x)
        for x in type_u2:
            type_qs.append(x)
        echo_test_type.append(type_u1)
        echo_test_type.append(type_u2)          # step 1a

        type_list = []  # changes from name to query set in the try block
        name_list = []  # remains name e.g "HB", "CBC"
        for x in echo_test_type[0]:
            type_list.append(x.type_name)
            name_list.append(x.type_name)
        for y in echo_test_type[1]:
            type_list.append(y.type_name)       # step 1b
            name_list.append(y.type_name)
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        ms = ['m01', 'm02', 'm03', 'm04', 'm05', 'm06', 'm07', 'm08', 'm09', 'm10', 'm11', 'm12']

        data_counts_detail = {}
        try:
            sex = ["MALE", "FEMALE"]
            age = ['0-1', "1-5", "5-15", "15-45", "45+"]
            age1 = [0, 1, 6, 16, 45, 150]
            all_test_this_year = UExamItem.objects.filter(date_created__istartswith=str(now_year))                  # step 2a
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
                    test_by_type_this_mth = mt.filter(utype=type)                   # Ok - step
                    test_by_type_this_mth_count = test_by_type_this_mth.count()
                    y += 1
                    i = 0
                    j = 1
                    for age_range in age:
                        age_rangeDict = {}
                        typeDict[age_range] = age_rangeDict
                        test_by_age_this_mth = test_by_type_this_mth.filter(uexam__patient__patient__age__gte=age1[i],
                                                                            uexam__patient__patient__age__lt=age1[j])
                        i += 1
                        j += 1
                        p = 0
                        for gender_type in sex:
                            gender = test_by_age_this_mth.filter(uexam__patient__patient__sex=gender_type)
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
                type_list[y] = all_test_this_year.filter(utype__type_name=name_list[y])
                count = type_list[y].count()

                tests_counts_year[name_list[y]] = count

        except:
            print("error somewhere")

        data_counts['total_' + str(now.year)] = all_test_this_year_count
        data_counts['total_qtly'] = qtly
        data_counts['total_month'] = mthly
        data = []
        data.append(data_counts)
        data.append(data_counts_detail)
        print('=========2============')
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


def check_regnum_exist(request):
    if request.method == 'POST':
        reg_num = request.POST["reg_num"]

        try:
            qt = UExam.objects.get(book_num=reg_num)
            print("UExam Exist with this reg num")
            return JsonResponse("TAKEN", safe=False)
        except:
            print("No Exam with this reg num")
            return JsonResponse("NOT TAKEN", safe=False)


def check_test_exist_in_exam(request):
    if request.method == 'POST':
        id_utype = request.POST["id_utype"]
        try:
            qt = UFinding.objects.get(u_test_id=id_utype)
            print("UFinding Exist for this Procedure")
            return JsonResponse("TAKEN", safe=False)
        except:
            print("UFinding Not Exist")
            return JsonResponse("NOT TAKEN", safe=False)


def check_book_num_exist(request):
    if request.method == 'POST':
        bn = request.POST["book_num"]
        print(bn)
        try:
            qt = UExam.objects.get(book_num=bn)
            print("UExam Exist for this Patient")
            return JsonResponse("TAKEN", safe=False)
        except:
            print("UExam Not Exist")
            return JsonResponse("NOT TAKEN", safe=False)


def check_full_name_exist(request):
    if request.method == 'POST':
        full_name = request.POST["full_name"]
        print(full_name)
        print(full_name.upper())
        try:
            qt = Patient.objects.get(full_name=full_name.upper())
            print("Patient Exist for this Patient")
            return JsonResponse("TAKEN", safe=False)
        except:
            print("Patient Not Exist")
            return JsonResponse("NOT TAKEN", safe=False)


def notification_items(request):
    # ===== pats with no exams ====
    uexs = UExam.objects.all().values_list('patient', flat=True)
    upts = UPatient.objects.exclude(un__in=uexs)
    # ===== Exam with no test ====
    test = UExamItem.objects.all().values_list('uexam', flat=True)
    uexam = UExam.objects.exclude(book_num__in=test)
    # ===== Echo male ob exams ====
    examitems = UExamItem.objects.all()
    male_obs = examitems.filter(utype__type_name="OBSTETRIC 6")\
                   .filter(uexam__patient__patient__sex="MALE") | \
               examitems.filter(utype__type_name="OBSTETRIC 10")\
                   .filter(uexam__patient__patient__sex="MALE")

    exams = UExam.objects.filter(date_created__year=now_year,
                                 date_created__month=now_month,)
    list = []
    for ex in exams:
        e = (ex.book_num)[1:6]
        n = ''.join(filter(str.isdigit, e))
        list.append(int(n))
    list_sort = sorted(list)
    s = sorted(set(range(list_sort[0], list_sort[-1])).difference(list_sort))

    ex = UExam.objects.filter(date_created__month=now_month)
    print("items.count()")
    print(ex.count())

    ok_list = []
    for item in ex:
        x = item.book_num[1:6]
        if x.isnumeric():
            ok_list.append(int(x))
    ok_list.sort()
    #print(ok_list)
    l = [x for x in range(ok_list[0], ok_list[-1] + 1) if x not in ok_list]

    x = 1
    for c in l:
        count4 = x
        x += 1

    print("skipped")
    print(count4)
    month = list_months[now_month - 1]
    string = month + " Skipped Numbers"
    context = {
        "info1": "Patients With No Exams", "cont1": upts.count(),
        "info2": "Exams With No Test", "cont2": uexam.count(),
        "info3": "Echo Male OB Exams", "cont3": male_obs.count(),
        "info4": string, "cont4": count4,
    }
    return JsonResponse(context, safe=False)


def pat_with_no_exam(request):
    print("pat no ")
    pts = UExam.objects.all().values_list('patient', flat=True)
    upat = UPatient.objects.exclude(un__in=pts)
    print(upat.count())
    print(upat)
    cat = RadiTestCategory.objects.filter(category_name__startswith='ECHO')
    catList = []
    for cat in cat:
        catList.append(cat.category_name)
    if upat:
        dataValues = upat.values()
        datalist = []
        for x in upat:
            print(x)
            datadict = {}
            un = x.un
            sn = x.patient.sn
            age = x.patient.age
            sex = x.patient.sex
            address = x.patient.address
            full_name = x.patient.full_name
            phone = x.patient.Phone
            date_created = x.date_created

            datadict["un"] = un
            datadict["sn"] = sn
            datadict["full_name"] = full_name
            datadict["address"] = address
            datadict["age"] = age
            datadict["sex"] = sex
            datadict["Phone"] = phone
            datadict["date_created"] = date_created.date()

            datalist.append(datadict)

            ex = UExamItem.objects.all().values_list('uexam', flat=True)

            upat = UPatient.objects.exclude(un__in=pts)
            uexam = UExam.objects.exclude(book_num__in=ex)
        context = {
            "info1": "Patients With NO Exams", "cont1": upat.count(),
            "info2": "Exams With No Procedures", "cont2": uexam.count(),
            "info3": "Exams With No Procedures", "cont3": uexam.count(),
            "data": datalist, "category": catList
        }
    else:
        context = {"data": "", "category": catList}
    html_form = render_to_string('radi/noti/echo_pat_no_exam.html', request=request)
    return JsonResponse({"html_form": html_form, "context": context})


def exam_with_no_test(request):
    pts = UExam.objects.all().values_list('patient', flat=True)
    ex = UExamItem.objects.all().values_list('uexam', flat=True)
    # upat = UPatient.objects.exclude(un__in=pts)
    uexam = UExam.objects.exclude(book_num__in=ex)
    print(ex.count())
    # print(upat)
    print(uexam)
    cat = RadiTestCategory.objects.filter(category_name__startswith='ECHO')
    catList = []
    for cat in cat:
        catList.append(cat.category_name)
    if uexam:
        dataValues = uexam.values()
        datalist = []
        for x in uexam:
            print(x)
            datadict = {}
            bn = x.book_num
            ward = x.ward
            age = x.patient.patient.age
            sex = x.patient.patient.sex
            address = x.patient.patient.address
            full_name = x.patient.patient.full_name
            phone = x.patient.patient.Phone
            date_created = x.date_created

            datadict["bn"] = bn
            datadict["ward"] = ward
            datadict["full_name"] = full_name
            datadict["address"] = address
            datadict["age"] = age
            datadict["sex"] = sex
            datadict["Phone"] = phone
            datadict["date_created"] = date_created.date()

            datalist.append(datadict)

            context = {"data": datalist, "category": catList}

    else:
        context = {"data": "", "category": catList}
    html_form = render_to_string('radi/noti/echo_exam_no_test.html', request=request)
    return JsonResponse({"html_form": html_form, "context": context})


def echo_exam_ob_male(request):
    exams = UExam.objects.all()
    examitems = UExamItem.objects.all()
    male_obs = examitems.filter(utype__type_name="OBSTETRIC 6").filter(uexam__patient__patient__sex="MALE") \
        | examitems.filter(utype__type_name="OBSTETRIC 10").filter(uexam__patient__patient__sex="MALE") \
            | examitems.filter(utype__type_name="OBSTETRIC 10").filter(uexam__patient__patient__dob__gte=now - datetime.timedelta(days = 366 * 12)) \
                | examitems.filter(utype__type_name="OBSTETRIC 6").filter(uexam__patient__patient__dob__gte=now - datetime.timedelta(days = 366 * 12))
    print("male ob and less than 10 years ======================================")
    print(male_obs.count())
    print(examitems.count())

    cat = RadiTestCategory.objects.filter(category_name__startswith='ECHO')
    catList = []
    for cat in cat:
        catList.append(cat.category_name)
    if male_obs:
        dataValues = male_obs.values()
        datalist = []
        for x in male_obs:
            datadict = {}
            id = x.id
            bn = x.uexam.book_num
            ward = x.uexam.ward
            age = x.uexam.patient.patient.age
            sex = x.uexam.patient.patient.sex
            address = x.uexam.patient.patient.address
            full_name = x.uexam.patient.patient.full_name
            phone = x.uexam.patient.patient.Phone
            date_created = x.date_created

            datadict["id"] = id
            datadict["bn"] = bn
            datadict["ward"] = ward
            datadict["full_name"] = full_name
            datadict["address"] = address
            datadict["age"] = age
            datadict["sex"] = sex
            datadict["Phone"] = phone
            datadict["date_created"] = date_created #.date()

            datalist.append(datadict)

        print(datalist)
        context = {
            "info3": "Echo Male OB Exams", "cont3": male_obs.count(),
            "data": datalist, "category": catList}

    else:
        context = {"data": "", "category": catList}
    html_form = render_to_string('radi/noti/echo_exam_ob_male.html', request=request)
    return JsonResponse({"html_form": html_form, "context": context})


def echo_skipped_number_this(request):
    items = UExam.objects.filter(date_created__month=now_month)

    ok_list = []
    for item in items:
        x = item.book_num[1:6]
        if x.isnumeric():
            ok_list.append(int(x))
    ok_list.sort()
    skipped = [x for x in range(ok_list[0], ok_list[-1]+1) if x not in ok_list]
    #skipped_this = [x for x in l]
    print("=============================")
    x = 1
    for c in skipped:
        count = x
        x += 1
    print("count")
    print(count)

    if True:
        month = list_months[now_month-1]
        string = month + " Skipped Numbers"
        context = {
            "info4": string, "cont4": count,
            "data": skipped, "category": []}

    else:
        context = {"data": "", "category": []}
    html_form = render_to_string('radi/noti/skipped_numbers.html', request=request)
    return JsonResponse({"html_form": html_form, "context": context})


def all_test_for_exam(request, book_num):
    exam = UExam.objects.get(book_num=book_num)
    all_tests = UExamItem.objects.filter(uexam=exam)
    print(all_tests)

    testList = []
    for test in all_tests:
        testList.append(test.id)
    if all_tests:
        dataValues = all_tests.values()
        datalist = []
        for x in all_tests:
            datadict = {}
            id = x.id
            bn = x.uexam.book_num
            full_name = x.uexam.patient.patient.full_name
            phone = x.uexam.patient.patient.Phone
            date_created = x.date_created

            datadict["id"] = id
            datadict["bn"] = bn
            datadict["full_name"] = full_name
            datadict["Phone"] = phone
            datadict["date_created"] = date_created

            datalist.append(datadict)

        context = {
            "All Test IDs": "All Test IDs", "list": datalist,
        }

    else:
        context = {"All Test IDs": "All Test IDs", "list": "",}
    html_form = render_to_string('radi/noti/echo_exam_ob_male.html', request=request)
    return JsonResponse({"html_form": html_form, "context": context})