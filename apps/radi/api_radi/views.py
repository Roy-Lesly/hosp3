from apps.radi.models import *
from apps.radi.api_radi.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# ____________ Echo Views ___________________

class UPatientList(APIView):
    def get(self, request, format=None):            # List Lab Patients
        upatients = UPatient.objects.all()
        serializer = UPatientSerializer(upatients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):           # Create Lap Patients
        serializer = UPatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UPatientDetail(APIView):

    def get_object(self, un):
        try:
            return UPatient.objects.get(un=un)
        except UPatient.DoesNotExist:
            raise Http404

    def get(self, request, un, format=None):
        upatient = self.get_object(un)
        serializer = UPatientSerializer(upatient)
        return Response(serializer.data)

    def put(self, request, un, format=None):
        upatient = self.get_object(un)
        serializer = UPatientSerializer(upatient, data=request.data)
        if serializer.is_vauid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, un, format=None):
        upatient = self.get_object(un)
        upatient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UExamListAll(APIView):
    def get(self, request, format=None):            # List Lab Patients
        lexam = UExam.objects.all()
        serializer = UExamSerializer(lexam, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):           # Create Lap Patients
        serializer = UExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UExamListOne(APIView):
    def get(self, request, patient, format=None):            # List Lab Patients
        uexam = UExam.objects.all()
        uexamone = uexam.filter(patient=patient)
        print(uexamone)
        print(uexam)
        e_list = {}
        t_list = []
        list = []
        for e in uexamone:
            print('x')
            upat = e.patient.patient.first_name
            type = e.labo_type.all()
            for t in type:
                t_list.append(t)
                list.append(t)
            e_list.update({upat: t_list})
        print(e_list)
        print("____________")
        print(list)
        #print(lexam)
        serializer = UExamSerializer(uexamone, many=True)
        #serializer2 = UTypeSerializer(list, many=True)
        return Response(serializer.data)#, serializer2.data ])

    def post(self, request, format=None):           # Create Lap Patients
        serializer = UExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UExamDetail(APIView):

    def get_object(self, us):
        try:
            return UFinding.objects.get(us=us)
        except UExam.DoesNotExist:
            raise Http404

    def get(self, request, ys, format=None):
        uexam = self.get_object(ys)
        serializer = UExamSerializer(uexam)
        return Response(serializer.data)

    def put(self, request, us, format=None):
        uexam = self.get_object(us)
        serializer = UExamSerializer(uexam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, us, format=None):
        uexam = self.get_object(us)
        uexam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UResultListAll(APIView):
    def get(self, request, format=None):            # List Lab Patients
        uresult = UFinding.objects.all()
        serializer = UResultSerializer(uresult, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):           # Create Lap Patients
        serializer = UExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UResultListOne(APIView):
    def get(self, request, uexam, format=None):            # List Lab Patients
        uresult = UFinding.objects.all()
        uresultone = uresult.filter(uexam=uexam)
        serializer = UResultSerializer(uresultone, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):           # Create Lap Patients
        serializer = UExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UResultDetail(APIView):

    def get_object(self, id):
        try:
            return UFinding.objects.get(id=id)
        except UFinding.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        lresultone = self.get_object(id)
        serializer = UResultSerializer(lresultone)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        uexam = self.get_object(id)
        serializer = UExamSerializer(uexam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("updated")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        uexam = self.get_object(id)
        uexam.delete()
        print("deleted")
        return Response(status=status.HTTP_204_NO_CONTENT)


# ____________ XRAY Views ___________________

class XPatientList(APIView):
    def get(self, request, format=None):            # List Lab Patients
        xpatients = XPatient.objects.all()
        serializer = XPatientSerializer(xpatients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):           # Create Lap Patients
        serializer = XPatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class XPatientDetail(APIView):

    def get_object(self, xn):
        try:
            return XPatient.objects.get(xn=xn)
        except XPatient.DoesNotExist:
            raise Http404

    def get(self, request, xn, format=None):
        xpatient = self.get_object(xn)
        serializer = XPatientSerializer(xpatient)
        return Response(serializer.data)

    def put(self, request, xn, format=None):
        xpatient = self.get_object(xn)
        serializer = UPatientSerializer(xpatient, data=request.data)
        if serializer.is_vauid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, un, format=None):
        upatient = self.get_object(un)
        upatient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class XExamListAll(APIView):
    def get(self, request, format=None):            # List Lab Patients
        xexam = UExam.objects.all()
        serializer = UExamSerializer(xexam, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):           # Create Lap Patients
        serializer = UExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class XExamListOne(APIView):
    def get(self, request, patient, format=None):            # List Lab Patients
        xexam = UExam.objects.all()
        xexamone = xexam.filter(patient=patient)
        print(xexamone)
        print(xexam)
        e_list = {}
        t_list = []
        list = []
        for e in xexamone:
            print('x')
            xpat = e.patient.patient.first_name
            type = e.labo_type.all()
            for t in type:
                t_list.append(t)
                list.append(t)
            e_list.update({xpat: t_list})
        print(e_list)
        print("____________")
        print(list)
        #print(lexam)
        serializer = UExamSerializer(xexamone, many=True)
        #serializer2 = UTypeSerializer(list, many=True)
        return Response(serializer.data)#, serializer2.data ])

    def post(self, request, format=None):           # Create Lap Patients
        serializer = UExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class XExamDetail(APIView):

    def get_object(self, xs):
        try:
            return XFinding.objects.get(xs=xs)
        except XExam.DoesNotExist:
            raise Http404

    def get(self, request, xs, format=None):
        xexam = self.get_object(xs)
        serializer = XExamSerializer(xexam)
        return Response(serializer.data)

    def put(self, request, xs, format=None):
        xexam = self.get_object(xs)
        serializer = XExamSerializer(xexam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, xs, format=None):
        xexam = self.get_object(xs)
        xexam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class XResultListAll(APIView):
    def get(self, request, format=None):            # List Lab Patients
        xresult = XFinding.objects.all()
        serializer = UResultSerializer(xresult, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):           # Create Lap Patients
        serializer = XExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class XResultListOne(APIView):
    def get(self, request, xexam, format=None):            # List Lab Patients
        xresult = XFinding.objects.all()
        xresultone = xresult.filter(xexam=xexam)
        serializer = XFindingSerializer(xresultone, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):           # Create Lap Patients
        serializer = XExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class XResultDetail(APIView):

    def get_object(self, id):
        try:
            return XFinding.objects.get(id=id)
        except XFindingSerializer.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        xresultone = self.get_object(id)
        serializer = XFindingSerializer(xresultone)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        xexam = self.get_object(id)
        serializer = XExamSerializer(xexam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("updated")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        xexam = self.get_object(id)
        xexam.delete()
        print("deleted")
        return Response(status=status.HTTP_204_NO_CONTENT)