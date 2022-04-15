from django.urls import path
from . import apps
from .views import *
from . import views

app_name = 'mate'

urlpatterns = [
    path('', mateWelcomeView, name='mateWelcome'),
    # path('wardHome/', EchoHomeView.as_view(), name='wardHome'),
    # path('ward2Home/', XrayHomeView.as_view(), name='ward2Home'),

    # ======================= Labo Staff ============================
    path('staffList/', views.staff_List, name='staffList'),
    path('staffCreate/', views.staff_Create, name='staffCreate'),
    path('staffUpdate/<int:id>', views.staff_Update, name='staffUpdate'),
    path('staffDelete/<int:id>', views.staff_Delete, name='staffDelete'),
]