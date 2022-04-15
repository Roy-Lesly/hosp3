from django.urls import path
from . import apps
from .views import *
from . import views

app_name = 'cons'

urlpatterns = [
    path('', cons_welcome, name='consWelcome'),
    # path('wardHome/', EchoHomeView.as_view(), name='wardHome'),
    # path('ward2Home/', XrayHomeView.as_view(), name='ward2Home'),

    # ======================= Cons Staff ============================
    path('staffList/', views.staff_List, name='staffList'),
    path('staffCreate/', views.staff_Create, name='staffCreate'),
    path('staffUpdate/<int:id>', views.staff_Update, name='staffUpdate'),
    path('staffDelete/<int:id>', views.staff_Delete, name='staffDelete'),

    # ======================== FBVs ==============================
    path('patcreate/', views.patient_create, name='consPatCreate'),
    path('patlist/', views.patient_list, name='consPatList'),
    path('patdetail/<slug>', views.patient_detail, name='consPatDetail'),
    path('patupdate/', views.patient_update, name='consPatUpdate'),
    path('patdelete/', views.patient_delete, name='consatDelete'),

]