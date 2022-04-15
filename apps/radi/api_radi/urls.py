from django.urls import path
from .views import *            # PatientListAPIView

app_name = 'api_radi'

urlpatterns = [
    # ___________________ ECHO API URLs ___________________________________
    path('upatlist/', UPatientList.as_view(), name='upatlist'),
    path('upatdetail/<un>/', UPatientDetail.as_view(), name='upatpetail'),

    path('uexamlistall/', UExamListAll.as_view(), name='uexamlistall'),
    path('uexamlistall/<patient>', UExamListOne.as_view(), name='uexamlistone'),
    path('uexamdetail/<ys>', UExamDetail.as_view(), name='uexamdetail'),

    path('uresultlistall/', UResultListAll.as_view(), name='uresultlistall'),
    path('uresultlistall/<lexam>', UResultListOne.as_view(), name='uresultlistone'), # all results for 1 exam
    path('uresultdetail/<id>', UResultDetail.as_view(), name='uresultdetail'),

    # path('uspatdelete/<un>/', UPatientDelete.as_view(), name='uspatdelete'),

    # ___________________ XRAY API URLs ___________________________________
    path('xpatlist/', XPatientList.as_view(), name='xpatlist'),
    path('xpatdetail/<xn>/', XPatientDetail.as_view(), name='xpatpetail'),

    path('xexamlistall/', XExamListAll.as_view(), name='xexamlistall'),
    path('xexamlistall/<patient>', XExamListOne.as_view(), name='xexamlistone'),
    path('xexamdetail/<ys>', XExamDetail.as_view(), name='xexamdetail'),

    path('xresultlistall/', XResultListAll.as_view(), name='xresultlistall'),
    path('xresultlistall/<lexam>', XResultListOne.as_view(), name='xresultlistone'),  # all results for 1 exam
    path('xresultdetail/<id>', XResultDetail.as_view(), name='xresultdetail'),

]