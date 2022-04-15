from django import forms
from .models import *
from crispy_forms.helper import FormHelper
import datetime


class LaboPatientForm(forms.ModelForm):
    class Meta:
        model = LaboPatient
        fields = "__all__"


class LaboExamForm(forms.ModelForm):
    class Meta:
        model = LaboExam
        fields = "__all__"
        exclude = ["labo_type"]


class LaboExamItemForm(forms.ModelForm):
    class Meta:
        model = LaboExamItem
        fields = "__all__"


class LaboFindingForm(forms.ModelForm):
    class Meta:
        model = LaboFinding
        fields = "__all__"


class LaboTestCategoryForm(forms.ModelForm):
    class Meta:
        model = LaboTestCategory
        fields = "__all__"


class LaboTestTypeForm(forms.ModelForm):
    class Meta:
        model = LaboTestType
        fields = "__all__"


class LaboStaffForm(forms.ModelForm):
    class Meta:
        model = LaboStaff
        fields = "__all__"