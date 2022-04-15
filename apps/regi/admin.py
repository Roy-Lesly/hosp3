from django.contrib import admin
from .models import *      # Patient, Purpose, Test

# admin.site.register(RegisUser)
admin.site.register([RegiStaff, RegiUser])
admin.site.register(Purpose)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass
    list_display = ("sn", "reg_num", "full_name", "address", "sex", "Phone", "dob", "date_created")
    list_filter = ("sn", "date_created")
    search_fields = ("sn", "full_name", "reg_num", "Phone")
