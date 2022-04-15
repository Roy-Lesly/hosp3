from django import forms
from .models import *
import datetime


class PharPatientForm(forms.ModelForm):
    class Meta:
        model = PharPatient
        fields = "__all__"


class PharStaffForm(forms.ModelForm):
    class Meta:
        model = PharStaff
        fields = "__all__"


class PharDeptForm(forms.ModelForm):
    class Meta:
        model = PharDept
        fields = "__all__"


class PharDrugCategoryForm(forms.ModelForm):
    class Meta:
        model = PharDrugCategory
        fields = "__all__"


class PharDrugTypeForm(forms.ModelForm):
    class Meta:
        model = PharDrugType
        fields = "__all__"


class PharPrescriptionForm(forms.ModelForm):
    class Meta:
        model = PharPrescription
        fields = "__all__"


class PharPrescriptionItemForm(forms.ModelForm):
    class Meta:
        model = PharPrescriptionItem
        fields = "__all__"


class PharDrugDispensedForm(forms.ModelForm):
    class Meta:
        model = PharDrugDispensed
        fields = "__all__"