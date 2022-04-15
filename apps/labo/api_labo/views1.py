from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from apps.labo.api_labo.serializers import *
from apps.labo.models import *
from rest_framework.response import Response
from rest_framework import status


# ================== API FBVs (No Rest Interface)======================
def labo_patient_list(request):

    if request.method == 'GET':
        lp = LaboPatient.objects.all()
        serializer = LaboPatientSerializer(lp, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LaboPatientSerializer(data=data)

        if serializer.is_valid():
            serializer.safe()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def labo_patient_detail(request, ln):

    try:
        lpatient = LaboPatient.objects.get(ln=ln)
    except LaboPatient.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LaboPatientSerializer(lpatient)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LaboPatientSerializer(lpatient, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        lpatient.delete()
        return HttpResponse(status=204)


def labo_exam_list_all(request):

    if request.method == 'GET':
        lexams = LaboExam.objects.all()
        serializer = LaboExamSerializer(lexams, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LaboExamSerializer(data=data)

        if serializer.is_valid():
            serializer.safe()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def labo_exam_list_one(request, patient):

    try:
        lexams = LaboExam.objects.filter(patient=patient)
    except LaboPatient.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LaboExamSerializer(lexams, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def labo_exam_detail(request, id):

    try:
        lexam = LaboExam.objects.get(id=id)
    except LaboPatient.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LaboExamSerializer(lexam)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LaboExamSerializer(lexam, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        lexam.delete()
        return HttpResponse(status=204)


def labo_result_list(request):

    if request.method == 'GET':
        lresults = LaboResult.objects.all()
        serializer = LaboResultSerializer(lresults, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LaboResultSerializer(data=data)

        if serializer.is_valid():
            serializer.safe()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def labo_result_list_one(request, lexam):

    try:
        lresult = LaboResult.objects.filter(lexam=lexam)
    except LaboPatient.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LaboResultSerializer(lresult, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def labo_result_detail(request, id):

    try:
        lresult = LaboResult.objects.get(id=id)
    except LaboResult.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LaboResultSerializer(lresult)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LaboResultSerializer(lresult, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        lresult.delete()
        return HttpResponse(status=204)


# ================ API FBVs (with Rest Interface) ===================
@api_view(['GET', 'POST'])
def labo_patient_list_1(request):

    if request.method == 'GET':
        lpatients = LaboPatient.objects.all()
        serializer = LaboPatientSerializer(lpatients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LaboPatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.safe()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def labo_patient_detail_1(request, ln):

    try:
        lpatient = LaboPatient.objects.get(ln=ln)
    except LaboPatient.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LaboPatientSerializer(lpatient)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LaboPatientSerializer(lpatient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lpatient.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def labo_exam_list_all_1(request):

    if request.method == 'GET':
        lexams = LaboExam.objects.all()
        serializer = LaboExamSerializer(lexams, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LaboExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.safe()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def labo_exam_list_one_1(request, patient):

    try:
        lexams = LaboExam.objects.filter(patient=patient)
    except LaboPatient.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LaboExamSerializer(lexams, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def labo_exam_detail_1(request, id):

    try:
        lexam = LaboExam.objects.get(id=id)
    except LaboPatient.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LaboExamSerializer(lexam)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LaboExamSerializer(lexam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lexam.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def labo_result_list_1(request):

    if request.method == 'GET':
        lresults = LaboResult.objects.all()
        serializer = LaboResultSerializer(lresults, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LaboResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.safe()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def labo_result_list_one_1(request, lexam):

    try:
        lresult = LaboResult.objects.filter(lexam=lexam)
    except LaboPatient.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = LaboResultSerializer(lresult, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def labo_result_detail_1(request, id):

    try:
        lresult = LaboResult.objects.get(id=id)
    except LaboResult.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LaboResultSerializer(lresult)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LaboResultSerializer(lresult, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lresult.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

