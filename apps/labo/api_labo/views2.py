# from apps.labo.models import LaboPatient, LaboExam, LaboType
from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from apps.labo.api_labo.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins, generics


# ================== GENERIC VIEWS (Using MIXINS) ======================
class GenericLaboPatAPIView(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):

    serializer_class = LaboPatientSerializer
    queryset = LaboPatient.objects.all()
    lookup_field = 'ln'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, ln=None):        # List and Retrieve

        if ln:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):                # Create
        return self.create(request)

    def put(self, request, ln=None):                 # Update
        return self.update(request, ln)

    def delete(self, request, ln):              # Delete
        return self.destroy(request, ln)


class GenericLaboExamAPIView(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):

    serializer_class = LaboExamSerializer
    queryset = LaboExam.objects.all()
    lookup_field = 'patient'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, patient=None):       # List and Retrieve

        if patient:
            return self.retrieve(request)       # Not ok, check how to activate many=True
        else:
            return self.list(request)

    def post(self, request):                    # Create
        return self.create(request)

    def put(self, request, patient=None):       # Update
        return self.update(request, patient)

    def delete(self, request, patient):         # Delete
        return self.delete(request, patient)


class GenericLaboResultAPIView(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):

    serializer_class = LaboExamItemSerializer
    queryset = LaboExamItem.objects.all()
    lookup_field = id
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):        # List and Retrieve

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):                # Create
        return self.create(request)

    def put(self, request, id=None):                 # Update
        return self.update(request, id)

    def delete(self, request):              # Delete
        return self.delete(request, id)


# ===================== ViewSet (Using Mixins) =======================
'''class LaboPatViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = LaboPatientSerializer
    queryset = LaboPatient.objects.all()'''


# ===================== ModelViewSet (Using Mixins) =======================
class LaboPatViewSet(viewsets.ModelViewSet):
    serializer_class = LaboPatientSerializer
    queryset = LaboPatient.objects.all()