from django.db import models
from apps.root.models import CommonStaff, Exam
from apps.regi.models import Patient
import datetime
from apps.accounts.models import Account

from django.db.models.signals import post_save, pre_save


# ==================== USER FOR Mate ========================================================
class MateUser(models.Model):
    username = models.OneToOneField(Account, unique=True, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.username)


def create_mateUser(sender, **kwargs):
    if kwargs['created']:
        created_obj = Account.objects.all().order_by('date_joined').last()
        name = created_obj.username
        if name == 'Maternity' or name == 'zane' or name == 'admin':
            radUser = MateUser.objects.create(username=created_obj)


post_save.connect(create_mateUser, sender=Account)

DEPTS = (('Laboratory1', 'Laboratory_1'), ('Laboratory2', 'Laboratory_2'))

TITLE_CHOICES = (('MD', 'Pathologist'),
                 ('LAB Sc.', 'Lab. Scientist'),
                 ('LAB TECH', 'Lab. Technician'),
                 ('As.Tech', 'Assistant Technician'),
                 ('Assis', 'Assistant'),
                 ('Other', "Other"))


class MateDept(models.Model):
    name = models.CharField(max_length=15, unique=True,
                            default='', choices=DEPTS)

    def __str__(self):
        return str(self.name.upper())


class MateStaff(CommonStaff):
    title = models.CharField(max_length=15,
                             default='', choices=TITLE_CHOICES)

    def __str__(self):
        return str(self.first_name.upper()) + " " + str(self.last_name.upper()[0])


