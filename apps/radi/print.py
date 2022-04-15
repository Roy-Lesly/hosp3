import datetime
import json
import os
from django.http import JsonResponse
from apps.radi.models import *
from collections import Counter
from docxtpl import DocxTemplate

from datetime import date


now = datetime.datetime.now()
now_year = now.year
now_month = now.month
now_day = now.day
search_month = str(now_year) + "-" + str(now_month).zfill(2)
search_day = str(now_year) + "-" + str(now_month).zfill(2) + "-" + str(now_day).zfill(2)


def u_this_month_stats(request):
    if request.method == "GET":
        try:
            uexamitem_this_month = UExamItem.objects.filter(date_created__month=now_month)
            uexam_this_month = UExam.objects.filter(date_created__month=now_month)
            print(uexamitem_this_month.count())
            print(uexam_this_month.count())
            test_all = RadiTestType.objects.all()
            all_months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY",
                          "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
            sex = ["MALE", "FEMALE"]
            age = ['0-1', "1-5", "5-15", "15-45", "45+"]
            age1 = [0, 1, 6, 16, 45, 150]
            tname_list = []
            for t in test_all:
                tname_list.append(t.type_name)
            dict = {}
            pats_this_month = uexamitem_this_month.filter(uexam__patient__date_created__month=now_month)

            print("========================= GETTING DATA ===========================")
            for test in tname_list:
                test_name_dict = {}
                dict[test] = test_name_dict
                items = uexamitem_this_month.filter(utype__type_name=test)
                x = 0
                i = 0
                j = 1
                for age_range in age:
                    age_range_dict = {}
                    test_name_dict[age_range] = age_range_dict
                    test_by_age_this_mth = items.filter(uexam__patient__patient__age__gte=age1[i],
                                                        uexam__patient__patient__age__lt=age1[j])
                    p = 0
                    i += 1
                    j += 1
                    for gender_type in sex:
                        gender = test_by_age_this_mth.filter(uexam__patient__patient__sex=gender_type)
                        gender_count = gender.count()
                        if gender_count == 0:
                            age_range_dict[gender_type] = 0
                        else:
                            age_range_dict[gender_type] = gender_count
                        p += 1

            print("========================= POPPING DATA ===========================")

            dataPel = dict.pop("PELVIC")
            dataAbd = dict.pop("ABDOMINAL")
            dataAbdPel = dict.pop("ABDOMINO-PELVIC")
            dataDop = dict.pop("DOPPLER")
            dataCard = dict.pop("CARDIAC")
            dataEcg = dict.pop("ECG")
            dataBur = dict.pop("BURKITT'S LYMPH")
            dataElas = dict.pop("ELASTOGRAPHY")

            dataA = dict.pop("OBSTETRIC 6")
            dataB = dict.pop("OBSTETRIC 10")
            dataC = dict.pop("THYROID")
            dataD = dict.pop("BREAST")
            dataE = dict.pop("SCROTAL")
            dataF = dict.pop("EYE")
            dataG = dict.pop("OTHER")
            dataH = dict.pop("OTHERS")
            dataI = dict.pop("TFU")
            dataJ = dict.pop("BIOPSY/ASPIRATI")

            dict["ABDOMINAL ULTRASOUND SCANS"] = dataAbd
            dict["ABDOMINO-PELVIC SCANS"] = dataAbdPel
            dict["PELVIC ULTRASOUND SCANS"] = dataPel

            print("================= JOIN OBSTETRIC (6 & 10) data1 ==================")
            data1 = {}
            dicts = [dataA, dataB]
            for a in dataA:
                data1[a] = {}
                i = 0
                for s in dataA[a]:
                    try:
                        list = [d[a][s] for d in dicts]
                        #new_val = sum([d[a][s] for d in dicts])
                        new_val = list[0] + list[1]
                    except:
                        new_val = 0
                    data1[a][s] = new_val
            dict["OBSTETRIC ULTRASOUND SCANS"] = data1

            print("================== JOIN ALL SMALL PARTS data2 ====================")
            data2 = {}
            print(dataE)
            dicts = [dataC, dataD, dataE, dataF, dataG, dataI]
            for a in dataA:
                data2[a] = {}
                for s in dataA[a]:
                    list = [d[a][s] for d in dicts]
                    new_val = list[0] + list[1] + list[2] + list[3] + list[4] + list[5]
                    data2[a][s] = new_val
            dict["SMALL PARTS (THYROID, BREAST, SCROTAL, EYE, TFU, OTHERS)"] = data2
            dict["VASCULAR (ARTERIES AND VEINS)"] = dataDop
            dict["CARDIAC ULTRASOUND SCANS"] = dataCard
            dict["ECG"] = dataEcg
            print("================== OTHER SPECIAL EXAMS data3 =====================")
            data3 = {}
            dicts = [dataH, dataI, dataJ]
            for a in dataH:
                data3[a] = {}
                for s in dataH[a]:
                    try:
                        list = [d[a][s] for d in dicts]
                        new_val = list[0] + list[1]
                    except:
                        new_val = 0
                    data3[a][s] = new_val
            dict["ULTRASOUND GUIDED (BIOPSY / ASPIRATIONS)"] = dataJ
            dict["BURKITT'S LYMPHOMA STUDIES"] = dataBur
            dict["ELASTOGRAPHY"] = dataElas

            dictTot = {}
            x = 1
            for t in dict:
                sum = 0
                for a in dict[t]:
                    for s in dict[t][a].values():
                        sum += s
                if sum != 0:
                    dictTot["T" + str(x)] = sum
                else:
                    dictTot["T" + str(x)] = ""
                x += 1
            print(dictTot)

            print("==================== Generating Stats =====================")
        except:
            pass

        print("=================== CHANGING SEX KEYS =====================")

        dict2 = {}
        for t in dictTot:
            dict2[t] = dictTot[t]
        x = 1
        for name in dict.values():
            y = 1
            for age in name.values():
                m = age.pop("MALE")
                f = age.pop("FEMALE")
                age["M" + str(x) + str(y)] = m
                age["F" + str(x) + str(y)] = f
                if m != 0:
                    dict2["M" + str(x) + str(y)] = m
                else:
                    dict2["M" + str(x) + str(y)] = ""
                if f != 0:
                    dict2["F" + str(x) + str(y)] = f
                else:
                    dict2["F" + str(x) + str(y)] = ""
                y += 1
            x += 1
        print("dict2")
        #print(dict2)
        i = 1
        for name in dict:
            dict2["TEST" + str(i)] = name
            i += 1
        print("==================== APPENDING1 dicts ======================")
        dict2["TOTAL"] = uexamitem_this_month.count()
        dict2["NEW"] = pats_this_month.count()
        dict2["OLD"] = uexamitem_this_month.count() - pats_this_month.count()
        dict2["MONTH"] = all_months[now_month-1] + " " + str(now_year)
        dict["T0"] = uexamitem_this_month.count()
        print("path")
        path = os.path.abspath(os.path.dirname(__file__))
        print(path)
        
        try:
            print("==================== GENERATING WORD ======================")
            doc = DocxTemplate("/home/pi/folder1/word_templates/forms/stats.docx")
            context = dict2
            doc.render(context)
            doc.save("home/pi/folder1/word_templates/statistics/" + str(now_year) + str(now_month).zfill(2) + ".docx")
            #doc.save("../../Desktop/results/" + str(now_year) + str(now_month).zfill(2) + ".docx")
            print("==================== STATS GENERATED ======================")
            return JsonResponse("GENERATED", safe=False)
        except:
            print("================== STATS NOT GENERATED ====================")
            return JsonResponse("ERROR", safe=False)


def u_gen_stats(request):
    if request.method == "POST":
        try:
            uexamitem_this_month = UExamItem.objects.filter \
                (date_created__year=request.POST["year"]).filter \
                (date_created__month=request.POST["month"])
            test_all = RadiTestType.objects.all()
            all_months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY",
                          "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
            sex = ["MALE", "FEMALE"]
            age = ['0-1', "1-5", "5-15", "15-45", "45+"]
            age1 = [0, 1, 6, 16, 45, 150]
            tname_list = []
            for t in test_all:
                tname_list.append(t.type_name)
            dict = {}
            pats_this_month = uexamitem_this_month.filter(uexam__patient__date_created__month=now_month)

            print("========================= GETTING DATA ===========================")
            for test in tname_list:
                test_name_dict = {}
                dict[test] = test_name_dict
                items = uexamitem_this_month.filter(utype__type_name=test)
                x = 0
                i = 0
                j = 1
                for age_range in age:
                    age_range_dict = {}
                    test_name_dict[age_range] = age_range_dict
                    test_by_age_this_mth = items.filter(uexam__patient__patient__age__gte=age1[i],
                                                        uexam__patient__patient__age__lt=age1[j])
                    p = 0
                    i += 1
                    j += 1
                    for gender_type in sex:
                        gender = test_by_age_this_mth.filter(uexam__patient__patient__sex=gender_type)
                        gender_count = gender.count()
                        if gender_count == 0:
                            age_range_dict[gender_type] = 0
                        else:
                            age_range_dict[gender_type] = gender_count
                        p += 1

            print("========================= POPPING DATA ===========================")

            dataPel = dict.pop("PELVIC")
            dataAbd = dict.pop("ABDOMINAL")
            dataAbdPel = dict.pop("ABDOMINO-PELVIC")
            dataDop = dict.pop("DOPPLER")
            dataCard = dict.pop("CARDIAC")
            dataEcg = dict.pop("ECG")
            dataBur = dict.pop("BURKITT'S LYMPH")
            dataElas = dict.pop("ELASTOGRAPHY")

            dataA = dict.pop("OBSTETRIC 6")
            dataB = dict.pop("OBSTETRIC 10")
            dataC = dict.pop("THYROID")
            dataD = dict.pop("BREAST")
            dataE = dict.pop("SCROTAL")
            dataF = dict.pop("EYE")
            dataG = dict.pop("OTHER")
            dataH = dict.pop("TFU")
            dataI = dict.pop("OTHERS")
            dataJ = dict.pop("BIOPSY/ASPIRATI")

            dict["ABDOMINAL ULTRASOUND SCANS"] = dataAbd
            dict["ABDOMINO-PELVIC SCANS"] = dataAbdPel
            dict["PELVIC ULTRASOUND SCANS"] = dataPel
            #print(dict)

            print("================= JOIN OBSTETRIC (6 & 10) data1 ==================")
            data1 = {}
            dicts = [dataA, dataB]
            for a in dataA:
                data1[a] = {}
                i = 0
                for s in dataA[a]:
                    try:
                        list = [d[a][s] for d in dicts]
                        #new_val = sum([d[a][s] for d in dicts])
                        new_val = list[0] + list[1]
                    except:
                        new_val = 0
                    data1[a][s] = new_val
            dict["OBSTETRIC ULTRASOUND SCANS"] = data1
            print(dataB)

            print("================== JOIN ALL SMALL PARTS data2 ====================")
            data2 = {}
            dicts = [dataC, dataD, dataE, dataF, dataG]
            for a in dataC:
                data2[a] = {}
                for s in dataC[a]:
                    list = [d[a][s] for d in dicts]
                    new_val = list[0] + list[1] + list[2] + list[3] + list[4]
                    data2[a][s] = new_val
            dict["SMALL PARTS (THYROID, BREAST, SCROTAL, EYE, OTHERS)"] = data2
            dict["VASCULAR (ARTERIES AND VEINS)"] = dataDop
            #dict["TFU"] = dataH
            dict["CARDIAC ULTRASOUND SCANS"] = dataCard
            dict["ECG"] = dataEcg

            print("================== OTHER SPECIAL EXAMS data3 =====================")
            data3 = {}
            dicts = [dataH, dataI, dataJ]
            for a in dataH:
                data3[a] = {}
                for s in dataH[a]:
                    try:
                        list = [d[a][s] for d in dicts]
                        new_val = list[0] + list[1] + list[2]
                    except:
                        new_val = 0
                    data3[a][s] = new_val
            dict["OTHERS (TFU, GUIDED, BIOPSY, ASPIRATIONS)"] = data3
            dict["BURKITT'S LYMPHOMA STUDIES"] = dataBur
            dict["ELASTOGRAPHY"] = dataElas

            dictTot = {}
            x = 1
            for t in dict:
                sum = 0
                for a in dict[t]:
                    for s in dict[t][a].values():
                        sum += s
                if sum != 0:
                    dictTot["T" + str(x)] = sum
                else:
                    dictTot["T" + str(x)] = ""

                x += 1
            #print(dictTot)

            print("==================== Generating Stats =====================")
        except:
            pass

        print("=================== CHANGING SEX KEYS =====================")

        dict2 = {}
        for t in dictTot:
            dict2[t] = dictTot[t]
        x = 1
        for name in dict.values():
            y = 1
            for age in name.values():
                m = age.pop("MALE")
                f = age.pop("FEMALE")
                age["M" + str(x) + str(y)] = m
                age["F" + str(x) + str(y)] = f
                if m != 0:
                    dict2["M" + str(x) + str(y)] = m
                else:
                    dict2["M" + str(x) + str(y)] = ""
                if f != 0:
                    dict2["F" + str(x) + str(y)] = f
                else:
                    dict2["F" + str(x) + str(y)] = ""
                y += 1
            x += 1
        #print(dict2)
        i = 1
        for name in dict:
            dict2["TEST" + str(i)] = name
            i += 1
        print("==================== APPENDING2 dicts ======================")
        dict2["TOTAL"] = uexamitem_this_month.count()
        dict2["T0"] = uexamitem_this_month.count()
        dict2["NEW"] = pats_this_month.count()
        dict2["OLD"] = uexamitem_this_month.count() - pats_this_month.count()
        dict2["MONTH"] = all_months[int(request.POST["month"])-1] + " " + str(now_year)
        print("HERE3")

        try:
            print("==================== GENERATING WORD ======================")
            try:
                doc = DocxTemplate("word_templates/forms/stats.docx")
                doc.render(dict2)
                doc.save("../Users/ULTRASOUND/Desktop/statistics/" + request.POST["year"] + request.POST["month"].zfill(2) + ".docx")
                doc.save("word_templates/statistics/" + request.POST["year"] + request.POST["month"].zfill(2) + ".docx")
                print("From US DESKTOP Server")
            except:
                try:
                    doc = DocxTemplate("home/pi/folder1/word_templates/forms/stats.docx")
                    doc.render(dict2)
                    doc.save("../Users/ULTRASOUND/Desktop/statistics/" + request.POST["year"] + request.POST["month"].zfill(2) + ".docx")
                    doc.save("word_templates/statistics/" + request.POST["year"] + request.POST["month"].zfill(2) + ".docx")
                    print("From US R-Pi Server")
                except:
                    doc = DocxTemplate("word_templates/forms/stats.docx")
                    doc.render(dict2)
                    doc.save("../Users/ZANE/Desktop/statistics/" + request.POST["year"] + request.POST["month"].zfill(2) + ".docx")
                    doc.save("word_templates/statistics/" + request.POST["year"] + request.POST["month"].zfill(2) + ".docx")
                    print("From Laptop Server")
            print("==================== STATS GENERATED ======================")
            return JsonResponse("GENERATED", safe=False)
        except:
            print("================== STATS NOT GENERATED ====================")
            return JsonResponse("ERROR", safe=False)
