from django import forms
from django.forms import NumberInput

from .models import *


class RadiDeptForm(forms.ModelForm):
    class Meta:
        model = RadiDept
        fields = "__all__"


class RadiStaffForm(forms.ModelForm):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10, required=False)
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={'hidden': 'hidden', 'readonly': 'readonly'}), label='', required=False)
    address = forms.CharField(max_length=15)
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    age = forms.CharField(widget=forms.TextInput(
        attrs={'hidden': 'hidden', 'readonly': 'readonly'}), label='', initial=0, required=False)
    Phone = forms.CharField(max_length=9)


    class Meta:
        model = RadiStaff
        fields = "__all__"


class RadiTestCategoryForm(forms.ModelForm):
    class Meta:
        model = RadiTestCategory
        fields = "__all__"


class RadiTypeForm(forms.ModelForm):
    class Meta:
        model = RadiTestType
        fields = "__all__"


class RadiHandingForm(forms.ModelForm):
    class Meta:
        model = RadiHanding
        fields = "__all__"


class UPatientForm(forms.ModelForm):
    class Meta:
        model = UPatient
        fields = "__all__"


class XPatientForm(forms.ModelForm):
    class Meta:
        model = XPatient
        fields = "__all__"


class UExamForm(forms.ModelForm):
    class Meta:
        model = UExam
        fields = "__all__"
        exclude = ["u_exam"]


class XExamForm(forms.ModelForm):
    class Meta:
        model = XExam
        fields = "__all__"
        exclude = ["x_exam"]


class UExamItemForm(forms.ModelForm):
    class Meta:
        model = UExamItem
        fields = "__all__"


SIDES = [('None', 'N/A'), ('Right', 'Right'), ('Left', 'Left')]
POSITION = [('None', 'N/A'), ('PA', 'PA'), ('AP', 'AP'), ('oblique', 'oblique')]


class XExamItemForm(forms.ModelForm):
    side = forms.ChoiceField(choices=SIDES)
    position = forms.ChoiceField(choices=POSITION)
    class Meta:
        model = XExamItem
        fields = "__all__"


class UFindingForm(forms.ModelForm):
    class Meta:
        model = UFinding
        fields = "__all__"


class XFindingForm(forms.ModelForm):
    class Meta:
        model = XFinding
        fields = "__all__"
