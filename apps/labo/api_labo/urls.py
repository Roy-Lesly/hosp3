from django.urls import path, include
from .views import *
from .views1 import *
from .views2 import *
from rest_framework.routers import DefaultRouter

app_name = 'api_labo'

router = DefaultRouter
#router.register('lpatient', LaboPatViewSet, basename='lpatient')

urlpatterns = [

    # ======================= API CBV (api_labo\dviews.py) =====================
    # path('labpatlist/', LaboPatientList.as_view(), name='labpatlist'),
    # path('labpatdetail/<ln>/', LaboPatientDetail.as_view(), name='labpatdetail'),

    # path('labexamlistall/', LaboExamListAll.as_view(), name='labexamlistall'),
    # path('labexamlistone/<patient>', LaboExamListOne.as_view(), name='labexamlistone'),
    # path('labexamdetail/<id>', LaboExamDetail.as_view(), name='labexamdetail'),

    # path('labresultlistall/', LaboResultListAll.as_view(), name='labresultlistall'),
    # path('labresultlistall/<lexam>', LaboResultListOne.as_view(), name='labresultlistone'), # all results for 1 exam
    # path('labresultdetail/<id>', LaboResultDetail.as_view(), name='labresultdetail'),


    # ====================== API FBV (api_labo\views1.py) =======================
    # 1. No rest interface
    # path('labpatlist/', labo_patient_list, name='labpatlist'),
    # path('labpatdetail/<slug:ln>/', labo_patient_detail, name='labpatdetail'),

    # path('labexamlistall/', labo_exam_list_all, name='labexamlistall'),
    # path('labexamlistone/<slug:patient>', labo_exam_list_one, name='labexamlistone'),
    # path('labexamdetail/<int:id>', labo_exam_detail, name='labexamdetail'),

    # path('labresultlistall/', labo_result_list, name='labresultlistall'),
    # path('labresultlistone/<slug:lexam>', labo_result_list_one, name='labresultlistone'),
    # path('labresultdetail/<int:id>', labo_result_detail, name='labresultdetail'),

    # 2. With rest interface
    path('labpatlist/', labo_patient_list_1, name='labpatlist'),
    path('labpatdetail/<slug:ln>/', labo_patient_detail_1, name='labpatdetail'),

    path('labexamlistall/', labo_exam_list_all_1, name='labexamlistall'),
    path('labexamlistone/<slug:patient>', labo_exam_list_one_1, name='labexamlistone'),
    path('labexamdetail/<int:id>', labo_exam_detail, name='labexamdetail'),

    path('labresultlistall/', labo_result_list_1, name='labresultlistall'),
    path('labresultlistone/<slug:lexam>', labo_result_list_one_1, name='labresultlistone'),
    path('labresultdetail/<int:id>', labo_result_detail_1, name='labresultdetail'),


    # ================== API FBV (api_labo\views2.py) ===================
    # Using Mixins
    # path('generic/labopat/', GenericLaboPatAPIView.as_view(), name='labopat'),
    # path('generic/labopat/<slug:ln>/', GenericLaboPatAPIView.as_view(), name='labopat'),
    # path('generic/laboexam/', GenericLaboExamAPIView.as_view(), name='laboexam'),
    # path('generic/laboexam/<patient>', GenericLaboExamAPIView.as_view(), name='laboexam'),
    # path('generic/laboresult/', GenericLaboResultAPIView.as_view(), name='laboresult'),
    # path('generic/laboresult/<int:id>', GenericLaboResultAPIView.as_view(), name='laboresult'),

    # Using ViewSet and Routers
    # ====================== Using ViewSet =======================
    # path('viewset/', include(router.urls)),

]