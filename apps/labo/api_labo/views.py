# from apps.labo.models import LaboPatient, LaboExam, LaboType
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from apps.labo.api_labo.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets


# ================== API CBVs ======================
class LaboPatientList(APIView):
    def get(self, request, format=None):            # List Lab Patients
        lpatients = LaboPatient.objects.all()
        serializer = LaboPatientSerializer(lpatients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):           # Create Lap Patients
        serializer = LaboPatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LaboPatientDetail(APIView):

    def get_object(self, ln):
        try:
            return LaboPatient.objects.get(ln=ln)
        except LaboPatient.DoesNotExist:
            #raise Http404
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, ln, format=None):
        lpatient = self.get_object(ln)
        serializer = LaboPatientSerializer(lpatient)
        return Response(serializer.data)

    def put(self, request, ln, format=None):
        lpatient = self.get_object(ln)
        serializer = LaboPatientSerializer(lpatient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ln, format=None):
        lpatient = self.get_object(ln)
        lpatient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LaboExamListAll(APIView):
    def get(self, request, format=None):            # List Lab Patients
        lexam = LaboExam.objects.all()
        serializer = LaboExamSerializer(lexam, many=True)
        return Response(serializer.data)


class LaboExamListOne(APIView):
    def get(self, request, patient, format=None):            # List Lab Patients
        lexams = LaboExam.objects.filter(patient=patient)
        serializer = LaboExamSerializer(lexams, many=True)
        return Response([serializer.data,])

    def post(self, request, format=None):           # Create Lap Exam
        serializer = LaboExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LaboExamDetail(APIView):

    def get_object(self, id):
        try:
            return LaboExam.objects.get(id=id)
        except LaboExam.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        lexam = self.get_object(id)
        serializer = LaboExamSerializer(lexam)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        lexam = self.get_object(id)
        serializer = LaboExamSerializer(lexam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ys, format=None):
        lexam = self.get_object(ys)
        lexam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LaboResultListAll(APIView):
    def get(self, request, format=None):            # List Lab Patients
        lresult = LaboResult.objects.all()
        serializer = LaboResultSerializer(lresult, many=True)
        return Response(serializer.data)


class LaboResultListOne(APIView):
    def get(self, request, lexam, format=None):            # List Lab Patients
        lresult = LaboResult.objects.all()
        lresultone = lresult.filter(lexam=lexam)
        serializer = LaboResultSerializer(lresultone, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):           # Create Lap Patients
        serializer = LaboExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LaboResultDetail(APIView):

    def get_object(self, id):
        try:
            return LaboResult.objects.get(id=id)
        except LaboResult.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        lresultone = self.get_object(id)
        serializer = LaboResultSerializer(lresultone)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        lexam = self.get_object(id)
        serializer = LaboExamSerializer(lexam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("updated")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        lexam = self.get_object(id)
        lexam.delete()
        print("deleted")
        return Response(status=status.HTTP_204_NO_CONTENT)
