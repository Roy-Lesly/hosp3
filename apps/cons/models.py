import datetime

from django.db import models
from apps.accounts.models import Account
from apps.labo.models import LaboTestType
from apps.phar.models import PharDrugType
from apps.radi.models import RadiTestType
from apps.regi.models import Patient, RegiStaff
from apps.root.models import PhysicalExam, Admission, CommonStaff, VitalSign
from django.db.models.signals import post_save


# Create your models here.
# ==================== USER FOR CONSULTATION ========================================================
class ConsUser(models.Model):
    username = models.OneToOneField(Account, unique=True, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.username)


def create_consUser(sender, **kwargs):
    if kwargs['created']:
        created_obj = Account.objects.all().order_by('date_joined').last()
        name = created_obj.username
        if name == 'Finance' or name == 'zane' or name == 'admin':
            consUser = ConsUser.objects.create(username=created_obj)


post_save.connect(create_consUser, sender=Account)


WARD_CHOICES = (('', ''),
                ('OPD', 'OPD'),
                ('MAT', 'Maternity'),
                ('LW', 'Labour / Delivery'),
                ('MW', 'Medical Ward'),
                ('SW', 'Surgical Ward'),
                ('CW', "Childrens' Ward"),
                ('OTHER', 'Other'))
DEPTS = (('cons1', 'Consultation_1'), ('cons2', 'Consultation_2'))
TITLE_CHOICES = (('Path', 'Pathologist'),
                 ('LAB Sc.', 'Lab. Scientist'),
                 ('LAB TECH', 'Lab. Technician'),
                 ('As.Tech', 'Assistant Technician'),
                 ('Assis', 'Assistant'),
                 ('Other', "Other"))


# ==============  Increment Lab number, Lab ms, Lab ds   =====================
def auto_increment_cn():
    now = datetime.date.today()
    all_patients = ConsPatient.objects.all().filter(date_created__year=now.year,
                                                    date_created__month=now.month, ).order_by('cn')
    if all_patients.exists():
        lp = all_patients.last()
        if lp.date_created.year == now.year:
            pat_int = int(lp.cn[:5])
            new_pat_int = int(pat_int) + 1
            cn = str(new_pat_int).zfill(5) + "-" + str(now.year)[2:4]
            return cn
    else:
        cn = '00001' + "-" + str(now.year)[2:4]
        return cn


def auto_increment_cms():
    now = datetime.date.today()
    all_month = LaboExam.objects.all().filter(date_created__year=now.year,
                                              date_created__month=now.month, ).order_by("date_created")
    if all_month.exists():
        count = all_month.count()
        ms = str(count + 1).zfill(4)
        return ms
    else:
        ms = '0001'
        return ms


def auto_increment_cds():
    now = datetime.date.today()
    all_day = LaboExam.objects.all().filter(date_created__year=now.year,
                                            date_created__month=now.month,
                                            date_created__day=now.day).order_by("date_created")
    if all_day.exists():
        count = all_day.count()
        new = count + 1
        ds = str(new).zfill(3)
        return ds
    else:
        ds = '001'
        return ds


DEPTS = (('Cons1', 'Consultation_1'), ('Cons2', 'Consultation_2'))


# ===================== CONS DEPT ==============================
class ConsDept(models.Model):
    name = models.CharField(max_length=15, unique=True,
                            default='', choices=DEPTS)

    def __str__(self):
        return str(self.name.upper())


# ===================== CONS STAFF ==============================
class ConsStaff(CommonStaff):
    title = models.CharField(max_length=15,
                             default='', choices=TITLE_CHOICES)

    def __str__(self):
        return str(self.first_name.upper()) + " " + str(self.last_name.upper()[0])


def create_regiStaff(sender, **kwargs):
    if kwargs['created']:
        obj = ConsStaff.objects.all().order_by('date_created').last()
        RegiStaff.objects.create(first_name=obj.first_name, last_name=obj.last_name,
                                 full_name=obj.full_name, address=obj.address, age=obj.age,dob=obj.dob,
                                 sex=obj.sex, Phone=obj.Phone, title=obj.title, code=obj.code)


post_save.connect(create_regiStaff, sender=ConsStaff)


# ===================== CONS PATIENT ==============================
class ConsPatient(models.Model):
    patient = models.OneToOneField(Patient, default='none', on_delete=models.CASCADE)
    cn = models.CharField(max_length=20, verbose_name='Con-Number', primary_key=True,
                          default=auto_increment_cn, editable=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.patient.first_name.upper())


# ===================== CONSULTATION ==============================
class Consultation(models.Model):
    patient = models.ForeignKey(ConsPatient, on_delete=models.CASCADE)
    complain = models.CharField(max_length=150)
    past_med_history = models.CharField(max_length=250)
    fees = models.CharField(max_length=12)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)


# ===================== VITAL SIGN =============================
class VitalSign(VitalSign):
    cons = models.OneToOneField(Consultation, on_delete=models.CASCADE)


# ===================== PHYSICAL EXAM =============================
class PhysicalExam(PhysicalExam):
    cons = models.OneToOneField(Consultation, on_delete=models.CASCADE)


# ===================== TEST EXAM =============================
class Test(models.Model):
    cons = models.OneToOneField(Consultation, on_delete=models.CASCADE)
    labs = models.ManyToManyField(LaboTestType, blank=True)
    echo = models.ManyToManyField(RadiTestType, related_name='echo_set', blank=True)
    xray = models.ManyToManyField(RadiTestType, related_name='xray_set', blank=True)


# ===================== PRESCRIPTION EXAM =============================
class Prescription(models.Model):
    cons = models.OneToOneField(Consultation, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=50)
    ph_drug = models.ManyToManyField(PharDrugType)
    # ph_drug = models.ForeignKey(PharDrugType, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=50, blank=True)
    duration = models.CharField(max_length=50, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

