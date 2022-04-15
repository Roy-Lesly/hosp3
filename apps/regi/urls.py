from django.urls import path
from . import apps, views, search
from .views import *
from django.views.decorators.csrf import csrf_exempt


app_name = 'regi'

urlpatterns = [
    path('', regiWelcomeView, name='regiWelcome'),
    path('regHome/', regiRegistration, name='regHome'),
    path('payHome/', regiPayment, name='payHome'),

    path('regiCreate/', patient_Create, name='regiPatCreate'),
    path('regiList/', patient_List, name='regiPatList'),
    path('regiUpdate/<int:id>/', patient_Update, name='regiUpdate'),
    path('regiDelete/<int:id>/', patient_Delete, name='regiDelete'),

    path('patCreateModalU/', patient_Create_Modal_u, name='PatCreateModalU'),
    path('patUpdate/<int:sn>', patient_update, name='patUpdate'),
    path('patCreateModalX/', patient_Create_Modal_x, name='PatCreateModalX'),
    path('patSearch/', csrf_exempt(views.patSearch), name='patSearch'),

    # ======================= Regis Staff ============================
    path('staffList/', views.staff_List, name='staffList'),
    path('staffCreate/', views.staff_Create, name='staffCreate'),
    path('staffUpdate/<int:id>', views.staff_Update, name='staffUpdate'),
    path('staffDelete/<int:id>', views.staff_Delete, name='staffDelete'),

    path('search_patient/', csrf_exempt(search.search_patient), name='search_patient'),  # by phone or sn

]