import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
SEX_CHOICES = (('FEMALE', 'FEMALE'), ('MALE', 'MALE'))
WARD_CHOICES = (('', ''),
                ('OPD', 'OPD'),
                ('ANC', 'ANC'),
                ('MAT', 'Maternity'),
                ('LW', 'Labour / Delivery'),
                ('MW', 'Medical Ward'),
                ('SW', 'Surgical Ward'),
                ('CW', "Childrens' Ward"),
                ('OTHER', 'Other'))


class Exam(models.Model):
    book_num = models.CharField(max_length=10, editable=True, unique=True, primary_key=True)
    ward = models.CharField(max_length=20, choices=WARD_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    prescriber = models.CharField(max_length=15, blank=True)

    class Meta:
        abstract = True


class VitalSign(Exam):
    temp = models.CharField(max_length=7)
    bp_L = models.CharField(max_length=12)
    bp_R = models.CharField(max_length=12, blank=True)
    pulse_L = models.CharField(max_length=7)
    pulse_R = models.CharField(max_length=7, blank=True)
    satO2 = models.CharField(max_length=4)
    other = models.CharField(max_length=30, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        now = datetime.date.today()
        # self.auto_increment_ex_count()
        book_num = str(self.book_num).zfill(5) + "-" + str(now.year)[2:4]
        self.book_num = book_num
        self.temp = str(self.temp) + " " + u"\N{DEGREE SIGN}" + "C"
        self.bp_R = str(self.bp_R) + " mmHg"
        self.bp_L = str(self.bp_L) + " mmHg"
        self.satO2 = str(self.satO2) + " %"
        self.pulse_R = str(self.pulse_R) + " bpm"
        self.pulse_L = str(self.pulse_L) + " bpm"
        super(VitalSign, self).save(*args, self, **kwargs)


class PhysicalExam(models.Model):
    eyes = models.CharField(max_length=100, blank=True)
    mouth = models.CharField(max_length=100, blank=True)
    head = models.CharField(max_length=100, blank=True)
    lungs = models.CharField(max_length=100, blank=True)
    heart = models.CharField(max_length=100, blank=True)
    abdomen = models.CharField(max_length=100, blank=True)
    upperLimbs = models.CharField(max_length=100, blank=True)
    lowerLimbs = models.CharField(max_length=100, blank=True)
    others = models.CharField(max_length=100, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class CommonPatient(models.Model):
    first_name = models.CharField(max_length=13, blank=False)
    last_name = models.CharField(max_length=13, unique=False, blank=True)
    full_name = models.CharField(max_length=27, unique=True, blank=False)
    address = models.CharField(max_length=25)
    sex = models.CharField(max_length=7, blank=False, choices=SEX_CHOICES)
    dob = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=False)
    Phone = models.CharField(verbose_name='Phone', unique=True, max_length=17)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse('reg_patient', kwargs={'slug': self.slug})


class CommonStaff(models.Model):
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10, unique=False, blank=False)
    full_name = models.CharField(max_length=40, blank=False)
    address = models.CharField(max_length=25)
    sex = models.CharField(max_length=7, blank=False, choices=SEX_CHOICES)
    dob = models.DateField(blank=True)
    age = models.IntegerField(editable=True, blank=True)
    Phone = models.CharField(verbose_name='Phone', max_length=17)
    date_created = models.DateTimeField(auto_now_add=True)
    code = models.SlugField(max_length=7, editable=False, default=000000, blank=True)

    class Meta:
        abstract = True
        unique_together = ['Phone', 'first_name']

    def save(self, *args, **kwargs):
        this_year = datetime.date.today().year
        self.full_name = (str(self.first_name) + " " + str(self.last_name)).upper()
        if self.age:
            if not self.dob:
                self.dob = str(this_year - self.age) + '-' + '01' + '-' + '01'
        elif self.dob:
            self.age = this_year - self.dob.year
        if not self.code:
            self.code = slugify(self.first_name[:2] + str(self.dob)[3:4] + str(self.dob)[2:3] + str(self.dob)[5:7] + self.last_name[:1])
        super(CommonStaff, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name.upper()}'

    def get_absolute_url(self):
        return reverse('reg_staff', kwargs={'slug': self.slug})


class Admission(models.Model):
    patient_NIC = models.IntegerField(blank=True)
    complain = models.CharField(max_length=150)
    past_med_history = models.CharField(max_length=250)
    fees = models.CharField(max_length=12)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True
