from django.urls import path
from . import apps
from . import views
from . import dviews
from . import search
from django.views.decorators.csrf import csrf_exempt

app_name = 'labo'

urlpatterns = [
    path('', views.laboWelcomeView, name='laboWelcome'),
    path('<int:id>', views.laboWelcomeView, name='laboWelcome'),
    path('laboHome/', views.laboHomeView, name='laboHome'),
    path('dash/', dviews.index, name='laboDash'),
    path('dash/page1', dviews.statistics, name='laboDash1'),
    path('dash/page2', dviews.income, name='laboDash2'),
    path('dash/page3', dviews.other, name='laboDash3'),

    # ======================== FBVs ==============================
    path('patcreate/', views.patient_create, name='laboPatCreate'),
    path('patlist/', views.patient_list, name='laboPatList'),
    path('patdetail/<slug>', views.patient_detail, name='laboPatDetail'),
    path('patupdate/', views.patient_update, name='laboPatUpdate'),
    path('patdelete/', views.patient_delete, name='laboPatDelete'),

    path('examcreate/', views.exam_create, name='laboExamCreate'),
    path('newtestinnewexam/', views.new_test_in_new_exam, name='newTestInNewExam'),
    path('examdetail/<slug>', views.exam_detail, name='laboExamDetail'),
    path('examupdate/<slug>', views.exam_detail, name='laboExamUpdate'),
    path('examlist/', views.exam_list, name='laboExamList'),

    path('examitemcreate/', views.exam_item_create, name='laboExamItemCreate'),
    # path('examitemdetail/<int:id>', views.exam_item_detail, name='laboExamItemdetail'),
    path('examitemupdate/<int:id>', views.exam_item_update, name='laboExamItemupdate'),

    path('resultcreate/', views.result_Create, name='laboResultCreate'),
    path('resultlist/', views.result_List, name='laboResultList'),
    path('resultdetail/<int:id>', views.result_Detail, name='laboResultDetail'),
    path('resultupdate/<slug:id>', views.result_Update, name='laboResultUpdate'),
    path('resultdelete/<slug:id>', views.result_Delete, name='laboResultDelete'),


    # ======================= Labo Staff ============================
    path('staffList/', views.staff_List, name='staffList'),
    path('staffCreate/', views.staff_Create, name='staffCreate'),
    path('staffUpdate/<int:id>', views.staff_Update, name='staffUpdate'),
    path('staffDelete/<int:id>', views.staff_Delete, name='staffDelete'),

    # ====================== Labo Category =========================
    path('categoryList/', views.category_List, name='categoryList'),
    path('categoryCreate/', views.category_Create, name='categoryCreate'),
    path('categoryUpdate/<int:id>', views.category_Update, name='categoryUpdate'),
    path('categoryDelete/<int:id>', views.category_Delete, name='categoryDelete'),

    # ====================== Labo Type =========================
    path('typeList/', views.type_List, name='typeList'),
    path('typeCreate/', views.type_Create, name='typeCreate'),
    path('typeUpdate/<int:id>', views.type_Update, name='typeUpdate'),
    path('typeDelete/<int:id>', views.type_Delete, name='typeDelete'),

    # ====================== Searches =========================
    path('search_labo_patient/', csrf_exempt(search.search_labo_patient), name='search_labo_patient'),  # by phone or ln
    path('search_labo_exam/', csrf_exempt(search.search_labo_exam), name='search_labo_exam'),  # by book_num or exam_num

    path('search_labo_test/', csrf_exempt(search.search_labo_test), name='search_labo_test'), # returns tests per category
    path('validate_code/', csrf_exempt(search.validate_code), name='validate_code'),

    # ==================== This year ========================
    path('labo_pats_this_year/', search.labo_pats_this_year, name='lP_all_this_Year'),
    path('labo_exams_this_year/', search.labo_exams_this_year, name='lE_all_this_Year'),
    path('labo_exams_item_this_year/', search.labo_exams_item_this_year, name='lEI_all_this_Year'),
    path('labo_tests_stats_this_year/', search.labo_tests_stats_this_year, name='lTS_this_Year'),

    # ==================== Last year ========================
    path('labo_pats_last_year/', search.labo_pats_last_year, name='lP_all_last_Year'),
    path('labo_exams_last_year/', search.labo_exams_last_year, name='lE_all_last_Year'),
    path('labo_exams_item_last_year/', search.labo_exams_item_last_year, name='lEI_all_last_Year'),

    # path('laboSearch1/', search_res_ln, name='laboSearch1'),
    # path('laboSearch2/', search_res_ph, name='laboSearch2'),
    # path('laboSearch3/', search_res_sn, name='laboSearch3'),
    # path('laboSearch4/', search_res_fn, name='laboSearch4'),
                 # returns tests per category
]