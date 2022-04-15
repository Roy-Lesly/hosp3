from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

user = None


def current_user(request):
    global user
    user = get_user_model()


class MyAccountManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError("Must Enter Username")

        user = self.model(username=username)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password)

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


DEPT_CHOICES = (('Registration', 'Registration'),
                ('Radiology', 'Radiology'),
                ('Pharmacy', 'Pharmacy'),
                ('Laboratory', 'Laboratory'),
                ('Ophthalmology', 'Ophthalmology'),
                ('Maternity', 'Maternity'),
                ('Ward', 'Ward'),
                ('Orthopedic', 'Orthopedic'),
                ('admin', "Admin"),
                ('zane', "Zane"),
                ('Technical', "Technical"),
                ('Finance', "Finance"),
                ('Other', 'Other'))


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='username', choices=DEPT_CHOICES, max_length=15, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, editable=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perms(self, perm_list, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
