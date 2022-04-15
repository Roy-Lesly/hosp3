from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import apps
from . import views
from . import dviews
from . import uviews
from . import xviews
from . import usearch
from . import xsearch
from . import print

app_name = 'radi'

urlpatterns = [
    path('', views.radiWelcomeView, name='radiWelcome'),

    path('udash/', dviews.u_index, name='echoDash'),
    path('udash/page0', dviews.u_statistics_0, name='echoDash0'),
    path('udash/page1', dviews.u_statistics_1, name='echoDash1'),
    path('udash/page2', dviews.u_statistics_2, name='echoDash2'),
    path('udash/page3', dviews.u_income, name='echoDash3'),
    path('udash/page4', dviews.u_other, name='echoDash4'),

    path('xdash/', dviews.x_index, name='xrayDash'),
    path('xdash/page1', dviews.x_statistics_1, name='xrayDash1'),
    path('xdash/page2', dviews.x_statistics_2, name='xrayDash2'),
    path('xdash/page3', dviews.x_income, name='xrayDash3'),
    path('xdash/page4', dviews.x_other, name='xrayDash4'),


    # ======================= Radio Staff ============================
    path('staffList/', views.staff_List, name='staffList'),
    path('staffCreate/', views.staff_Create, name='staffCreate'),
    path('staffUpdate/<int:id>', views.staff_Update, name='staffUpdate'),
    path('staffDelete/<int:id>', views.staff_Delete, name='staffDelete'),

    # ====================== Radio Category =========================
    path('categoryList/', views.category_List, name='categoryList'),
    path('categoryCreate/', views.category_Create, name='categoryCreate'),
    path('categoryUpdate/<int:id>', views.category_Update, name='categoryUpdate'),
    path('categoryDelete/<int:id>', views.category_Delete, name='categoryDelete'),

    # ====================== Radi Exam Type =========================
    path('typeList/', views.type_List, name='typeList'),
    path('typeCreate/', views.type_Create, name='typeCreate'),
    path('typeUpdate/<int:id>', views.type_Update, name='typeUpdate'),
    path('typeDelete/<int:id>', views.type_Delete, name='typeDelete'),

    # ====================== Radi Department =========================
    path('deptList/', views.dept_List, name='deptList'),
    path('deptCreate/', views.dept_Create, name='deptCreate'),
    path('deptUpdate/<int:id>', views.dept_Update, name='deptUpdate'),
    # path('deptDelete/<int:id>', views.dept_Delete, name='deptDelete'),

    # ====================== Radi Handing Over =========================
    path('handingList/', views.handing_List, name='handingList'),
    path('handingCreate/', views.handing_Create, name='handingCreate'),
    path('handingUpdate/<int:id>', views.handing_Update, name='handingUpdate'),
    path('handingDelete/<int:id>', views.handing_Delete, name='handingDelete'),

    # ======================== Maintence ===========================
    path('maintenanceList/', views.maintenance_List, name='maintenanceList'),
    path('maintenanceCreate/', views.maintenance_Create, name='maintenanceCreate'),
    path('maintenanceUpdate/<int:id>', views.maintenance_Update, name='maintenanceUpdate'),
    path('maintenanceDelete/<int:id>', views.maintenance_Delete, name='maintenanceDelete'),

    # ======================== Echo Views ==============================
    path('echo/', uviews.echoHomeView, name='echoHomeView'),
    path('u_patcreate/', uviews.u_patient_create, name='echoPatCreate'),
    path('u_patlist/', uviews.u_patient_list, name='echoPatList'),
    path('u_patdetail/<slug>', uviews.u_patient_detail, name='echoPatDetail'),
    path('u_patdelete/', uviews.u_patient_delete, name='echoPatDelete'),
    path('u_examcreate/', uviews.u_exam_create, name='echoExamCreate'),
    path('u_examlist/', uviews.u_exam_list, name='echoExamList'),
    path('u_examdetail/<slug:slug>', uviews.u_exam_detail, name='echoExamDetail'),
    path('u_examupdate/<slug:slug>', uviews.u_exam_update, name='echoExamUpdate'),
    path('u_examitemcreate/', uviews.u_exam_item_create, name='echoExamItemCreate'),
    path('u_examitemlist/', uviews.u_exam_item_list, name='echoExamItemList'),
    path('u_examitemlistall/', uviews.u_exam_item_list_all, name='echoExamItemListAll'),
    path('u_examitemupdate/<int:id>', uviews.u_exam_item_update, name='echoExamItemUpdate'),
    path('u_resultcreate/', uviews.u_result_create, name='echoResultCreate'),
    path('u_resultlist/', uviews.u_result_list, name='echoResultList'),
    path('u_resultlistall/', uviews.u_result_list_all, name='echoResultListAll'),
    path('u_resultdetail/<int:id>', uviews.u_result_detail, name='echoResultDetail'),
    path('u_resultupdate/<int:id>', uviews.u_result_update, name='echoResultUpdate'),


    # ======================== Radio Views ==============================
    path('xray/', xviews.xrayHomeView, name='xrayHomeView'),
    path('x_patcreate/', xviews.x_patient_create, name='xrayPatCreate'),
    path('x_patlist/', xviews.x_patient_list, name='xrayPatList'),
    path('x_patdetail/<slug>', xviews.x_patient_detail, name='xrayPatDetail'),
    path('x_patdelete/', xviews.x_patient_delete, name='xrayPatDelete'),
    path('x_examcreate/', xviews.x_exam_create, name='xrayExamCreate'),
    path('x_examlist/', xviews.x_exam_list, name='xrayExamList'),
    path('x_examitemcreate/', xviews.x_exam_item_create, name='xrayExamItemCreate'),
    path('x_examitemlist/', xviews.x_exam_item_list, name='xrayExamItemList'),
    path('x_resultcreate/', xviews.x_result_create, name='xrayResultCreate'),
    path('x_resultlist/', xviews.x_result_list, name='xrayResultList'),
    path('x_resultdetail/<int:id>', xviews.x_result_detail, name='xrayResultDetail'),
    path('x_resultupdate/<int:id>', xviews.x_result_update, name='xrayResultUpdate'),

    # Echo Patient CRUD
    path('echoPatientCreate/', uviews.u_patient_create, name='echoPatientCreate'),  # get and post req. Create
    path('echoPatientList/', uviews.u_patient_list, name='echoPatientList'),        # get and post req. Retrieve and Display
    path('echoPatientDelete/<slug:un>/', uviews.u_patient_delete, name='echoPatientDelete'),   # get and post req. Delete
    path('echoPatientDetail/<slug:un>/', uviews.u_patient_detail, name='echoPatientDetail'),

    # ==================== ECHO SEARCHES ===================================================
    path('search_echo_test/', csrf_exempt(usearch.search_echo_test), name='search_echo_test'),
    path('search_echo_exam/', csrf_exempt(usearch.search_echo_exam), name='search_echo_exam'),
    path('search_patient/', csrf_exempt(usearch.search_patient), name='search_patient'),  # by phone or sn

    # ==================== XRAY SEARCHES ===================================================
    path('search_xray_test/', csrf_exempt(xsearch.search_xray_test), name='search_xray_test'),
    path('searchxray_exam/', csrf_exempt(xsearch.search_xray_exam), name='search_xray_exam'),
    path('search_patient/', csrf_exempt(usearch.search_patient), name='search_patient'),  # by phone or sn

    # ==================== ECHO STATISTICS ========================
    path('echo_exams_stats_0_this_month/', usearch.echo_exams_stats_0_this_month, name='ES_this_month'),
    path('echo_pats_chart_1_this_year/', usearch.echo_pats_chart_1_this_year, name='RUTS_this_1_Year'),
    path('echo_exams_chart_1_this_year/', usearch.echo_exams_chart_1_this_year, name='RUTS_this_1_Year'),
    path('echo_tests_stats_1_this_year/', usearch.echo_tests_stats_1_this_year, name='RUTS_this_1_Year'),
    path('echo_tests_stats_2_this_year/', usearch.echo_tests_stats_2_this_year, name='RUTS_this_2_Year'),

    # =================== NOTIFICATIONS ==========================
    path('notification_items/', usearch.notification_items, name='notification'),
    path('patNoExam/', usearch.pat_with_no_exam, name='PWNE_this_1_Year'),
    path('examNoTest/', usearch.exam_with_no_test, name='EWNT_this_1_Year'),
    path('obSexMale/', usearch.echo_exam_ob_male, name='OESM_this_1_Year'),
    path('skippedNumThis/', usearch.echo_skipped_number_this, name='ESN_this'),

    # ==================== XRAY STATISTICS ========================
    path('xray_pats_chart_1_this_year/', xsearch.xray_pats_chart_1_this_year, name='RXTS_this_1_Year'),
    # path('xray_pats_chart_1_this_year/', xsearch.xray_pats_chart_1_this_year, name='RXTS_this_1_Year'),

    path('xray_exams_chart_1_this_year/', xsearch.xray_exams_chart_1_this_year, name='RXTS_this_1_Year'),
    # path('xray_exams_chart_1_this_year/', xsearch.xray_exams_chart_1_this_year, name='RUTS_this_1_Year'),

    path('xray_tests_stats_1_this_year/', xsearch.xray_tests_stats_1_this_year, name='RXTS_this_1_Year'),
    path('xray_tests_stats_2_this_year/', xsearch.xray_tests_stats_2_this_year, name='RXTS_this_2_Year'),

    path('search_echo_patient/', csrf_exempt(usearch.search_echo_patient), name='search_echo_patient'),  # returns tests per category
    path('search_echo_exam/', csrf_exempt(usearch.search_echo_exam), name='search_echo_exam'),  # returns echo exams
    path('all_test_for_exam/<slug:book_num>/', usearch.all_test_for_exam, name='all_test_for_exam'),  # returns echo exams
    path('search_xray_patient/', csrf_exempt(xsearch.search_xray_patient), name='search_xray_patient'),  # returns tests per category
    path('validate_code/', csrf_exempt(usearch.validate_code), name='validate_code'),  # returns tests per category

    path('patCreateModalDetailU/<slug:book_num>/', views.patient_Create_Modal_Detail_u, name='PatCreateModalDetailU'),
    path('resCreateDetailModalU/', uviews.result_create_confirm_u, name='result_create_confirm_u'),

    path('checkRegNum/', csrf_exempt(usearch.check_regnum_exist), name='search_reg_num'),  # by phone or sn
    path('checkBookNum/', csrf_exempt(usearch.check_book_num_exist), name='search_book_num'),  # by phone or sn
    path('checkFullName/', csrf_exempt(usearch.check_full_name_exist), name='search_full_name'),  #
    path('check_test_exist_in_exam/', csrf_exempt(usearch.check_test_exist_in_exam), name='search_test_in_exam'),  # by phone or sn

    # =============== Print ======================
    path('u_this_month_stats/', print.u_this_month_stats, name='print_u_stats_this'),
    path('u_gen_stats/', print.u_gen_stats, name='generate_stats'),
    path('write_results/', uviews.write_results, name='write_results'),
    path('generate_report/', uviews.generate_report, name='generate_report'),

]
