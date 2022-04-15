from django.db import models
from django.db import models

from apps.root.models import CommonStaff, Exam
from apps.regi.models import Patient, RegiStaff
import datetime
from apps.accounts.models import Account

from django.db.models.signals import post_save, pre_save


# ==================== USER FOR RADIO ================================================================
class PharUser(models.Model):
    username = models.OneToOneField(Account, unique=True, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.username)


def create_pharUser(sender, **kwargs):
    if kwargs['created']:
        created_obj = Account.objects.all().order_by('date_joined').last()
        name = created_obj.username
        print("phar: " + name)
        if name == 'Pharmacy' or name == 'zane' or name == 'admin':        # 'Radiology', 'PHAR', 'LABO', 'WARD', 'ADMIN', 'zane', 'OTHER'
            pharUser = PharUser.objects.create(username=created_obj)


post_save.connect(create_pharUser, sender=Account)

# ____________________________________________________________________________________________________


# =============  Increment pharmacy dispensary(pd) pn, ms, ds,   =======================
def auto_increment_pdpn():
    now = datetime.date.today()
    all_patients = PharPatient.objects.all().filter(date_created__year=now.year,
                                                 date_created__month=now.month, ).order_by('pn')
    if all_patients.exists():
        pp = all_patients.last()
        if pp.date_created.year == now.year:
            pat_int = int(pp.pn[:5])
            new_pat_int = int(pat_int) + 1
            pn = str(new_pat_int).zfill(5) + "/" + str(now.year)[2:4]
            return pn
    else:
        pn = '00001' + "/" + str(now.year)[2:4]
        return pn


def auto_increment_pdms():
    now = datetime.date.today()
    all_month = PharPrescription.objects.all().filter(date_created__year=now.year,
                                                date_created__month=now.month, ).order_by("date_created")
    if all_month.exists():
        ms = str(all_month.count() + 1).zfill(4)
        return ms
    else:
        ms = '0001'
        return ms


def auto_increment_pdds():
    now = datetime.date.today()
    all_day = PharPrescription.objects.all().filter(date_created__year=now.year,
                                                 date_created__month=now.month,
                                                 date_created__day=now.day).order_by("date_created")
    if all_day.exists():
        count = all_day.count()
        ds = str(count + 1).zfill(3)
        return ds
    else:
        ds = '001'
        return ds


# -------------------------------------------------------------------------


'''
# ==============  Increment Store number, store ms, store ds  (st = store) =====================
def auto_increment_stn():
    now = datetime.date.today()
    # all_patients = Patient.objects.using('radio_db').all().filter(date_created__year=now.year,
    all_patients = XPatient.objects.all().filter(date_created__year=now.year,
                                                 date_created__month=now.month, ).order_by('xn')
    if all_patients.exists():
        lp = all_patients.last()
        if lp.date_created.year == now.year:
            pat_int = int(lp.xn[:5])
            new_pat_int = int(pat_int) + 1
            xn = str(new_pat_int).zfill(5) + "/" + str(now.year)[2:4]
            return xn
    else:
        xn = '00001' + "/" + str(now.year)[2:4]
        return xn


def auto_increment_stms():
    now = datetime.date.today()
    all_purpose = XExam.objects.all().filter(date_created__year=now.year,
                                             date_created__month=now.month, ).order_by("date_created")
    if all_purpose.exists():
        lp = all_purpose.last()

        if lp.date_created.year == now.year:
            if lp.date_created.month == now.month:
                new = int(lp.ms) + 1
                ms = str(new).zfill(4)
                return ms
            else:
                ms = '0001'
                return ms
        else:
            ms = '0001'
            return ms
    else:
        ms = '0001'
        return ms


def auto_increment_stds():
    now = datetime.date.today()
    all_patients = XExam.objects.all().filter(date_created__year=now.year,
                                              date_created__month=now.month,
                                              date_created__day=now.day).order_by("date_created")
    if all_patients.exists():
        lp = all_patients.last()
        if lp.date_created.year == now.year:
            if lp.date_created.month == now.month:
                if lp.date_created.day == now.day:
                    new = int(lp.ds) + 1
                    ds = str(new).zfill(2)
                    return ds
                else:
                    ds = '01'
                    return ds
            else:
                ds = '01'
                return ds
        else:
            ds = '01'
            return ds
    else:
        ds = '01'
        return ds
'''

# -------------------------------------------------------------------------------------


# ==============  Increment Pharmacy Dispensary Yearly Number =====================================
def auto_increment_pys():
    now = datetime.date.today()
    pha_presc = PharPrescription.objects.all().filter(date_created__year=now.year,).order_by('ys')
    if pha_presc.exists():
        count = pha_presc.count()
        new = count + 1
        pys = str(new).zfill(5) + "-" + str(now.year)[2:4]
        return pys
    else:
        pys = '00001' + "-" + str(now.year)[2:4]
        return pys

# _____________________________________________________________________________________

# Create your models here.
WARD_CHOICES = (('', ''),
                ('OPD', 'OPD'),
                ('MAT', 'Maternity'),
                ('LW', 'Labour / Delivery'),
                ('MW', 'Medical Ward'),
                ('SW', 'Surgical Ward'),
                ('CW', "Childrens' Ward"),
                ('OTHER', 'Other'))
DEPTS = (('STORE', 'Store'), ('DISPENSARY', 'Dispensary'))
TITLE_CHOICES = (('PHARM', 'Pharmacist'),
                 ('PHA TECHNO', 'Pha. Technologist'),
                 ('PHA TECH', 'Pha. Technician'),
                 ('As.Tech', 'Assistant Technician'),
                 ('ASS', 'Assistant'),
                 ('OTHER', "Other"))


class PharDept(models.Model):
    dept_name = models.CharField(max_length=15, unique=True,
                            default='', choices=DEPTS)

    def __str__(self):
        return str(self.dept_name.upper())


class PharStaff(CommonStaff):
    title = models.CharField(max_length=15, unique=True,
                            default='', choices=TITLE_CHOICES)

    def __str__(self):
        return str(self.first_name.upper()) + " " + str(self.last_name.upper()[0])


def create_regiStaff(sender, **kwargs):
    if kwargs['created']:
        obj = PharStaff.objects.all().order_by('date_created').last()
        RegiStaff.objects.create(first_name=obj.first_name, last_name=obj.last_name,
                                 full_name=obj.full_name, address=obj.address, age=obj.age,dob=obj.dob,
                                 sex=obj.sex, Phone=obj.Phone, title=obj.title, code=obj.code)


post_save.connect(create_regiStaff, sender=PharStaff)


class PharDrugCategory(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.category_name.upper())

    def save(self, *args, **kwargs):
        self.category_name = (str(self.category_name)).upper()
        super(PharDrugCategory, self).save(*args, **kwargs)


class PharDrugType(models.Model):
    FORM_CHOICES = (("tabs", "Tablets"), ("Syrop", "Syrop"), ("Sach", "Sachet"))
    type_name = models.CharField(max_length=30, default='')
    strength = models.CharField(max_length=30, default='')
    form = models.CharField(max_length=30, choices=FORM_CHOICES, default='')
    unit_cost = models.IntegerField(default='')
    department = models.ForeignKey(PharDept, on_delete=models.CASCADE)
    category = models.ForeignKey(PharDrugCategory, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.type_name)

    def save(self, *args, **kwargs):
        self.type_name = (str(self.type_name)).upper()
        super(PharDrugType, self).save(*args, **kwargs)

    class Meta:
        unique_together = [['type_name', 'strength', 'form']]


class PharPatient(models.Model):
    patient = models.OneToOneField(Patient, default='none',
                                   on_delete=models.CASCADE)
    pn = models.CharField(max_length=20, verbose_name='Phar-Number', primary_key=True,
                          default=auto_increment_pdpn, editable=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.patient.first_name.upper())


class PharPrescription(Exam):
    drug_name = models.ManyToManyField(PharDrugType, through="PharPrescriptionItem")
    ys = models.CharField(max_length=20, verbose_name='Y-Serial', primary_key=False,
                          default=auto_increment_pys, editable=False)
    patient = models.ForeignKey(PharPatient, on_delete=models.CASCADE)
    dept = models.ForeignKey(PharDept, on_delete=models.CASCADE)
    ms = models.CharField(max_length=20, verbose_name='M-Serial',
                          default=auto_increment_pdms, editable=False)
    ds = models.CharField(max_length=20, verbose_name='D-Serial',
                          default=auto_increment_pdds, editable=False)
    cost = models.IntegerField(default=0, editable=False)
    paid = models.IntegerField(default='')
    difference = models.IntegerField(default=0, null=False, editable=False)
    count = models.CharField(max_length=7, editable=False)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.book_num) + ' - ' + str(self.patient.patient.first_name)

    def auto_increment_ex_count(self, *args, **kwargs):
        this = PharPrescription.objects.all().filter(patient=self.patient)  # query this patient
        if this.exists():
            count = this.order_by('count').count()
            self.count = count + 1
        else:
            self.count = 1

    def auto_calc_difference(self, *args, **kwargs):
        self.difference = self.paid - self.cost

    def save(self, *args, **kwargs):
        now = datetime.date.today()
        if len(self.book_num) != 8:
            book_num = str(self.book_num).zfill(5) + "-" + str(now.year)[2:4]
            self.book_num = book_num
            self.auto_increment_ex_count()
            self.auto_calc_difference()
            super(PharPrescription, self).save(*args, self, **kwargs)
        super(PharPrescription, self).save(update_fields=['cost', 'difference'])


class PharPrescriptionItem(models.Model):
    ph_presc = models.ForeignKey(PharPrescription, on_delete=models.CASCADE)
    ph_drug = models.ForeignKey(PharDrugType, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    quantity = models.IntegerField(blank=True, null=True)
    cost = models.IntegerField(editable=False, null=False)
    paid = models.IntegerField(default=0, null=False, blank=False)
    difference = models.IntegerField(default=0, null=False, editable=False)

    def __str__(self):
        return str(self.ph_presc) + " " + str(self.ph_drug)

    def auto_cost(self, *args, **kwargs):
        this = PharDrugType.objects.all().filter(type_name=self.ph_drug)  # query this patient
        if this.exists():
            cost = this[0].unit_cost * self.quantity
            self.cost = cost
        else:
            self.cost = 0

    def auto_calc_difference(self, *args, **kwargs):
        self.difference = self.paid - self.cost

    def save(self, *args, **kwargs):
        self.auto_cost()
        self.auto_calc_difference()
        super(PharPrescriptionItem, self).save(*args, **kwargs)

    class Meta:
        unique_together = [['ph_presc', 'ph_drug']]


def pharpresc_update_cost(sender, instance, *args, **kwargs):
    if kwargs['created']:
        this = PharPrescription.objects.get(book_num=instance.ph_presc.book_num)  # query this Exam
        if this:
            new = this.cost + int(instance.cost)
            this.cost = new
            this.difference = this.paid - this.cost
            this.save(update_fields=['cost', 'difference'])
            print("Exam Updated")
        else:
            print("instance not exist")


post_save.connect(pharpresc_update_cost, sender=PharPrescriptionItem)


class PharDrugDispensed(models.Model):
    TIMES_DAY_CHOICES = (('', ''), ('1/D', 'Once/Day'), ('2/D', 'Twice/Day'), ('3/D', 'Thrice/Day'),
                         ('4', 'Four/D'), ('Q4', 'Every 4H'),
                         ('Q6', 'Every 6H'), ('Q8', 'Every 8H'), ('Q12', 'Every 12H'),)
    staff = models.ForeignKey(PharStaff, on_delete=models.CASCADE)
    phar_drug = models.ForeignKey(PharPrescriptionItem, on_delete=models.CASCADE)
    phar_presc = models.ForeignKey(PharPrescription, on_delete=models.CASCADE)
    quantity_per_doze = models.CharField(max_length=6, default=0, null=False)
    times_per_day = models.CharField(max_length=6, default=0, choices=TIMES_DAY_CHOICES, null=False)
    duration_in_days = models.CharField(max_length=15, default=0, null=False)
    instructions = models.TextField(max_length=150, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        unique_together = ['phar_drug', 'phar_presc']

    def __str__(self):
        return str(self.phar_presc) + " " + str(self.phar_drug)

    def save(self, *args, **kwargs):
        super(PharDrugDispensed, self).save(*args, **kwargs)
