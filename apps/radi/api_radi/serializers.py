from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.regi.models import Patient
from apps.radi.models import *


class RadStaffSerializer(ModelSerializer):
    class Meta:
        model = RadiStaff
        fields = "__all__"


class UPatientSerializer(ModelSerializer):
    class Meta:
        model = UPatient
        fields = '__all__'


class UExamSerializer(ModelSerializer):
    class Meta:
        model = UExam
        fields = '__all__'


class UResultSerializer(ModelSerializer):
    class Meta:
        model = UFinding
        fields = '__all__'


class XPatientSerializer(ModelSerializer):
    class Meta:
        model = XPatient
        fields = '__all__'


class UExamSerializer(ModelSerializer):
    class Meta:
        model = UExam
        fields = '__all__'


class XExamSerializer(ModelSerializer):
    class Meta:
        model = XExam
        fields = '__all__'


class XFindingSerializer(ModelSerializer):
    class Meta:
        model = XFinding
        fields = '__all__'

