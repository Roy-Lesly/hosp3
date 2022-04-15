from django.http import JsonResponse
from apps.regi.models import Patient
import json


def search_patient(request):
    if request.method == 'POST':
        qt = json.loads(request.body).get('queryType')
        search_str = json.loads(request.body).get('searchText')

        if qt == "Phone":
            patient = Patient.objects.all().filter(Phone__istartswith=search_str)  # return list of qs
        elif qt == "sn":
            patient = Patient.objects.all().filter(sn__istartswith=search_str)
        elif qt == "fn":
            patient = Patient.objects.all().filter(full_name__icontains=search_str)
        if patient:
            datlist = list(patient.values())
            return JsonResponse([datlist], safe=False)
        else:
            return JsonResponse("", safe=False)