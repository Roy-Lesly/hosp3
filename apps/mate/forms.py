from django import forms
from .models import *
from crispy_forms.helper import FormHelper
import datetime


class MateStaffForm(forms.ModelForm):
    class Meta:
        model = MateStaff
        fields = "__all__"