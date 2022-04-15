from django import forms
from django.forms import NumberInput

from crispy_forms.helper import FormHelper

PRESEN_CHOICES = (("/", "N/A"), ("CEPHALIC", "CEPHALIC"),("TRANSVERSE", "TRANSVERSE"), ("BREECH", "BREECH"), ("OBLIQUE-BREECH", "OBLIQUE-BREECH"), ("OBLIQUE-CEPHALIC", "OBLIQUE-CEPHALIC"))
NUM_FET_CHOICES = (("01", "1"),("02", "2"), ("03", "3"), (">3", "MULTIPLE"))
FET_MOV_CHOICES = (("VERY ACTIVE", "V. GOOD"),("GOOD, ACTIVE", "GOOD"), ("REDUCED MOVEMENTS", "REDUCED"), ("NO MOVEMENTS", "NONE"))
AFI_QUANTITY_CHOICES = (("NORMAL", "NORMAL"), ("REDUCED", "REDUCED"), ("OLIGOHYDRAMNIOS", "OLIGOHYDRAMNIOS"), ("POLYHYDRAMNIOS", "POLYHYDRAMNIOS"))
AFI_APPEARANCE_CHOICES = (("NORMAL (ANECHOIC)", "NORMAL"), ("TURBID ECHOES", "TURBID"))
PL_POSIT_CHOICES = (("", ""), ("POSTERIOR", "POSTERIOR"), ("ANTERIOR", "ANTERIOR"), ("FUNDAL", "FUNDAL"), ("LT LATERAL", "LT LATERAL"),
                    ("RT LATERAL", "RT LATERAL"), ("POST-FUNDAL", "POST-FUNDAL"), ("ANT-FUNDAL", "ANT-FUNDAL"))
PL_GRADE_CHOICES = (("", ""), ("GRADE 0", "GRADE 0"), ("GRADE 1", "GRADE 1"), ("GRADE 2", "GRADE 2"),
                    ("GRADE 3", "GRADE 3"))
PL_LIE_CHOICES = (("", ""), ("NOT LOW LYING", "NOT LOW LYING"), ("POST-MARGINAL", "POSTERIOR-MARGINAL"), ("ANTERIOR MARGINAL", "ANTERIOR MARGINAL"),
                  ("COMPLETE PREVIA", "COMPLETE PREVIA"))
PL_STATE_CHOICES = (("HOMOGENOUS", "HOMOGENOUS"), ("HETEROGENOUS", "HETEROGENOUS"))
BPS_CHOICES = (("", ""), ("2", "2"), ("1", "1"), ("0", "0"))


class HeaderForm(forms.Form):
    sn = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    un = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    book_num = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    full_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    address = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    sex = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    staff = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    presc = forms.CharField(max_length=20, required=False, label="Prescriber")
    date_created = forms.DateField(widget=NumberInput(attrs={'type': 'date', 'readonly': 'readonly'}))
    age = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True)
    phone = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    indic = forms.CharField(max_length=30, required=False, label="Indication")


class ObstetricForm(HeaderForm):
    lmp = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="LMP")
    numfet = forms.ChoiceField(choices=NUM_FET_CHOICES, required=False, label="Number of Fetus")
    presen = forms.ChoiceField(choices=PRESEN_CHOICES, required=False, label="Presentation / Lie")
    fhr = forms.CharField(max_length=3, required=True, label="Hetal Hear Rate")
    fetmov1 = forms.ChoiceField(choices=FET_MOV_CHOICES, required=True, label="Fetal Movements")
    fetmov2 = forms.CharField(max_length=37, required=False, label="More Fetal Movements")
    afi1 = forms.CharField(max_length=4, required=True, label="AFI")
    afi2 = forms.ChoiceField(choices=AFI_QUANTITY_CHOICES, required=False, label="AFI-QUANTITY")
    appearance = forms.ChoiceField(choices=AFI_APPEARANCE_CHOICES, required=False, label="AFI APPEARANCE")
    afi3 = forms.CharField(max_length=40, required=True, label="More Afi")

    gs1 = forms.CharField(max_length=4, required=False, label="GS - A")
    crl1 = forms.CharField(max_length=4, required=False, label="CRL - A")
    bpd1 = forms.CharField(max_length=5, required=False, label="BPD - A")
    hc1 = forms.CharField(max_length=5, required=False, label="HC - A")
    ac1 = forms.CharField(max_length=5, required=False, label="AC - A")
    fl1 = forms.CharField(max_length=4, required=False, label="FL - A")

    gs2 = forms.CharField(max_length=4, required=False, label="GS - B")
    crl2 = forms.CharField(max_length=4, required=False, label="CRL - B")
    bpd2 = forms.CharField(max_length=5, required=False, label="BPD - B")
    hc2 = forms.CharField(max_length=5, required=False, label="HC - B")
    ac2 = forms.CharField(max_length=5, required=False, label="AC - B")
    fl2 = forms.CharField(max_length=4, required=False, label="FL - B")

    gs3 = forms.CharField(max_length=4, required=False, label="GS - C")
    crl3 = forms.CharField(max_length=4, required=False, label="CRL - C")
    bpd3 = forms.CharField(max_length=5, required=False, label="BPD - C")
    hc3 = forms.CharField(max_length=5, required=False, label="HC - C")
    ac3 = forms.CharField(max_length=5, required=False, label="AC - C")
    fl3 = forms.CharField(max_length=4, required=False, label="FL - C")

    ga1 = forms.CharField(max_length=2, required=True, label="GA Weeks")
    ga2 = forms.CharField(max_length=1, required=True, label="GA Days")
    edd = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="Expected Date of Delivery")
    efwa1 = forms.CharField(max_length=4, required=False, label="EFW - A")
    efwa2 = forms.CharField(max_length=3, required=False, label="+/-")
    efwb1 = forms.CharField(max_length=4, required=False, label="EFW - B")
    efwb2 = forms.CharField(max_length=3, required=False, label="+/-")

    fetnorm1 = forms.CharField(max_length=59, required=False, label="Fetal Normality")
    fetnorm2 = forms.CharField(max_length=65, required=False, label="Fet. N line2")
    placen1 = forms.ChoiceField(choices=PL_POSIT_CHOICES, required=False, label="Placenta")
    placen2 = forms.ChoiceField(choices=PL_GRADE_CHOICES, required=False, label="Grade")
    placen3 = forms.ChoiceField(choices=PL_LIE_CHOICES, required=False, label="Lie")
    placen4 = forms.ChoiceField(choices=PL_STATE_CHOICES, required=False, label="Texture")
    placen5 = forms.CharField(max_length=20, required=False, label="More Placenta")
    addcom1 = forms.CharField(max_length=45, required=False, label="Additional Comments")
    addcom2 = forms.CharField(max_length=57, required=False, label="Additional Comments line2")
    addcom3 = forms.CharField(max_length=57, required=False, label="Additional Comments line3")

    bps1 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Posture/Tone")
    bps2 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Fetal Movements")
    bps3 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Breathing Movements")
    bps4 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Quantitative AF Volume")
    bps5 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Fetal Heart (NST)")
    bpst = forms.CharField(max_length=2, required=False, label="BPS Total")

    imp1 = forms.CharField(max_length=42, required=False, label="Impression1")
    imp2 = forms.CharField(max_length=42, required=False, label="Impression2")
    imp3 = forms.CharField(max_length=42, required=False, label="Impression3")
    imp4 = forms.CharField(max_length=42, required=False, label="Impression4")

    class Meta:
        fields = "__all__"


class AbdominalForm(HeaderForm):
    lmp = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="LMP")
    numfet = forms.ChoiceField(choices=NUM_FET_CHOICES, required=False, label="Number of Fetus")
    presen = forms.ChoiceField(choices=PRESEN_CHOICES, required=False, label="Presentation / Lie")
    fhr = forms.CharField(max_length=3, required=True, label="Hetal Hear Rate")
    fetmov1 = forms.ChoiceField(choices=FET_MOV_CHOICES, required=True, label="Fetal Movements")
    fetmov2 = forms.CharField(max_length=37, required=False, label="More Fetal Movements")
    afi1 = forms.CharField(max_length=4, required=True, label="AFI")
    afi2 = forms.ChoiceField(choices=AFI_QUANTITY_CHOICES, required=False, label="AFI-QUANTITY")
    appearance = forms.ChoiceField(choices=AFI_APPEARANCE_CHOICES, required=False, label="AFI APPEARANCE")
    afi3 = forms.CharField(max_length=40, required=True, label="More Afi")

    gs1 = forms.CharField(max_length=4, required=False, label="GS - A")
    crl1 = forms.CharField(max_length=4, required=False, label="CRL - A")
    bpd1 = forms.CharField(max_length=5, required=False, label="BPD - A")
    hc1 = forms.CharField(max_length=5, required=False, label="HC - A")
    ac1 = forms.CharField(max_length=5, required=False, label="AC - A")
    fl1 = forms.CharField(max_length=4, required=False, label="FL - A")

    gs2 = forms.CharField(max_length=4, required=False, label="GS - B")
    crl2 = forms.CharField(max_length=4, required=False, label="CRL - B")
    bpd2 = forms.CharField(max_length=5, required=False, label="BPD - B")
    hc2 = forms.CharField(max_length=5, required=False, label="HC - B")
    ac2 = forms.CharField(max_length=5, required=False, label="AC - B")
    fl2 = forms.CharField(max_length=4, required=False, label="FL - B")

    gs3 = forms.CharField(max_length=4, required=False, label="GS - C")
    crl3 = forms.CharField(max_length=4, required=False, label="CRL - C")
    bpd3 = forms.CharField(max_length=5, required=False, label="BPD - C")
    hc3 = forms.CharField(max_length=5, required=False, label="HC - C")
    ac3 = forms.CharField(max_length=5, required=False, label="AC - C")
    fl3 = forms.CharField(max_length=4, required=False, label="FL - C")

    ga1 = forms.CharField(max_length=2, required=True, label="GA Weeks")
    ga2 = forms.CharField(max_length=1, required=True, label="GA Days")
    edd = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="Expected Date of Delivery")
    efwa1 = forms.CharField(max_length=4, required=False, label="EFW - A")
    efwa2 = forms.CharField(max_length=3, required=False, label="+/-")
    efwb1 = forms.CharField(max_length=4, required=False, label="EFW - B")
    efwb2 = forms.CharField(max_length=3, required=False, label="+/-")

    fetnorm1 = forms.CharField(max_length=59, required=False, label="Fetal Normality")
    fetnorm2 = forms.CharField(max_length=65, required=False, label="Fet. N line2")
    placen1 = forms.ChoiceField(choices=PL_POSIT_CHOICES, required=False, label="Placenta")
    placen2 = forms.ChoiceField(choices=PL_GRADE_CHOICES, required=False, label="Grade")
    placen3 = forms.ChoiceField(choices=PL_LIE_CHOICES, required=False, label="Lie")
    placen4 = forms.ChoiceField(choices=PL_STATE_CHOICES, required=False, label="Texture")
    placen5 = forms.CharField(max_length=20, required=False, label="More Placenta")
    addcom1 = forms.CharField(max_length=45, required=False, label="Additional Comments")
    addcom2 = forms.CharField(max_length=57, required=False, label="Additional Comments line2")
    addcom3 = forms.CharField(max_length=57, required=False, label="Additional Comments line3")

    bps1 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Posture/Tone")
    bps2 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Fetal Movements")
    bps3 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Breathing Movements")
    bps4 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Quantitative AF Volume")
    bps5 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Fetal Heart (NST)")
    bpst = forms.CharField(max_length=2, required=False, label="BPS Total")

    imp1 = forms.CharField(max_length=42, required=False, label="Impression1")
    imp2 = forms.CharField(max_length=42, required=False, label="Impression2")
    imp3 = forms.CharField(max_length=42, required=False, label="Impression3")
    imp4 = forms.CharField(max_length=42, required=False, label="Impression4")

    class Meta:
        fields = "__all__"


class FPelvicForm(HeaderForm):
    lmp = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="LMP")
    numfet = forms.ChoiceField(choices=NUM_FET_CHOICES, required=False, label="Number of Fetus")
    presen = forms.ChoiceField(choices=PRESEN_CHOICES, required=False, label="Presentation / Lie")
    fhr = forms.CharField(max_length=3, required=True, label="Hetal Hear Rate")
    fetmov1 = forms.ChoiceField(choices=FET_MOV_CHOICES, required=True, label="Fetal Movements")
    fetmov2 = forms.CharField(max_length=37, required=False, label="More Fetal Movements")
    afi1 = forms.CharField(max_length=4, required=True, label="AFI")
    afi2 = forms.ChoiceField(choices=AFI_QUANTITY_CHOICES, required=False, label="AFI-QUANTITY")
    appearance = forms.ChoiceField(choices=AFI_APPEARANCE_CHOICES, required=False, label="AFI APPEARANCE")
    afi3 = forms.CharField(max_length=40, required=True, label="More Afi")

    gs1 = forms.CharField(max_length=4, required=False, label="GS - A")
    crl1 = forms.CharField(max_length=4, required=False, label="CRL - A")
    bpd1 = forms.CharField(max_length=5, required=False, label="BPD - A")
    hc1 = forms.CharField(max_length=5, required=False, label="HC - A")
    ac1 = forms.CharField(max_length=5, required=False, label="AC - A")
    fl1 = forms.CharField(max_length=4, required=False, label="FL - A")

    gs2 = forms.CharField(max_length=4, required=False, label="GS - B")
    crl2 = forms.CharField(max_length=4, required=False, label="CRL - B")
    bpd2 = forms.CharField(max_length=5, required=False, label="BPD - B")
    hc2 = forms.CharField(max_length=5, required=False, label="HC - B")
    ac2 = forms.CharField(max_length=5, required=False, label="AC - B")
    fl2 = forms.CharField(max_length=4, required=False, label="FL - B")

    gs3 = forms.CharField(max_length=4, required=False, label="GS - C")
    crl3 = forms.CharField(max_length=4, required=False, label="CRL - C")
    bpd3 = forms.CharField(max_length=5, required=False, label="BPD - C")
    hc3 = forms.CharField(max_length=5, required=False, label="HC - C")
    ac3 = forms.CharField(max_length=5, required=False, label="AC - C")
    fl3 = forms.CharField(max_length=4, required=False, label="FL - C")

    ga1 = forms.CharField(max_length=2, required=True, label="GA Weeks")
    ga2 = forms.CharField(max_length=1, required=True, label="GA Days")
    edd = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="Expected Date of Delivery")
    efwa1 = forms.CharField(max_length=4, required=False, label="EFW - A")
    efwa2 = forms.CharField(max_length=3, required=False, label="+/-")
    efwb1 = forms.CharField(max_length=4, required=False, label="EFW - B")
    efwb2 = forms.CharField(max_length=3, required=False, label="+/-")

    fetnorm1 = forms.CharField(max_length=59, required=False, label="Fetal Normality")
    fetnorm2 = forms.CharField(max_length=65, required=False, label="Fet. N line2")
    placen1 = forms.ChoiceField(choices=PL_POSIT_CHOICES, required=False, label="Placenta")
    placen2 = forms.ChoiceField(choices=PL_GRADE_CHOICES, required=False, label="Grade")
    placen3 = forms.ChoiceField(choices=PL_LIE_CHOICES, required=False, label="Lie")
    placen4 = forms.ChoiceField(choices=PL_STATE_CHOICES, required=False, label="Texture")
    placen5 = forms.CharField(max_length=20, required=False, label="More Placenta")
    addcom1 = forms.CharField(max_length=45, required=False, label="Additional Comments")
    addcom2 = forms.CharField(max_length=57, required=False, label="Additional Comments line2")
    addcom3 = forms.CharField(max_length=57, required=False, label="Additional Comments line3")

    bps1 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Posture/Tone")
    bps2 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Fetal Movements")
    bps3 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Breathing Movements")
    bps4 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Quantitative AF Volume")
    bps5 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Fetal Heart (NST)")
    bpst = forms.CharField(max_length=2, required=False, label="BPS Total")

    imp1 = forms.CharField(max_length=42, required=False, label="Impression1")
    imp2 = forms.CharField(max_length=42, required=False, label="Impression2")
    imp3 = forms.CharField(max_length=42, required=False, label="Impression3")
    imp4 = forms.CharField(max_length=42, required=False, label="Impression4")

    class Meta:
        fields = "__all__"


class MPelvicForm(HeaderForm):
    lmp = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="LMP")
    numfet = forms.ChoiceField(choices=NUM_FET_CHOICES, required=False, label="Number of Fetus")
    presen = forms.ChoiceField(choices=PRESEN_CHOICES, required=False, label="Presentation / Lie")
    fhr = forms.CharField(max_length=3, required=True, label="Hetal Hear Rate")
    fetmov1 = forms.ChoiceField(choices=FET_MOV_CHOICES, required=True, label="Fetal Movements")
    fetmov2 = forms.CharField(max_length=37, required=False, label="More Fetal Movements")
    afi1 = forms.CharField(max_length=4, required=True, label="AFI")
    afi2 = forms.ChoiceField(choices=AFI_QUANTITY_CHOICES, required=False, label="AFI-QUANTITY")
    appearance = forms.ChoiceField(choices=AFI_APPEARANCE_CHOICES, required=False, label="AFI APPEARANCE")
    afi3 = forms.CharField(max_length=40, required=True, label="More Afi")

    gs1 = forms.CharField(max_length=4, required=False, label="GS - A")
    crl1 = forms.CharField(max_length=4, required=False, label="CRL - A")
    bpd1 = forms.CharField(max_length=5, required=False, label="BPD - A")
    hc1 = forms.CharField(max_length=5, required=False, label="HC - A")
    ac1 = forms.CharField(max_length=5, required=False, label="AC - A")
    fl1 = forms.CharField(max_length=4, required=False, label="FL - A")

    gs2 = forms.CharField(max_length=4, required=False, label="GS - B")
    crl2 = forms.CharField(max_length=4, required=False, label="CRL - B")
    bpd2 = forms.CharField(max_length=5, required=False, label="BPD - B")
    hc2 = forms.CharField(max_length=5, required=False, label="HC - B")
    ac2 = forms.CharField(max_length=5, required=False, label="AC - B")
    fl2 = forms.CharField(max_length=4, required=False, label="FL - B")

    gs3 = forms.CharField(max_length=4, required=False, label="GS - C")
    crl3 = forms.CharField(max_length=4, required=False, label="CRL - C")
    bpd3 = forms.CharField(max_length=5, required=False, label="BPD - C")
    hc3 = forms.CharField(max_length=5, required=False, label="HC - C")
    ac3 = forms.CharField(max_length=5, required=False, label="AC - C")
    fl3 = forms.CharField(max_length=4, required=False, label="FL - C")

    ga1 = forms.CharField(max_length=2, required=True, label="GA Weeks")
    ga2 = forms.CharField(max_length=1, required=True, label="GA Days")
    edd = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="Expected Date of Delivery")
    efwa1 = forms.CharField(max_length=4, required=False, label="EFW - A")
    efwa2 = forms.CharField(max_length=3, required=False, label="+/-")
    efwb1 = forms.CharField(max_length=4, required=False, label="EFW - B")
    efwb2 = forms.CharField(max_length=3, required=False, label="+/-")

    fetnorm1 = forms.CharField(max_length=59, required=False, label="Fetal Normality")
    fetnorm2 = forms.CharField(max_length=65, required=False, label="Fet. N line2")
    placen1 = forms.ChoiceField(choices=PL_POSIT_CHOICES, required=False, label="Placenta")
    placen2 = forms.ChoiceField(choices=PL_GRADE_CHOICES, required=False, label="Grade")
    placen3 = forms.ChoiceField(choices=PL_LIE_CHOICES, required=False, label="Lie")
    placen4 = forms.ChoiceField(choices=PL_STATE_CHOICES, required=False, label="Texture")
    placen5 = forms.CharField(max_length=20, required=False, label="More Placenta")
    addcom1 = forms.CharField(max_length=45, required=False, label="Additional Comments")
    addcom2 = forms.CharField(max_length=57, required=False, label="Additional Comments line2")
    addcom3 = forms.CharField(max_length=57, required=False, label="Additional Comments line3")

    bps1 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Posture/Tone")
    bps2 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Fetal Movements")
    bps3 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Breathing Movements")
    bps4 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Quantitative AF Volume")
    bps5 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Fetal Heart (NST)")
    bpst = forms.CharField(max_length=2, required=False, label="BPS Total")

    imp1 = forms.CharField(max_length=42, required=False, label="Impression1")
    imp2 = forms.CharField(max_length=42, required=False, label="Impression2")
    imp3 = forms.CharField(max_length=42, required=False, label="Impression3")
    imp4 = forms.CharField(max_length=42, required=False, label="Impression4")

    class Meta:
        fields = "__all__"


class SmallPartsForm(HeaderForm):
    lmp = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="LMP")
    numfet = forms.ChoiceField(choices=NUM_FET_CHOICES, required=False, label="Number of Fetus")
    presen = forms.ChoiceField(choices=PRESEN_CHOICES, required=False, label="Presentation / Lie")
    fhr = forms.CharField(max_length=3, required=True, label="Hetal Hear Rate")
    fetmov1 = forms.ChoiceField(choices=FET_MOV_CHOICES, required=True, label="Fetal Movements")
    fetmov2 = forms.CharField(max_length=37, required=False, label="More Fetal Movements")
    afi1 = forms.CharField(max_length=4, required=True, label="AFI")
    afi2 = forms.ChoiceField(choices=AFI_QUANTITY_CHOICES, required=False, label="AFI-QUANTITY")
    appearance = forms.ChoiceField(choices=AFI_APPEARANCE_CHOICES, required=False, label="AFI APPEARANCE")
    afi3 = forms.CharField(max_length=40, required=True, label="More Afi")

    gs1 = forms.CharField(max_length=4, required=False, label="GS - A")
    crl1 = forms.CharField(max_length=4, required=False, label="CRL - A")
    bpd1 = forms.CharField(max_length=5, required=False, label="BPD - A")
    hc1 = forms.CharField(max_length=5, required=False, label="HC - A")
    ac1 = forms.CharField(max_length=5, required=False, label="AC - A")
    fl1 = forms.CharField(max_length=4, required=False, label="FL - A")

    gs2 = forms.CharField(max_length=4, required=False, label="GS - B")
    crl2 = forms.CharField(max_length=4, required=False, label="CRL - B")
    bpd2 = forms.CharField(max_length=5, required=False, label="BPD - B")
    hc2 = forms.CharField(max_length=5, required=False, label="HC - B")
    ac2 = forms.CharField(max_length=5, required=False, label="AC - B")
    fl2 = forms.CharField(max_length=4, required=False, label="FL - B")

    gs3 = forms.CharField(max_length=4, required=False, label="GS - C")
    crl3 = forms.CharField(max_length=4, required=False, label="CRL - C")
    bpd3 = forms.CharField(max_length=5, required=False, label="BPD - C")
    hc3 = forms.CharField(max_length=5, required=False, label="HC - C")
    ac3 = forms.CharField(max_length=5, required=False, label="AC - C")
    fl3 = forms.CharField(max_length=4, required=False, label="FL - C")

    ga1 = forms.CharField(max_length=2, required=True, label="GA Weeks")
    ga2 = forms.CharField(max_length=1, required=True, label="GA Days")
    edd = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="Expected Date of Delivery")
    efwa1 = forms.CharField(max_length=4, required=False, label="EFW - A")
    efwa2 = forms.CharField(max_length=3, required=False, label="+/-")
    efwb1 = forms.CharField(max_length=4, required=False, label="EFW - B")
    efwb2 = forms.CharField(max_length=3, required=False, label="+/-")

    fetnorm1 = forms.CharField(max_length=59, required=False, label="Fetal Normality")
    fetnorm2 = forms.CharField(max_length=65, required=False, label="Fet. N line2")
    placen1 = forms.ChoiceField(choices=PL_POSIT_CHOICES, required=False, label="Placenta")
    placen2 = forms.ChoiceField(choices=PL_GRADE_CHOICES, required=False, label="Grade")
    placen3 = forms.ChoiceField(choices=PL_LIE_CHOICES, required=False, label="Lie")
    placen4 = forms.ChoiceField(choices=PL_STATE_CHOICES, required=False, label="Texture")
    placen5 = forms.CharField(max_length=20, required=False, label="More Placenta")
    addcom1 = forms.CharField(max_length=45, required=False, label="Additional Comments")
    addcom2 = forms.CharField(max_length=57, required=False, label="Additional Comments line2")
    addcom3 = forms.CharField(max_length=57, required=False, label="Additional Comments line3")

    bps1 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Posture/Tone")
    bps2 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Fetal Movements")
    bps3 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Breathing Movements")
    bps4 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Quantitative AF Volume")
    bps5 = forms.ChoiceField(choices=BPS_CHOICES, required=False, label="Fetal Heart (NST)")
    bpst = forms.CharField(max_length=2, required=False, label="BPS Total")

    imp1 = forms.CharField(max_length=42, required=False, label="Impression1")
    imp2 = forms.CharField(max_length=42, required=False, label="Impression2")
    imp3 = forms.CharField(max_length=42, required=False, label="Impression3")
    imp4 = forms.CharField(max_length=42, required=False, label="Impression4")

    class Meta:
        fields = "__all__"


class DopplerForm(HeaderForm):
    lmp = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="LMP")


class CardiacForm(HeaderForm):
    lmp = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label="LMP")