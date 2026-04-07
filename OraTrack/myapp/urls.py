from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('log/',views.log,name="log"),
    path('patient_registration/',views.patient_registration,name="patient_registration"),
    path('login_action/',views.login_action,name="login_action"),
    path('patient_action/',views.patient_action,name="patient_action"),
    path("admin_home/", views.admin_home, name="admin_home"),
    path('admin_view_patient_requests/', views.admin_view_patient_requests, name='admin_view_patient_requests'),
    path('update_patient_status/<int:patient_id>/', views.update_patient_status, name='update_patient_status'),
    path("patient_home/",views.patient_home, name="patient_home"),
    path("common_logout/",views.common_logout, name="common_logout"),
    path("admin_add_department/",views.admin_add_department, name="admin_add_department"),
    path("admin_department_list/", views.admin_department_list, name="admin_department_list"),
    path("admin_add_doctor/",views.admin_add_doctor, name="admin_add_doctor"),
    path("doctor_home/",views.doctor_home, name="doctor_home"),
    path("admin_doctor_list/", views.admin_doctor_list, name="admin_doctor_list"),
   
    path("patient_health_details/", views.patient_health_details, name="patient_health_details"),
    path("view_health_details/",views.view_health_details, name="view_health_details"),
    path('book_appointment/',views.book_appointment,name='book_appointment'),
    path('view_appointments/',views.view_appointments,name='view_appointments'),
    path("doctor_appointments/", views.doctor_appointments, name="doctor_appointments"),
    path("admin_add_lab/", views.admin_add_lab, name="admin_add_lab"),
    path("lab_home/", views.lab_home, name="lab_home"),
    path('admin_view_labs/', views.admin_view_labs, name='admin_view_labs'),
    path('lab_add_and_view_tests/', views.lab_add_and_view_tests, name='lab_add_and_view_tests'),
    path("feedback/", views.feedback, name="feedback"),
    path("reply_feedback/", views.reply_feedback, name="reply_feedback"),
    path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
    path('admin_reply_complaint/', views.admin_reply_complaint, name='admin_reply_complaint'),
    path('edit_doctor_profile/', views.edit_doctor_profile, name='edit_doctor_profile'),
    path('update_doctor_profile/', views.update_doctor_profile, name='update_doctor_profile'),
    path('doctor_appointment_detail/<int:appointment_id>/', views.doctor_appointment_detail, name='doctor_appointment_detail'),
    path('patient_prescriptions/', views.patient_prescriptions, name='patient_prescriptions'),
    path('patient_prescription_detail/<int:appointment_id>/', views.patient_prescription_detail, name='patient_prescription_detail'),

path("approved_patient_list/", views.admin_approved_patient_list, name="approved_patient_list"),

path('consult/<int:appointment_id>/', views.consult, name='consult'),
path('save_clinical', views.save_clinical, name='save_clinical'),
path('predict/<int:appointment_id>/', views.prediction, name='predict'),
path('forward_to_lab_test/<int:appointment_id>/', views.forward_to_lab_test, name='forward_to_lab_test'),
path('ajax/load-lab-tests/', views.load_lab_tests, name='ajax_load_lab_tests'),
path('doctor_lab_tests', views.doctor_lab_tests, name='doctor_lab_tests'),

path('pending_tests', views.pending_tests, name='pending_tests'),
path('upload_reports', views.upload_reports, name='upload_reports'),
 path('processing_test/<int:test_id>/', views.processing_test, name='processing_test'),   

 path('upload_test_result/<int:test_id>/', views.upload_test_result, name='upload_test_result'),   
 path('test_history', views.test_history, name='test_history'),   
    
      path('forwared_to_oncology/<int:appointment_id>/', views.forwared_to_oncology, name='forwared_to_oncology'),
  
   path('oncology_cases', views.oncology_cases, name='oncology_cases'),     
   path('add_chemotherapy/<int:id>/', views.add_chemotherapy, name='add_chemotherapy'),
path('add_radiotherapy/<int:id>/', views.add_radiotherapy, name='add_radiotherapy'),

path('patient_details/<int:id>/', views.patient_details, name='patient_details'),
path('treatment_details/<int:id>/', views.treatment_details, name='treatment_details'),

   path('dr_appointment_history/',views.dr_appointment_history,name='dr_appointment_history'),
    path('doctor/todays_chemo/', views.todays_chemo, name='todays_chemo'),
     path('doctor/todays_radio/', views.todays_radio, name='tdays_radio'),
  # Today's sessions
    path('patient/todays_chemo/', views.p_todays_chemo, name='p_todays_chemo'),
    path('patient/todays_radio/', views.p_todays_radio, name='p_todays_radio'),

    # All sessions
    path('patient/all_chemo/', views.p_all_chemo, name='p_all_chemo'),
    path('patient/all_radio/', views.p_all_radio, name='p_all_radio'),

 path('message_to_doctor/',views.message_to_doctor,name='message_to_doctor'),

    path('message_from_patient/', views.message_from_patient, name='message_from_patient'),
path('reply_patient/<int:message_id>/', views.reply_patient, name='reply_patient'),



  # =============================
    path('appointments/', views.admin_appointments, name='admin_appointments'),
    path('appointments/pending/', views.admin_pending_appointments, name='admin_pending_appointments'),
    path('appointments/approved/', views.admin_approved_appointments, name='admin_approved_appointments'),

    # =============================
    # ONCOLOGY CASES
    # =============================
    path('oncology/', views.admin_oncology_cases, name='admin_oncology_cases'),
    path('oncology/confirmed/', views.admin_confirmed_cases, name='admin_confirmed_cases'),

    # =============================
    # TREATMENTS
    # =============================
    path('treatments/chemotherapy/', views.admin_chemo_list, name='admin_chemo_list'),
    path('treatments/radiotherapy/', views.admin_radio_list, name='admin_radio_list'),

    # =============================
    # MESSAGES
    # =============================
    path('messages/', views.admin_messages, name='admin_messages'),


    path('approval_appointments/', views.approval_appointments, name='approval_appointments'),

    path('search_appointments/', views.search_appointments, name='search_appointments'),

        path('search_appointments_today/', views.search_appointments_today, name='search_appointments_today'),
  path('search_appointments_history/', views.search_appointments_history, name='search_appointments_history'),
path('ajax/search_oncology_cases/', views.search_oncology_cases, name='search_oncology_cases'),
path('ajax/search_lab_tests/', views.search_lab_tests, name='search_lab_tests'),


path('ajax/search_completed_tests/', views.search_completed_tests, name='search_completed_tests'),
path('ajax/search_lab_tests_processing/', views.search_lab_tests_processing, name='search_lab_tests_processing'),

path('all_patient_details/', views.all_patient_details, name='all_patient_details'),



 path('emergency_to_doctor/',views.emergency_to_doctor,name='emergency_to_doctor'),

    path('emergency_message_patient/', views.emergency_message_patient, name='emergency_message_patient'),
path('reply_emergency_patient/<int:message_id>/', views.reply_emergency_patient, name='reply_emergency_patient'),

path('adm_patient_details/<int:id>/', views.adm_patient_details, name='adm_patient_details'),
    path('get-doctors/<int:department_id>/', views.get_doctors, name='get_doctors'),
 path('p_appointment_status/', views.view_appointments, name='p_appointment_status'),
   
]
