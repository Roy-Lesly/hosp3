import datetime
import json
from django.http import JsonResponse
from apps.labo.models import LaboPatient, LaboExam, LaboTestType, LaboStaff, LaboExamItem
from apps.regi.models import Patient

now = datetime.datetime.now()
now_year = now.year
now_month = now.month
now_day = now.day
search_month = str(now_year) + "-" + str(now_month).zfill(2)
search_day = str(now_year) + "-" + str(now_month).zfill(2) + "-" + str(now_day).zfill(2)


def labo_exams_all(request):  # OK
    if request.method == 'GET':
        try:
            all_exams = LaboExam.objects.all().count()
            return JsonResponse(all_exams, safe=False)
        except:
            msg = 0
            return JsonResponse(msg, safe=False)


def labo_pats_this_year(request):  # OK
    if request.method == 'GET':
        try:
            all_pats_this_year = LaboPatient.objects.filter(date_created__istartswith=str(now_year)).count()
            return JsonResponse(all_pats_this_year, safe=False)
        except:
            msg = 0
            return JsonResponse(msg, safe=False)


def labo_exams_this_year(request):  # OK
    if request.method == 'GET':
        try:
            all_exams_this_year = LaboExam.objects.filter(date_created__istartswith=str(now_year)).count()
            return JsonResponse(all_exams_this_year, safe=False)
        except:
            msg = 0
            return JsonResponse(msg, safe=False)


# ===================== patients ===========================
def labo_pats_this_year(request):  # OK
    if request.method == 'GET':
        data = []
        this = {}
        last = {}
        try:
            all_lp = LaboPatient.objects.all().count()
        except:
            all_lp = 0
        try:
            all_lp_this_year = LaboPatient.objects.filter(date_created__istartswith=str(now_year)).count()
        except:
            all_lp_this_year = 0
        try:
            all_lp_last_year = LaboPatient.objects.filter(date_created__istartswith=str(now_year - 1)).count()
        except:
            all_lp_last_year = 0

        lp_this = LaboPatient.objects.all().filter(date_created__istartswith=now_year)
        total_this = LaboPatient.objects.all().filter(date_created__istartswith=now_year).count()
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


def labo_pats_last_year(request):  # OK
    if request.method == 'GET':
        data = []
        last = {}
        try:
            all_lp = LaboPatient.objects.all().count()
        except:
            all_lp = 0
        try:
            all_lp_last_year = LaboPatient.objects.filter(date_created__istartswith=str(now_year - 1)).count()
        except:
            all_lp_last_year = 0

        lp_last = LaboPatient.objects.all().filter(date_created__istartswith=now_year - 1)
        total_last = lp_last.count()
        m1 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "01").count()
        m2 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "02").count()
        m3 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "03").count()
        m4 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "04").count()
        m5 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "05").count()
        m6 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "06").count()
        m7 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "07").count()
        m8 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "08").count()
        m9 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "09").count()
        m10 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "10").count()
        m11 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "11").count()
        m12 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "12").count()

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
            mthly['jul'] = 0
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

        last_s = str(now_year - 1) + "_" + "Total_Patients"

        last[last_s] = all_lp_last_year
        last["quarterly"] = qtly
        last["monthly"] = mthly
        last[last_s] = all_lp_last_year

        data.append(last)
        print(data)
        return JsonResponse(data, safe=False)


# ==================== exams ===========================
def labo_exams_this_year(request):  # OK
    if request.method == 'GET':
        data = []
        this = {}
        last = {}
        try:
            all_lp = LaboExam.objects.all().count()
        except:
            all_lp = 0
        try:
            all_lp_this_year = LaboExam.objects.filter(date_created__istartswith=str(now_year)).count()
        except:
            all_lp_this_year = 0

        lp_this = LaboExam.objects.all().filter(date_created__istartswith=now_year)
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


def labo_exams_last_year(request):  # OK
    if request.method == 'GET':
        data = []
        this = {}
        last = {}
        try:
            all_lp = LaboPatient.objects.all().count()
        except:
            all_lp = 0
        try:
            all_lp_this_year = LaboPatient.objects.filter(date_created__istartswith=str(now_year)).count()
        except:
            all_lp_this_year = 0
        try:
            all_lp_last_year = LaboPatient.objects.filter(date_created__istartswith=str(now_year - 1)).count()
        except:
            all_lp_last_year = 0

        lp_this = LaboPatient.objects.all().filter(date_created__istartswith=now_year)
        total_this = LaboPatient.objects.all().filter(date_created__istartswith=now_year).count()
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
            mthly['jan'] = 0
        if m2:
            mthly['feb'] = m2
        else:
            mthly['feb'] = 0
        if m3:
            mthly['mar'] = m3
        else:
            mthly['mar'] = 0
        if m4:
            mthly['apr'] = m4
        else:
            mthly['apr'] = 0
        if m5:
            mthly['may'] = m5
        else:
            mthly['may'] = 0
        if m6:
            mthly['jun'] = m6
        else:
            mthly['jun'] = 0
        if m7:
            mthly['jul'] = m7
        else:
            mthly['jul'] = 0
        if m8:
            mthly['aug'] = m8
        else:
            mthly['aug'] = 0
        if m9:
            mthly['sep'] = m9
        else:
            mthly['sep'] = 0
        if m10:
            mthly['oct'] = m10
        else:
            mthly['oct'] = 0
        if m11:
            mthly['nov'] = m11
        else:
            mthly['nov'] = 0
        if m12:
            mthly['dec'] = m12
        else:
            mthly['dec'] = 0

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


# ==================== exam tests ===========================
def labo_exams_item_this_year(request):  # OK
    if request.method == 'GET':
        data = []
        this = {}
        last = {}
        try:
            all_lp = LaboExamItem.objects.all().count()
        except:
            all_lp = 0
        try:
            all_lp_this_year = LaboExamItem.objects.filter(date_created__istartswith=str(now_year)).count()
        except:
            all_lp_this_year = 0
        try:
            all_lp_last_year = LaboExamItem.objects.filter(date_created__istartswith=str(now_year - 1)).count()
        except:
            all_lp_last_year = 0

        lp_this = LaboExamItem.objects.all().filter(date_created__istartswith=now_year)
        total_this = lp_this.count()
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
            mthly['jan'] = 0
        if m2:
            mthly['feb'] = m2
        else:
            mthly['feb'] = 0
        if m3:
            mthly['mar'] = m3
        else:
            mthly['mar'] = 0
        if m4:
            mthly['apr'] = m4
        else:
            mthly['apr'] = 0
        if m5:
            mthly['may'] = m5
        else:
            mthly['may'] = 0
        if m6:
            mthly['jun'] = m6
        else:
            mthly['jun'] = 0
        if m7:
            mthly['jul'] = m7
        else:
            mthly['jul'] = 0
        if m8:
            mthly['aug'] = m8
        else:
            mthly['aug'] = 0
        if m9:
            mthly['sep'] = m9
        else:
            mthly['sep'] = 0
        if m10:
            mthly['oct'] = m10
        else:
            mthly['oct'] = 0
        if m11:
            mthly['nov'] = m11
        else:
            mthly['nov'] = 0
        if m12:
            mthly['dec'] = m12
        else:
            mthly['dec'] = 0

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


def labo_exams_item_last_year(request):  # OK
    if request.method == 'GET':
        data = []
        last = {}
        try:
            all_lp = LaboPatient.objects.all().count()
        except:
            all_lp = 0
        try:
            all_lp_last_year = LaboPatient.objects.filter(date_created__istartswith=str(now_year - 1)).count()
        except:
            all_lp_last_year = 0

        lp_last = LaboPatient.objects.all().filter(date_created__istartswith=now_year - 1)
        total_last = lp_last.count()
        m1 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "01").count()
        m2 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "02").count()
        m3 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "03").count()
        m4 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "04").count()
        m5 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "05").count()
        m6 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "06").count()
        m7 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "07").count()
        m8 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "08").count()
        m9 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "09").count()
        m10 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "10").count()
        m11 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "11").count()
        m12 = lp_last.filter(date_created__istartswith=str(now_year - 1) + "-" + "12").count()

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
            mthly['jan'] = 0
        if m2:
            mthly['feb'] = m2
        else:
            mthly['feb'] = 0
        if m3:
            mthly['mar'] = m3
        else:
            mthly['mar'] = 0
        if m4:
            mthly['apr'] = m4
        else:
            mthly['apr'] = 0
        if m5:
            mthly['may'] = m5
        else:
            mthly['may'] = 0
        if m6:
            mthly['jun'] = m6
        else:
            mthly['jun'] = 0
        if m7:
            mthly['jul'] = m7
        else:
            mthly['jul'] = 0
        if m8:
            mthly['aug'] = m8
        else:
            mthly['aug'] = 0
        if m9:
            mthly['sep'] = m9
        else:
            mthly['sep'] = 0
        if m10:
            mthly['oct'] = m10
        else:
            mthly['oct'] = 0
        if m11:
            mthly['nov'] = m11
        else:
            mthly['nov'] = 0
        if m12:
            mthly['dec'] = m12
        else:
            mthly['dec'] = 0

        last_s = str(now_year - 1) + "_" + "Total_Patients"

        last[last_s] = all_lp_last_year
        last["quarterly"] = qtly
        last["monthly"] = mthly
        last[last_s] = all_lp_last_year

        data.append(last)
        print(data)
        return JsonResponse(data, safe=False)


# ==================== Tests ==============================
def labo_tests_stats_this_year(request):  # OK
    if request.method == 'GET':
        type = LaboTestType.objects.all()
        type_list = []  # changes from name to query set in the try block
        name_list = []  # remains name e.g "HB", "CBC"
        for x in type:
            type_list.append(x.type_name)
            name_list.append(x.type_name)

        try:
            all_test_this_year = LaboExamItem.objects.filter(date_created__istartswith=str(now_year))
            data_counts = {}
            tests_counts_year = {}
            tests_counts_qtly = {}
            tests_counts_month = {}

            for y in range(0, len(name_list)):
                type_list[y] = all_test_this_year.filter(ltype__type_name=name_list[y])
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
        print(data)

        return JsonResponse(data, safe=False)


def search_labo_patient(request):
    if request.method == 'POST':
        qt = json.loads(request.body).get('queryType')
        search_str = json.loads(request.body).get('searchText')

        if qt == "ln":
            patient = LaboPatient.objects.all().filter(ln__istartswith=search_str)
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
            patient = LaboPatient.objects.all().filter(patient_id__Phone__istartswith=search_str)
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

        lpatient = LaboPatient.objects.all().filter(  # return list of qs
            ln__istartswith=search_str) | LaboPatient.objects.all().filter(
            patient_id__first_name__istartswith=search_str) | LaboPatient.objects.all().filter(
            patient_id__sn__istartswith=search_str) | LaboPatient.objects.all().filter(
            patient_id__Phone__istartswith=search_str)
        if lpatient:
            i = 0
            fnpat = []  # list of objects in lpatient
            spat = []  # list of objects in lpatient
            phpat = []  # list of objects in lpatient
            for x in lpatient:
                fn = x.patient.first_name + ' ' + x.patient.last_name
                sex = x.patient.sex
                ph = x.patient.Phone
                fnpat.append(fn)
                phpat.append(ph)
                spat.append(sex)
            datvals = lpatient.values()
            datlist = list(datvals)
            # data = list(datlist, lnpat, fnpat, l_n, phpat)

            return JsonResponse([datlist, fnpat, spat, phpat], safe=False)
        else:
            return JsonResponse("", safe=False)


def search_labo_exam(request):
    if request.method == 'POST':
        qt = json.loads(request.body).get('queryType')
        search_str = json.loads(request.body).get('searchText')
        print(qt + "  " + search_str)

        if qt == "book_num":
            patient = LaboExam.objects.all().filter(book_num__istartswith=search_str)
            # print(patient)
            if patient:
                dataValues = patient.values()
                datlist = list(dataValues)
                p = 0
                for x in patient:
                    ln = x.patient.ln
                    bn = x.book_num
                    full_n = x.patient.patient.full_name
                    sex = x.patient.patient.sex
                    age = x.patient.patient.age
                    address = x.patient.patient.address
                    ph = x.patient.patient.Phone
                    date_created = x.patient.patient.date_created.date()

                    datlist[p]["ln"] = ln
                    datlist[p]["book_num"] = bn
                    datlist[p]["full_name"] = full_n
                    datlist[p]["address"] = address
                    datlist[p]["age"] = age
                    datlist[p]["sex"] = sex
                    datlist[p]["Phone"] = ph
                    datlist[p]["date_created"] = date_created
                    p += 1
                # print(datlist)
                return JsonResponse([datlist], safe=False)
            else:
                return JsonResponse("", safe=False)

        if qt == "Phone":
            patient = LaboPatient.objects.all().filter(patient_id__Phone__istartswith=search_str)
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
                    date_created = x.date_created.date()

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


def search_labo_test(request):
    if request.method == 'POST':
        try:
            print("search by category")
            qt = LaboTestType.objects.filter(category=request.POST["category"])
            if qt:
                qtList = list(qt.values())
                return JsonResponse([qtList], safe=False)
            else:
                return JsonResponse("", safe=False)
        except:
            pass
        try:
            print("search by book_num")
            exam = LaboExam.objects.get(book_num=request.POST["book_num"])
            tests = LaboExamItem.objects.filter(lexam=exam)
            if tests:
                tests_list = list(tests.values())
                n = 0
                for x in tests:
                    ltype_name = x.ltype.type_name
                    tests_list[n]['ltype_name'] = ltype_name
                    n += 1

                return JsonResponse([tests_list], safe=False)
            else:
                return JsonResponse("", safe=False)
        except:
            pass


def validate_code(request):
    if request.method == 'POST':
        code = request.POST["code"]
        staff = request.POST["staff"]

        if staff != "":
            qt = LaboStaff.objects.get(id=staff)
            if qt.code == code:
                print("validated")
                return JsonResponse("VALID", safe=False)
            else:
                return JsonResponse("NOT VALID", safe=False)
        else:
            return JsonResponse("STAFF NOT SELECTED", safe=False)
