from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.regi.models import Patient
from apps.labo.models import *


class LaboStaffSerializer(ModelSerializer):
    class Meta:
        model = LaboStaff
        fields = '__all__'


class LaboPatientSerializer(ModelSerializer):
    class Meta:
        model = LaboPatient
        fields = '__all__'
        dept = 2


class LaboExamSerializer(ModelSerializer):
    class Meta:
        model = LaboExam
        fields = '__all__'
        depth = 1


class LaboTypeSerializer(ModelSerializer):
    class Meta:
        model = LaboTestType
        fields = '__all__'
        depth = 1


class LaboExamItemSerializer(ModelSerializer):
    class Meta:
        model = LaboExamItem
        fields = '__all__'
        dept = 1


class LaboFindingSerializer(ModelSerializer):
    class Meta:
        model = LaboFinding
        fields = '__all__'
        dept = 1