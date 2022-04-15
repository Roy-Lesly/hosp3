from django import forms
from .models import *
from crispy_forms.helper import FormHelper
import datetime


class ConsPatientForm(forms.ModelForm):
    class Meta:
        model = ConsPatient
        fields = "__all__"


class ConsStaffForm(forms.ModelForm):
    class Meta:
        model = ConsStaff
        fields = "__all__"