from django import forms

from apps.labo.models import LaboPatient, LaboExam, LaboResult


class LaboPatientForm(forms.ModelForm):
    class Meta:
        model = LaboPatient
        fields = "__all__"


class LaboExamForm(forms.ModelForm):
    class Meta:
        model = LaboExam
        fields = "__all__"


class LaboExamForm(forms.ModelForm):
    class Meta:
        model = LaboExam
        fields = "__all__"


class LaboResultForm(forms.ModelForm):
    class Meta:
        model = LaboResult
        fields = "__all__"
