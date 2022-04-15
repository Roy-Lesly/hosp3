from django.db import models
from django.utils.text import slugify

from apps.root.models import CommonStaff, Exam
from apps.regi.models import Patient, RegiStaff
import datetime
from apps.accounts.models import Account

from django.db.models.signals import post_save, pre_save


# ==================== USER FOR Labo ========================================================
class LaboUser(models.Model):
    username = models.OneToOneField(Account, unique=True, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.username)


def create_laboUser(sender, **kwargs):
    if kwargs['created']:
        created_obj = Account.objects.all().order_by('date_joined').last()
        name = created_obj.username
        if name == 'Laboratory' or name == 'zane' or name == 'admin':
            radUser = LaboUser.objects.create(username=created_obj)


post_save.connect(create_laboUser, sender=Account)


# ______________________________________________________________________________________________________

# ==============  Increment Lab number, Lab ms, Lab ds   =====================
def auto_increment_ln():
    now = datetime.date.today()
    all_patients = LaboPatient.objects.all().filter(date_created__year=now.year,
                                                    date_created__month=now.month, ).order_by('ln')
    if all_patients.exists():
        lp = all_patients.last()
        if lp.date_created.year == now.year:
            pat_int = int(lp.ln[:5])
            new_pat_int = int(pat_int) + 1
            ln = str(new_pat_int).zfill(5) + "-" + str(now.year)[2:4]
            return ln
    else:
        ln = '00001' + "-" + str(now.year)[2:4]
        return ln


def auto_increment_lms():
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


def auto_increment_lds():
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


# -------------------------------------------------------------------------------------

# ==============  Increment Year Number =====================================

def auto_increment_ys():
    now = datetime.date.today()
    l_exams = LaboExam.objects.all().filter(date_created__year=now.year, ).order_by('ys')
    if l_exams.exists():
        count = l_exams.count()
        new = count + 1
        ys = str(new).zfill(5) + "-" + str(now.year)[2:4]
        return ys
    else:
        ys = '00001' + "-" + str(now.year)[2:4]
        return ys


# _____________________________________________________________________________________


# Create your models here.
# PURPOSES = (('CONST', 'consultation'), ('RDV', 'rendez-vous'), ('VISIT', 'visit'), ('OTHER', 'other'))

WARD_CHOICES = (('', ''),
                ('OPD', 'OPD'),
                ('MAT', 'Maternity'),
                ('LW', 'Labour / Delivery'),
                ('MW', 'Medical Ward'),
                ('SW', 'Surgical Ward'),
                ('CW', "Childrens' Ward"),
                ('OTHER', 'Other'))
DEPTS = (('Laboratory1', 'Laboratory_1'), ('Laboratory2', 'Laboratory_2'))
TITLE_CHOICES = (('Path', 'Pathologist'),
                 ('LAB Sc.', 'Lab. Scientist'),
                 ('LAB TECH', 'Lab. Technician'),
                 ('As.Tech', 'Assistant Technician'),
                 ('Assis', 'Assistant'),
                 ('Other', "Other"))


class LaboDept(models.Model):
    name = models.CharField(max_length=15, unique=True,
                            default='', choices=DEPTS)

    def __str__(self):
        return str(self.name.upper())


class LaboStaff(CommonStaff):
    title = models.CharField(max_length=15,
                             default='', choices=TITLE_CHOICES)

    def __str__(self):
        return str(self.first_name.upper()) + " " + str(self.last_name.upper()[0])


def create_regiStaff(sender, **kwargs):
    if kwargs['created']:
        obj = LaboStaff.objects.all().order_by('date_created').last()
        RegiStaff.objects.create(first_name=obj.first_name, last_name=obj.last_name,
                                 full_name=obj.full_name, address=obj.address, age=obj.age,dob=obj.dob,
                                 sex=obj.sex, Phone=obj.Phone, title=obj.title, code=obj.code)


post_save.connect(create_regiStaff, sender=LaboStaff)


class LaboTestCategory(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.category_name.upper())

    def save(self, *args, **kwargs):
        self.category_name = (str(self.category_name)).upper()
        super(LaboTestCategory, self).save(*args, **kwargs)


class LaboTestType(models.Model):
    type_name = models.CharField(max_length=15, unique=True, default='')
    cost = models.IntegerField(default='')
    department = models.ForeignKey(LaboDept, on_delete=models.CASCADE)
    category = models.ForeignKey(LaboTestCategory, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.type_name)

    def save(self, *args, **kwargs):
        self.type_name = (str(self.type_name)).upper()
        super(LaboTestType, self).save(*args, **kwargs)


class LaboPatient(models.Model):
    patient = models.OneToOneField(Patient, default='none', on_delete=models.CASCADE)
    ln = models.CharField(max_length=20, verbose_name='Lab-Number', primary_key=True,
                          default=auto_increment_ln, editable=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.patient.first_name.upper())


class LaboExam(Exam):
    labo_type = models.ManyToManyField(LaboTestType, through='LaboExamItem')
    ys = models.CharField(max_length=20, verbose_name='Y-Serial', primary_key=False,
                          default=auto_increment_ys, editable=False)
    patient = models.ForeignKey(LaboPatient, on_delete=models.CASCADE)
    dept = models.ForeignKey(LaboDept, default=1, on_delete=models.CASCADE, editable=False)
    ms = models.CharField(max_length=20, verbose_name='M-Serial',
                          default=auto_increment_lms, editable=False)
    ds = models.CharField(max_length=20, verbose_name='D-Serial',
                          default=auto_increment_lds, editable=False)
    cost = models.IntegerField(default=0, editable=False)
    paid = models.IntegerField(default='')
    count = models.CharField(max_length=7, editable=False)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.book_num) + ' - ' + str(self.patient.patient.first_name)

    def auto_increment_ex_count(self, *args, **kwargs):
        this = LaboExam.objects.all().filter(patient=self.patient)  # query this patient
        if this.exists():
            count = this.order_by('count').count()
            self.count = count + 1
        else:
            self.count = 1

    def save(self, *args, **kwargs):
        now = datetime.date.today()
        if len(self.book_num) != 8:
            book_num = str(self.book_num).zfill(5) + "-" + str(now.year)[2:4]
            self.book_num = book_num
            self.auto_increment_ex_count()
            super(LaboExam, self).save(*args, self, **kwargs)
        super(LaboExam, self).save(update_fields=['cost'])


class LaboExamItem(models.Model):
    lexam = models.ForeignKey(LaboExam, related_name="lexams", on_delete=models.CASCADE)
    ltype = models.ForeignKey(LaboTestType, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    cost = models.CharField(max_length=6, editable=False, null=False)
    paid = models.CharField(max_length=6, default=0, null=False, blank=False)

    def __str__(self):
        return str(self.lexam) + " " + str(self.ltype)

    def auto_cost(self, *args, **kwargs):
        this = LaboTestType.objects.all().filter(type_name=self.ltype)  # query this patient
        if this.exists():
            cost = this[0].cost
            self.cost = cost
        else:
            self.cost = 0

    def save(self, *args, **kwargs):
        self.auto_cost()
        super(LaboExamItem, self).save(*args, **kwargs)

    class Meta:
        unique_together = [['ltype', 'lexam']]


def labexam_update_cost(sender, instance, *args, **kwargs):
    if kwargs['created']:
        this = LaboExam.objects.get(book_num=instance.lexam.book_num)  # query this Exam
        if this:
            new = this.cost + int(instance.cost)
            this.cost = new
            this.save(update_fields=['fees'])
            print("Exam Updated")
        else:
            print("instance not exist")


post_save.connect(labexam_update_cost, sender=LaboExamItem)


class LaboFinding(models.Model):
    staff = models.ForeignKey(LaboStaff, on_delete=models.CASCADE)
    lab_test = models.ForeignKey(LaboExamItem, on_delete=models.CASCADE)
    lab_exam = models.ForeignKey(LaboExam, on_delete=models.CASCADE)
    findings = models.TextField(max_length=150, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        unique_together = ['lab_test', 'lab_exam']

    def __str__(self):
        return str(self.lab_exam) + " " + str(self.lab_test)

    def save(self, *args, **kwargs):
        super(LaboFinding, self).save(*args, **kwargs)
