from django import forms
from django.forms import NumberInput

from .models import *
import datetime


class RegPatientForm(forms.ModelForm):
    reg_num = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'id': 'id_reg_num_reg', 'style': 'width:8ch'}))
    reg_num2 = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'id': 'id_reg_num_reg2', 'hidden': 'hidden'}), label='')
    first_name = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'id': 'id_first_name_reg'}))
    last_name = forms.CharField(max_length=12, required=False, widget=forms.TextInput(attrs={'id': 'id_last_name_reg'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'hidden': 'hidden'}),
                                initial='full name', required=False, label='')
    address = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'id': 'id_address_reg'}))
    # sex = forms.CharField(attrs={'id': 'id_sex'})
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date', 'id': 'id_dob_reg'}))
    age = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_age_reg', 'readonly': 'readonly'}),
                          initial="", required=False, label='')      # 'hidden': 'hidden'})
    Phone = forms.CharField(max_length=9, required=False, widget=forms.TextInput(attrs={'id': 'id_phone_reg'}))

    class Meta:
        model = Patient
        fields = ['reg_num', 'first_name', 'last_name', 'address', 'sex', 'dob', 'age', 'Phone', 'full_name']


class RegiStaffForm(forms.ModelForm):
    class Meta:
        model = RegiStaff
        fields = "__all__"