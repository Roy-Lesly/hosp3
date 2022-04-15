from django.urls import path
from . import apps
from .views import *
from . import dviews
from . import sviews

app_name = 'phar'

urlpatterns = [
    path('', pharWelcomeView, name='pharWelcome'),
    path('dispHome/', PharmHomeView.as_view(), name='dispHome'),
    path('storeHome/', StoreHomeView.as_view(), name='storeHome'),

    # ======================= Pharm Dept ============================
    path('DeptList/', dept_List, name='deptList'),
    path('DeptCreate/', dept_Create_Update, name='deptCreate'),
    path('DeptUpdate/<int:id>', dept_Create_Update, name='deptUpdate'),
    path('DeptDelete/<int:id>', dept_Delete, name='deptDelete'),

    # ======================= Pharm Staff ============================
    path('staffList/', staff_List, name='staffList'),
    path('staffCreate/', staff_Create, name='staffCreate'),
    path('staffUpdate/<int:id>', staff_Update, name='staffUpdate'),
    path('staffDelete/<int:id>', staff_Delete, name='staffDelete'),

    # ====================== Pharm Drug Category =========================
    path('categoryList/', category_List, name='categoryList'),
    path('categoryCreate/', category_Create_Update, name='categoryCreate'),
    path('categoryUpdate/<int:id>', category_Create_Update, name='categoryUpdate'),
    path('categoryDelete/<int:id>', category_Delete, name='categoryDelete'),

    # ====================== Pharm Drug Type =========================
    path('typeList/', type_List, name='typeList'),
    path('typeCreate/', type_Create_Update, name='typeCreate'),
    path('typeUpdate/<int:id>', type_Create_Update, name='typeUpdate'),
    path('typeDelete/<int:id>', type_Delete, name='typeDelete'),

    # ======================== Dispensary Views ==============================
    path('disp/', dviews.pharWelcomeView, name='pharHomeView'),
    path('p_patCreate/', dviews.patient_create, name='dispPatCreate'),
    path('p_patList/', dviews.patient_list, name='dispPatList'),
    path('p_patDetail/<slug>', dviews.patient_detail, name='dispPatDetail'),
    path('p_patDelete/', dviews.patient_delete, name='dispPatDelete'),

    path('p_prescCreate/', dviews.prescription_Create_Update, name='dispPrescCreate'),
    path('p_prescList/', dviews.prescription_List, name='dispPrescList'),
    # path('p_prescDetail/<slug>', dviews.prescription_detail, name='dispPrecDetail'),
    path('p_prescDelete/', dviews.prescription_Delete, name='dispPrescDelete'),

    path('p_prescItemCreate/', dviews.prescription_item_Create_Update, name='dispPrescItemCreate'),
    path('p_prescItemList/', dviews.prescription_item_List, name='dispPrescItemList'),
    # path('p_prescItemDetail/<slug>', dviews.prescription_item_detail, name='dispPrescItemDetail'),
    path('p_presItemcDelete/', dviews.prescription_item_Delete, name='dispPrescItemDelete'),

    path('p_drugDispensedCreate/', dviews.drug_dispensed_Create_Update, name='dispDispensedCreate'),
    path('p_drugDispensedUpdate/<int:id>', dviews.drug_dispensed_Create_Update, name='dispDispensedUpdate'),
    path('p_drugDispensedList/', dviews.drug_dispensed_List, name='dispDispensedList'),
    path('p_drugDispensedDelete/<int:id>', dviews.drug_dispensed_Delete, name='dispDispensedDelete'),

]