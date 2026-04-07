from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate
from datetime import date,datetime,timedelta
from django.contrib.auth import logout
from django.utils.timezone import now
from django.utils import timezone
import os
import joblib
import numpy as np
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Load model & scaler globally
MODEL_PATH = os.path.join(settings.BASE_DIR, "media", "detection", "oral_cancer_rf_model.pkl")
model = joblib.load(MODEL_PATH)  # <-- This is now the RandomForest model object

# Create your views here.
today = date.today()

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def log(request):
    return render(request,'login.html')


def patient_registration(request):
    return render(request,'patient_register.html')



def login_action(request):
    u = request.POST.get("username")
    p = request.POST.get("password")
    obj = authenticate(username=u, password=p)

    if obj is not None:
        if obj.is_superuser == 1:
            # Admin
            request.session['aname'] = u
            request.session['slogid'] = obj.id
            return redirect('admin_home')
        else:
            # Invalid user for non-admin
            messages.add_message(request, messages.INFO, 'Invalid User.')
            return redirect('log')
    else:
        newp = p
        try:
            obj1 = Login.objects.get(username=u, password=newp)

            if obj1.Usertype == "Patient":
                # User
                if obj1.status == "Approved":
                    request.session['pname'] = u
                    request.session['slogid'] = obj1.login_id
                    return redirect('patient_home')
                elif obj1.status == "Not Approved":
                    messages.add_message(request, messages.INFO, 'Waiting For Approval.')
                    return redirect('log')
                else:
                    messages.add_message(request, messages.INFO, 'Invalid User.')
                    return redirect('log')

            elif obj1.Usertype == "Doctor":
                # Staff
                if obj1.status == "Available":
                    request.session['dname'] = u
                    request.session['slogid'] = obj1.login_id
                    return redirect('doctor_home')
                elif obj1.status == "Available":
                    messages.add_message(request, messages.INFO, 'Waiting For Approval.')
                    return redirect('log')
                else:
                    messages.add_message(request, messages.INFO, 'Invalid User.')
                    return redirect('log')

            elif obj1.Usertype == "Lab":
                # Company
                if obj1.status == "Approved":
                    request.session['lname'] = u
                    request.session['slogid'] = obj1.login_id
                    return redirect('lab_home')
                elif obj1.status == "Approved":
                    messages.add_message(request, messages.INFO, 'Waiting For Approval.')
                    return redirect('log')
                else:
                    messages.add_message(request, messages.INFO, 'Invalid User.')
                    return redirect('log')

            else:
                messages.add_message(request, messages.INFO, 'Invalid User.')
                return redirect('log')

        except Login.DoesNotExist:
            messages.add_message(request, messages.INFO, 'Invalid User.')
            return redirect('log')
        



def admin_home(request):
    if 'aname' not in request.session:
        return redirect('log')

    context = {
        "patient_count": Patient.objects.count(),
        "doctor_count": Doctor.objects.count(),
        "department_count": DoctorDepartment.objects.count(),
        "appointment_count": Appointment.objects.count(),
        "pending_appointment_count": Appointment.objects.filter(status="Pending").count(),
        "approved_appointment_count": Appointment.objects.filter(status="Approved").count(),
        "lab_count": Lab.objects.count(),
        "lab_test_count": LabTest.objects.count(),
        "oncology_case_count": OncologyCase.objects.count(),
        "confirmed_case_count": OncologyCase.objects.filter(detection_status="Confirmed").count(),
        "chemo_count": Chemotherapy.objects.count(),
        "radio_count": Radiotherapy.objects.count(),
        "feedback_count": Feedback.objects.count(),
        "complaint_count": Complaint.objects.count(),
        "message_count": PatientDoctorMessage.objects.count(),
        "pending_message_count": PatientDoctorMessage.objects.filter(reply__isnull=True).count(),
    }

    return render(request, 'master/index.html', context)

    


def patient_action(request):
    if request.method == "POST":
        username = request.POST.get("username")

        # Check username exists
        if Login.objects.filter(username=username).exists():
            messages.add_message(request, messages.INFO, "Username already exists.")
            return redirect('patient_registration')

        # Create Login
        login = Login.objects.create(
            username=username,
            password=request.POST.get("password"),
            Usertype="Patient",
            status="Not Approved"
        )

        # Create Patient
        Patient.objects.create(
            login=login,
            name=request.POST.get("name"),
            age=request.POST.get("age"),
            gender=request.POST.get("gender"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            address=request.POST.get("address"),
            image=request.FILES.get("image") 
        )

        messages.add_message(request, messages.INFO, "Patient registered successfully.")
        return redirect('patient_registration')
    
    

def common_logout(request):
    logout(request)
    request.session.delete()
    return redirect('log')


from .models import OncologyCase

def patient_home(request):
    if 'pname' in request.session:
        patient_data = Patient.objects.get(login_id=request.session['slogid'])

        # Check if the patient has a confirmed cancer case
        has_cancer = OncologyCase.objects.filter(
            patient=patient_data,
            detection_status='Confirmed'
        ).exists()

        # Store the value in session
        request.session['has_cancer'] = has_cancer  # True or False

        return render(request, 'patient/index.html', {
            'patient_data': patient_data,
            'has_cancer': has_cancer
        })
    else:
        return redirect('log')


 
    
def admin_view_patient_requests(request):
    if 'aname' not in request.session:
        return redirect('log')

    # Show only patients whose login status is 'Not Approved'
    patients = Patient.objects.exclude(login__status="Approved")

    return render(request, 'master/admin_patient_requests.html', {'patients': patients})

    
def admin_approved_patient_list(request):
    if 'aname' not in request.session:
        return redirect('log')

    # Show only patients whose login status is 'Not Approved'
    patients = Patient.objects.filter(login__status="Approved")

    return render(request, 'master/admin_approved_patient_requests.html', {'patients': patients,'All':'All'})

def update_patient_status(request, patient_id):
    if 'aname' not in request.session:
        return redirect('log') 

    if request.method == "POST":
        action = request.POST.get('action')
        patient = get_object_or_404(Patient, patient_id=patient_id)
        login = patient.login

        if action == "Approved":
            login.status = "Approved"
        elif action == "Rejected":
            login.status = "Rejected"
        else:
            messages.error(request, "Invalid action.")
            return redirect('admin_view_patient_requests')

        login.save()
        messages.success(request, f"Patient '{patient.name}' status updated to {login.status}.")
        return redirect('admin_view_patient_requests')

    return redirect('admin_view_patient_requests')


def admin_add_department(request):
    if 'aname' not in request.session:
        return redirect('log')

    if request.method == "POST":
        DoctorDepartment.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        messages.success(request, "Department added successfully")
        return redirect('admin_add_department')

    return render(request, 'master/add_department.html')

def admin_department_list(request):
    if 'aname' not in request.session:
        return redirect('log')

    departments = DoctorDepartment.objects.all()

    return render(request, 'master/department_list.html', {
        'departments': departments
    })

def admin_edit_department(request, id):
    if 'aname' not in request.session:
        return redirect('log')

    department = DoctorDepartment.objects.get(department_id=id)

    if request.method == "POST":
        department.name = request.POST.get('name')
        department.description = request.POST.get('description')
        department.save()
        messages.success(request, "Department updated successfully")
        return redirect('admin_department_list')

    return render(request, 'master/edit_department.html', {'department': department})

def admin_delete_department(request, id):
    if 'aname' not in request.session:
        return redirect('log')

    DoctorDepartment.objects.filter(department_id=id).delete()
    messages.success(request, "Department deleted successfully")
    return redirect('admin_department_list')


def admin_add_doctor(request):
    if 'aname' not in request.session:
        return redirect('log')

    if request.method == "POST":
        department_id = request.POST.get('department')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validate department
        if not DoctorDepartment.objects.filter(department_id=department_id).exists():
            messages.info(request, "Selected department does not exist.")
            return redirect('admin_add_doctor')

        # Check if username already exists in Login
        if Login.objects.filter(username=username).exists():
            messages.info(request, "Username already taken.")
            return redirect('admin_add_doctor')

        # Create login for doctor
        login = Login.objects.create(
            username=username,
            password=password, 
            Usertype="Doctor",
            status="Available"
        )

        # Create doctor linked to login
        Doctor.objects.create(
            login=login,
            department_id=department_id,
            name=request.POST.get('name'),
            qualification=request.POST.get('qualification'),
            experience=request.POST.get('experience'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            image=request.FILES.get('image'),
            status='Available'
        )
        messages.success(request, "Doctor added successfully.")
        return redirect('admin_add_doctor')

    departments = DoctorDepartment.objects.all()
    return render(request, 'master/add_doctor.html', {
        'departments': departments
    })


def doctor_home(request):
    if 'dname' in request.session:
        doctor_data = Doctor.objects.select_related('department').get(
            login_id=request.session['slogid']
        )

        request.session['doctor_id'] = doctor_data.doctor_id
        request.session['department_name'] = doctor_data.department.name  # ✅ store department
        
        return render(request, 'doctor/index.html', {
            'doctor': doctor_data,
            'department_name': doctor_data.department.name
           
        })
    else:
        return redirect('log')



def admin_doctor_list(request):
    if 'aname' not in request.session:
        return redirect('log')

    doctors = Doctor.objects.select_related('department').all()
    return render(request, 'master/doctor_list.html', {
        'doctors': doctors
    })

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def edit_doctor(request, doctor_id):
    if 'aname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(Doctor, doctor_id=doctor_id)
    departments = DoctorDepartment.objects.all()

    if request.method == "POST":
        doctor.name = request.POST.get('name')
        doctor.phone = request.POST.get('phone')
        doctor.email = request.POST.get('email')
        doctor.qualification = request.POST.get('qualification')
        doctor.experience = request.POST.get('experience')
        doctor.status = request.POST.get('status')

        department_id = request.POST.get('department')
        if department_id:
            doctor.department = get_object_or_404(
                DoctorDepartment,
                department_id=department_id
            )

        if request.FILES.get('image'):
            doctor.image = request.FILES.get('image')

        doctor.save()
        messages.success(request, "Doctor updated successfully")
        return redirect('admin_doctor_list')

    return render(request, 'master/edit_doctor.html', {
        'doctor': doctor,
        'departments': departments
    })
def admin_delete_doctor(request, doctor_id):
    if 'aname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(Doctor, doctor_id=doctor_id)

    # delete linked login also
    doctor.login.delete()
    doctor.delete()

    messages.success(request, "Doctor deleted successfully")
    return redirect('admin_doctor_list')
def admin_add_lab(request):
    if 'aname' not in request.session:
        return redirect('log')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Login.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('admin_add_lab')

        login = Login.objects.create(
            username=username,
            password=password,   # plain password (as per your system)
            Usertype="Lab",
            status="Approved"
        )

        Lab.objects.create(
            login=login,
            lab_name=request.POST.get('lab_name'),
            license_number=request.POST.get('license_number'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            lab_type=request.POST.get('lab_type'),
        )

        messages.success(request, "Lab added and approved successfully")
        return redirect('admin_add_lab')

    return render(request, 'master/add_lab.html')



def edit_lab(request, lab_id):
    if 'aname' not in request.session:
        return redirect('log')

    lab = get_object_or_404(Lab, lab_id=lab_id)

    if request.method == "POST":
        lab.lab_name = request.POST.get('lab_name')
        lab.license_number = request.POST.get('license_number')
        lab.lab_type = request.POST.get('lab_type')
        lab.phone = request.POST.get('phone')
        lab.email = request.POST.get('email')
        lab.address = request.POST.get('address')

        lab.save()
        messages.success(request, "Lab updated successfully")
        return redirect('admin_view_labs')

    return render(request, 'master/edit_lab.html', {
        'lab': lab
    })
def delete_lab(request, lab_id):
    if 'aname' not in request.session:
        return redirect('log')

    lab = get_object_or_404(Lab, lab_id=lab_id)

    # delete login first
    lab.login.delete()
    lab.delete()

    messages.success(request, "Lab deleted successfully")
    return redirect('admin_view_labs')
def lab_home(request):
    if 'lname' in request.session:
        lab = Lab.objects.get(login_id=request.session['slogid'])
        request.session['lab_id'] = lab.lab_id

        # 🔹 Count Pending Tests
        pending_tests = PatientLabTest.objects.filter(
            lab_test__lab=lab,
            status='Pending'
        ).count()

        # 🔹 Count Completed Tests
        completed_tests = PatientLabTest.objects.filter(
            lab_test__lab=lab,
            status='Completed'
        ).count()

        context = {
            'lab': lab,
            'pending_tests': pending_tests,
            'completed_tests': completed_tests,
        }

        return render(request, 'lab/index.html', context)

    else:
        return redirect('log')

    
def admin_view_labs(request):
    if 'aname' not in request.session:
        return redirect('log')

    labs = Lab.objects.select_related('login').all().order_by('-registered_date')

    return render(request, 'master/view_labs.html', {
        'labs': labs
    }) 

def patient_health_details(request):
    if 'pname' not in request.session:
        return redirect('log')

    patient = Patient.objects.get(login__username=request.session['pname'])

    # 🔹 Get existing health details (if any)
    health = PatientHealthDetails.objects.filter(patient=patient).first()

    if request.method == 'POST':
        PatientHealthDetails.objects.update_or_create(
            patient=patient,
            defaults={
                'tobacco_use': request.POST.get('tobacco_use'),
                'alcohol_consumption': request.POST.get('alcohol_consumption'),
                'betel_quid_use': request.POST.get('betel_quid_use'),
                'sun_exposure': request.POST.get('sun_exposure'),
                'family_history': request.POST.get('family_history'),
                'immune_compromised': request.POST.get('immune_compromised'),
                'hpv_infection': request.POST.get('hpv_infection'),
                'lifestyle_habits': request.POST.get('lifestyle_habits'),
                'symptoms': request.POST.get('symptoms'),
                'poor_oral_hygiene': request.POST.get('poor_oral_hygiene'),
                'diet_intake': request.POST.get('diet_intake'),
            }
        )
        messages.success(request, "Health details saved successfully.")
        return redirect('patient_health_details')

    return render(
        request,
        'patient/health_details.html',
        {'health': health}
    )



def view_health_details(request):
    if 'pname' not in request.session:
        return redirect('log')

    patient = get_object_or_404(
        Patient,
        login__username=request.session['pname']
    )

    health_details = PatientHealthDetails.objects.filter(patient=patient).first()

    # DELETE
    if request.method == 'POST':
        if health_details:
            health_details.delete()
            messages.success(request, "Health details deleted successfully.")
        return redirect('view_health_details')

    return render(request, 'patient/view_health_details.html', {
        'health_details': health_details
    })


def book_appointment(request):
    if 'pname' not in request.session:
        return redirect('log')

    patient = get_object_or_404(
        Patient,
        login__username=request.session['pname']
    )

    # Patient health details (MANDATORY)
    health_details = PatientHealthDetails.objects.filter(patient=patient).first()
    if not health_details:
        messages.warning(request, "Please add your health details before booking an appointment.")
        return redirect('patient_health_details')

    departments = DoctorDepartment.objects.all()
    doctors = Doctor.objects.filter(status='Available')

    if request.method == 'POST':
        department_id = request.POST.get('department')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')

        department = get_object_or_404(DoctorDepartment, department_id=department_id)
        doctor = get_object_or_404(Doctor, doctor_id=doctor_id)

        Appointment.objects.create(
            patient=patient,
            department=department,
            doctor=doctor,
            health_details=health_details,
            appointment_date=date,
            appointment_time=time
        )

        messages.success(request, "Appointment booked successfully.")
        return redirect('book_appointment')

    return render(request, 'patient/book_appointment.html', {
        'departments': departments,
        'doctors': doctors,
        'health_details': health_details
    })


def view_appointments(request):
    if 'pname' not in request.session:
        return redirect('log')

    patient = get_object_or_404(
        Patient,
        login__username=request.session['pname']
    )

    appointments = Appointment.objects.filter(
        patient=patient
    ).select_related('doctor', 'department').order_by('-created_at')

    return render(request, 'patient/view_appointments.html', {
        'appointments': appointments
    })
    
def doctor_appointments(request):
    if 'dname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(Doctor, login__username=request.session['dname'])

    # if request.method == "POST":
    #     appointment_id = request.POST.get('appointment_id')

    #     # Update appointment status
    #     if 'update_status' in request.POST:
    #         new_status = request.POST.get('status')
    #         appointment = get_object_or_404(Appointment, appointment_id=appointment_id, doctor=doctor)

    #         if new_status in ['Pending', 'Approved', 'Rejected']:
    #             appointment.status = new_status
    #             appointment.save()
    #             messages.success(request, f"Appointment status updated to {new_status}.")
    #         else:
    #             messages.error(request, "Invalid status selected.")

    #         return redirect('doctor_appointments')

    #     # Save Clinical Examination and Prescription
       
    today = timezone.localdate()
    appointments = Appointment.objects.filter(
        doctor=doctor,
        appointment_date=today,
        status='Approved'
    ).select_related('patient', 'health_details', 'clinical', 'prescription').order_by('appointment_time')

    return render(request, 'doctor/appointments.html', {
        'appointments': appointments,
    })
    
def approval_appointments(request):
    if 'dname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(Doctor, login__login_id=request.session['slogid'])

    if request.method == "POST":
        appointment_id = request.POST.get('appointment_id')

        # Update appointment status
        if 'update_status' in request.POST:
            new_status = request.POST.get('status')
            appointment = get_object_or_404(Appointment, appointment_id=appointment_id, doctor=doctor)

            if new_status in ['Pending', 'Approved', 'Rejected']:
                appointment.status = new_status
                appointment.save()
                messages.success(request, f"Appointment status updated to {new_status}.")
            else:
                messages.error(request, "Invalid status selected.")

            return redirect('approval_appointments')

        # Save Clinical Examination and Prescription
       
  
    appointments = Appointment.objects.filter(
        doctor=doctor,status='Pending',
         appointment_date__gte=today
    ).select_related('patient', 'health_details', 'clinical', 'prescription').order_by('appointment_time')

    return render(request, 'doctor/approval_appointments.html', {
        'appointments': appointments,
    })



def doctor_appointment_detail(request, appointment_id):
    if 'dname' not in request.session:
        return redirect('log')

    appointment = get_object_or_404(
        Appointment.objects.select_related('patient', 'health_details', 'clinical', 'prescription'),
        appointment_id=appointment_id,
        doctor__login__username=request.session['dname']
    )

    return render(request, 'doctor/appointment_detail.html', {
        'appointment': appointment
    })
    
    
    
def lab_add_and_view_tests(request):
    if 'lname' not in request.session:
        return redirect('log')

    lab = Lab.objects.get(login_id=request.session['slogid'])

    if request.method == "POST":
        test_name = request.POST.get('test_name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        LabTest.objects.create(
            lab=lab,
            test_name=test_name,
            description=description,
            price=price
        )

        messages.success(request, "Test added successfully")
        return redirect('lab_add_and_view_tests')

    tests = LabTest.objects.filter(lab=lab).order_by('-created_at')

    return render(request, 'lab/add_test.html', {
        'tests': tests
    })
    
    

def feedback(request):
    if 'pname' not in request.session:
        return redirect('log')  # Redirect to login if the session does not contain 'uname'

    try:
        patient = Patient.objects.get(login_id=request.session['slogid'])
    except Patient.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('log')

    if request.method == 'POST':
        feedback_text = request.POST.get("feedback")
        if feedback_text:
            # Create a new feedback entry
            Feedback.objects.create(
                feedback=feedback_text,
                date=now(),
                patient=patient
            )
            messages.success(request, 'Feedback submitted successfully!')
            return redirect('feedback')  # Redirect to avoid re-submission on refresh
        else:
            messages.error(request, 'Feedback cannot be empty!')

    data = Feedback.objects.filter(patient=patient).order_by('-date') 
    return render(request, 'patient/feedback.html', {'data': data})


def reply_feedback(request):
    if 'aname' in request.session:
        if request.method == 'POST':
            fd_id = request.POST.get('fd_id')
            reply = request.POST.get('reply')
            
            Feedback.objects.filter(fd_id=fd_id).update(reply=reply)
            messages.success(request, 'Reply submitted successfully.')
            return redirect('reply_feedback') 
            
        else:
            data = Feedback.objects.all() 
            return render(request, 'master/feedback_view.html', {'data': data})
    else:
        return redirect('log')
    

def submit_complaint(request):
    if 'pname' not in request.session:
        return redirect('log')

    try:
        patient = Patient.objects.get(login_id=request.session['slogid'])
    except Patient.DoesNotExist:
        messages.error(request, "Patient not found.")
        return redirect('log')

    if request.method == 'POST':
        complaint_text = request.POST.get('complaint')

        if complaint_text:
            Complaint.objects.create(
                patient=patient,
                complaint=complaint_text
            )
            messages.success(request, "Complaint submitted successfully.")
            return redirect('submit_complaint')
        else:
            messages.error(request, "Complaint cannot be empty.")

    data = Complaint.objects.filter(patient=patient).order_by('-date')
    return render(request, 'patient/complaint.html', {'data': data})


def admin_reply_complaint(request):
    if 'aname' not in request.session:
        return redirect('log')

    if request.method == 'POST':
        complaint_id = request.POST.get('complaint_id')
        reply = request.POST.get('reply')

        Complaint.objects.filter(complaint_id=complaint_id).update(reply=reply)
        messages.success(request, "Reply sent successfully.")
        return redirect('admin_reply_complaint')

    data = Complaint.objects.all().order_by('-date')
    return render(request, 'master/complaint_view.html', {'data': data})


def edit_doctor_profile(request):
    if 'dname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(Doctor, login_id=request.session['slogid'])
    return render(request, 'doctor/profile.html', {'doctor': doctor})

def update_doctor_profile(request):
    if 'dname' not in request.session:
        return redirect('log')

    doctor = Doctor.objects.get(doctor_id=request.POST.get('doctor_id'))

    doctor.name = request.POST.get('name')
    doctor.qualification = request.POST.get('qualification')
    doctor.experience = request.POST.get('experience')
    doctor.phone = request.POST.get('phone')
    doctor.email = request.POST.get('email')
    doctor.status = request.POST.get('status')

    if request.FILES.get('image'):
        doctor.image = request.FILES.get('image')

    doctor.save()
    messages.success(request, "Profile updated successfully")
    return redirect('edit_doctor_profile')


def patient_prescriptions(request):
    if 'pname' not in request.session:
        return redirect('log')

    patient = get_object_or_404(Patient, login__login_id=request.session['slogid'])
    # Get all appointments with prescriptions for this patient
    appointments = Appointment.objects.filter(
    patient=patient
).exclude(
    status='Pending'
).select_related('prescription').order_by('-appointment_date')

    return render(request, 'patient/prescriptions.html', {
        'appointments': appointments
    })


def patient_prescription_detail(request, appointment_id):
    if 'pname' not in request.session:
        return redirect('log')

    patient = get_object_or_404(Patient, login__username=request.session['pname'])
    appointment = get_object_or_404(
    Appointment,
    Q(appointment_id=appointment_id) &
    Q(patient=patient) &
    ~Q(status='Pending')
)
    prescription = getattr(appointment, 'prescription', None)
    lab_tests = PatientLabTest.objects.filter(
        appointment=appointment
    ).select_related('lab_test', 'lab_test__lab')
    return render(request, 'patient/prescription_detail.html', {
        'appointment': appointment,
        'prescription': prescription,
        'lab_tests':lab_tests
    })

def consult(request, appointment_id):
    if 'dname' not in request.session:
        return redirect('login')

    appointment = get_object_or_404(
        Appointment,
        appointment_id=appointment_id
    )

    if appointment.status != 'Approved':
        messages.error(request, "Consultation is not approved yet.")
        return redirect('doctor_appointments')

    # 🔹 Attach existing clinical & prescription if available
    appointment.clinical = ClinicalExamination.objects.filter(
        appointment=appointment
    ).first()

    appointment.prescription = Prescription.objects.filter(
        appointment=appointment
    ).first()

    return render(request, 'doctor/consult.html', {
        'appt': appointment,  'today': date.today().isoformat()
    })





def save_clinical(request):
    if 'dname' not in request.session:
        return redirect('login')
    if request.method == "POST":

        appointment_id = request.POST.get("appointment_id")
        appointment = get_object_or_404(Appointment, pk=appointment_id)

        # =========================
        # 🔹 CLINICAL EXAMINATION
        # =========================
        clinical, _ = ClinicalExamination.objects.get_or_create(
            appointment=appointment
        )

        clinical.symptoms = request.POST.get("symptoms")

        # Checkboxes → True/False
        clinical.oral_lesions = "oral_lesions" in request.POST
        clinical.unexplained_bleeding = "unexplained_bleeding" in request.POST
        clinical.difficulty_swallowing = "difficulty_swallowing" in request.POST
        clinical.white_red_patches = "white_red_patches" in request.POST

        # Pain intensity (nullable int)
        pain = request.POST.get("pain_intensity")
        clinical.pain_intensity = int(pain) if pain else None

        # Ulcer duration
        clinical.ulcer_duration = request.POST.get("ulcer_duration")

        clinical.save()

        # =========================
        # 🔹 PRESCRIPTION
        # =========================
        prescription, _ = Prescription.objects.get_or_create(
            appointment=appointment
        )

        prescription.diagnosis = request.POST.get("diagnosis")
        prescription.medicine_details = request.POST.get("medicine_details")
        prescription.medicine_usage = request.POST.get("medicine_usage")
        prescription.more_details = request.POST.get("more_details")

        next_visit = request.POST.get("next_visit_date")
        prescription.next_visit_date = next_visit if next_visit else None

        prescription.save()

        return redirect("doctor_appointments")







def prediction(request, appointment_id):
    if 'dname' not in request.session:
        return redirect('login')
    # Fetch appointment and related data
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    patient_health = get_object_or_404(PatientHealthDetails, patient=appointment.patient)
    clinical = getattr(appointment, "clinical", None)

    if not clinical:
        return render(request, "doctor/prediction_result.html", {"error": "No clinical data."})

    # Helper to convert Yes/No to 1/0
    def yn(value):
        return 1 if value == "Yes" else 0

    # Gender: Female=0, Male=1
    gender = 1 if appointment.patient.gender == "Male" else 0
    age = appointment.patient.age

    # PatientHealthDetails features
    tobacco = yn(patient_health.tobacco_use)
    alcohol = yn(patient_health.alcohol_consumption)
    hpv = yn(patient_health.hpv_infection)
    betel = yn(patient_health.betel_quid_use)
    sun = yn(patient_health.sun_exposure)
    hygiene = yn(patient_health.poor_oral_hygiene)
    diet_map = {"Low": 0, "Moderate": 1, "High": 2}
    diet = diet_map.get(patient_health.diet_intake, 0)
    family = yn(patient_health.family_history)
    immune = yn(patient_health.immune_compromised)

    # ClinicalExamination features
    lesions = int(clinical.oral_lesions)
    bleeding = int(clinical.unexplained_bleeding)
    swallow = int(clinical.difficulty_swallowing)
    patches = int(clinical.white_red_patches)

    # Arrange features in the same order as training (15 features)
    features = np.array([[
        age, gender, tobacco, alcohol, hpv,
        betel, sun, hygiene, diet,
        family, immune, lesions,
        bleeding, swallow, patches
    ]])

    # Predict
    prediction = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1]

    result_text = "High Risk of Oral Cancer" if prediction == 1 else "Low Risk"
    prob_text = f"{prob*100:.2f}% probability"

    # Prepare patient info for display
    patient_values = {
        "Age": age,
        "Gender": appointment.patient.gender,
        "Tobacco Use": patient_health.tobacco_use,
        "Alcohol Consumption": patient_health.alcohol_consumption,
        "HPV Infection": patient_health.hpv_infection,
        "Betel Quid Use": patient_health.betel_quid_use,
        "Chronic Sun Exposure": patient_health.sun_exposure,
        "Poor Oral Hygiene": patient_health.poor_oral_hygiene,
        "Diet Intake": patient_health.diet_intake,
        "Family History": patient_health.family_history,
        "Immune Compromised": patient_health.immune_compromised,
        "Oral Lesions": "Yes" if lesions else "No",
        "Unexplained Bleeding": "Yes" if bleeding else "No",
        "Difficulty Swallowing": "Yes" if swallow else "No",
        "White/Red Patches": "Yes" if patches else "No"
    }

    return render(request, "doctor/prediction_result.html", {
        "patient_values": patient_values,
        "result_text": result_text,
        "prob_text": prob_text,
        "appointment": appointment
    })




def forward_to_lab_test(request, appointment_id):
    if 'dname' not in request.session:
        return redirect('login')
    # 🔹 Get appointment and related patient
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    patient = appointment.patient
    labs = Lab.objects.all()

    if request.method == "POST":
        # Get selected tests as a list of IDs
        selected_tests = request.POST.getlist("tests")

        # Create PatientLabTest entries
        for test_id in selected_tests:
            lab_test = get_object_or_404(LabTest, pk=test_id)
            PatientLabTest.objects.create(
                patient=patient,
                lab_test=lab_test,
                appointment=appointment
            )

        # 🔹 Update appointment status to "Forwarded to Lab"
        appointment.status = "Forwarded to Lab"
        appointment.save()

        return redirect('doctor_lab_tests')  # Redirect to the patient's lab tests page

    return render(request, "doctor/forward_to_lab_test.html", {
        "labs": labs,
        "appointment": appointment
    })


def load_lab_tests(request):
    lab_id = request.GET.get("lab_id")
    if not lab_id:
        return JsonResponse({"tests": []})

    # Fetch tests for the selected lab
    tests = LabTest.objects.filter(lab_id=lab_id).values(
        "test_id", "test_name", "description", "price"
    )

    # Return JSON with key 'tests' so front-end can access data.tests
    return JsonResponse({"tests": list(tests)})

def doctor_lab_tests(request):
    if 'dname' not in request.session:
        return redirect('login')

    doctor = Doctor.objects.get(login_id=request.session['slogid'])

    # Fetch all lab tests for this doctor's appointments, prefetch related oncology cases
    lab_tests = PatientLabTest.objects.select_related(
        'patient', 'appointment', 'lab_test', 'lab_test__lab'
    ).prefetch_related(
        'appointment__oncology_case'
    ).filter(
        appointment__doctor=doctor
    ).order_by('-appointment__appointment_date')

    # Group lab tests by patient
    patients_dict = {}
    for test in lab_tests:
        patient_id = test.patient.patient_id
        if patient_id not in patients_dict:
            patients_dict[patient_id] = {
                'patient': test.patient,
                'appointments': {}
            }

        appt_id = test.appointment.appointment_id
        if appt_id not in patients_dict[patient_id]['appointments']:
            # Include a flag if appointment already forwarded to oncology
            forwarded = OncologyCase.objects.filter(
              patient=test.patient
    ).exists()

            patients_dict[patient_id]['appointments'][appt_id] = {
                'appointment': test.appointment,
                'tests': [],
                'forwarded_to_oncology': forwarded
            }

        patients_dict[patient_id]['appointments'][appt_id]['tests'].append(test)

    context = {
        'patients': patients_dict.values()
    }

    return render(request, 'doctor/doctor_lab_tests.html', context)
# views.py




def pending_tests(request):
    if 'lname' not in request.session:
        return redirect('login')

    lab = get_object_or_404(
        Lab,
        login__login_id=request.session['slogid']
    )

    tests = PatientLabTest.objects.filter(
        lab_test__lab=lab,
        status='Pending'
    ).select_related(
        'patient',
        'lab_test',
        'appointment'
    ).order_by('-created_at')

    return render(request, 'lab/pending_tests.html', {
        'tests': tests
    })

def upload_reports(request):
    if 'lname' not in request.session:
        return redirect('login')

    lab = get_object_or_404(
        Lab,
        login__login_id=request.session['slogid']
    )

    tests = PatientLabTest.objects.filter(
        lab_test__lab=lab,
        status='Processing'
    ).select_related(
        'patient',
        'lab_test',
        'appointment'
    ).order_by('-created_at')

    return render(request, 'lab/upload_reports.html', {
        'tests': tests
    })


def processing_test(request, test_id):
    if 'lname' not in request.session:
        return redirect('login')

    test = get_object_or_404(PatientLabTest, pk=test_id)

    test.status = "Processing"
    test.save()

    messages.warning(request, "Test is now under processing.")

    return redirect('pending_tests')  # 👈 redirect to pending tests page

def upload_test_result(request, test_id):
    if 'lname' not in request.session:
        return redirect('login')

    test = get_object_or_404(PatientLabTest, pk=test_id)

    if request.method == "POST":

        if len(request.FILES) != 0:
            report = request.FILES['report_file']

            # Get file extension
            split_tup = os.path.splitext(report.name)
            file_extension = split_tup[1]

            # Save inside lab_reports folder
            upload_path = os.path.join(settings.MEDIA_ROOT, "lab_reports")

            # Create folder if not exists
            if not os.path.exists(upload_path):
                os.makedirs(upload_path)

            # Count existing files
            count = 0
            for path in os.listdir(upload_path):
                if os.path.isfile(os.path.join(upload_path, path)):
                    count += 1

            filecount = count + 1

            # Create new filename
            filename = str(filecount) + file_extension

            # Save file
            fs = FileSystemStorage(location=upload_path)
            file = fs.save(filename, report)

            # Save relative path to model
            test.report_file = "lab_reports/" + file
            test.status = "Completed"
            test.save()

            return redirect('upload_reports')

    return render(request, 'lab/upload_result.html', {'test': test})
def test_history(request):
    if 'lname' not in request.session:
        return redirect('login')

    lab = get_object_or_404(
        Lab,
        login__login_id=request.session['slogid']
    )

    tests = PatientLabTest.objects.filter(
        lab_test__lab=lab,
        status='Completed'
    ).select_related(
        'patient',
        'lab_test',
        'appointment'
    ).order_by('-created_at')

    return render(request, 'lab/test_history.html', {
        'tests': tests
    })



def forwared_to_oncology(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)

    # Get only Oncology department doctors
    oncology_doctors = Doctor.objects.filter(
        department__name="Oncology",
        status="Available"
    )

    if request.method == "POST":
        doctor_id = request.POST.get("doctor")
        selected_doctor = Doctor.objects.get(pk=doctor_id)

        # Update appointment doctor & department
        appointment.doctor = selected_doctor
        appointment.department = selected_doctor.department
        appointment.save()

        return redirect("doctor_lab_tests")

    return render(request, "doctor/forward_oncology.html", {
        "appointment": appointment,
        "oncology_doctors": oncology_doctors
    })
def forwared_to_oncology(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)

    oncology_doctors = Doctor.objects.filter(
        department__name="Oncology",
        status="Available"
    )

    if request.method == "POST":
        doctor_id = request.POST.get("doctor")
        new_date = request.POST.get("appointment_date")
        new_time = request.POST.get("appointment_time")

        selected_doctor = Doctor.objects.get(pk=doctor_id)

        # ✅ Create new Oncology appointment
        new_appointment = Appointment.objects.create(
            patient=appointment.patient,
            doctor=selected_doctor,
            department=selected_doctor.department,
            health_details=appointment.health_details,
            appointment_date=new_date,
            appointment_time=new_time,
            status="Approved"
        )

        # ✅ Store Confirmed Oncology Case
        OncologyCase.objects.create(
            appointment=new_appointment,
            patient=new_appointment.patient,
            doctor=selected_doctor,
            detection_status="Confirmed"
        )
        appointment.status="Forwarded to Oncology"
        appointment.save()
        return redirect("doctor_lab_tests")

    return render(request, "doctor/forward_oncology.html", {
        "appointment": appointment,
        "oncology_doctors": oncology_doctors
    })
def oncology_cases(request):
    if 'dname' not in request.session:
        return redirect('login')

    doctor = Doctor.objects.get(login_id=request.session['slogid'])

    # Only cases for this doctor
    cases = OncologyCase.objects.select_related(
        'patient',
        'appointment'
    ).filter(
        doctor=doctor
    ).order_by('-created_at')

    return render(request, 'doctor/oncology_cases.html', {
        'cases': cases,
        'doctor': doctor
    })


def add_chemotherapy(request, id):
    appointment = get_object_or_404(Appointment, pk=id)

    # Get existing chemo sessions for this appointment
    existing_chemo = Chemotherapy.objects.filter(
        appointment=appointment
    ).order_by('-chemo_date')

    # If already exists and last date is in future → block new entry
    if existing_chemo.exists():
        last_chemo = existing_chemo.first()  # latest date

        if last_chemo.chemo_date >= date.today():
            messages.warning(request, "Chemotherapy already scheduled. Cannot add new sessions until last date is completed.")

            return render(request, 'doctor/chemo_list.html', {
                'appointment': appointment,
                'chemo_list': existing_chemo
            })

    # Normal POST logic
    if request.method == "POST":

        session_no = request.POST.get('session_no')

        if not session_no:
            messages.error(request, "Session number required")
            return redirect(request.path)

        session_no = int(session_no)

        drug_name = request.POST.get('drug_name')
        dosage = request.POST.get('dosage')
        chemo_dates = request.POST.getlist('chemo_dates')

        # Validate count
        if len(chemo_dates) != session_no:
            messages.error(request, "Number of dates must match session number")
            return redirect(request.path)

        # Validate past dates
        for d in chemo_dates:
            if date.fromisoformat(d) < date.today():
                messages.error(request, "Past dates are not allowed")
                return redirect(request.path)

        # Save
        for d in chemo_dates:
            Chemotherapy.objects.create(
                appointment=appointment,
                session_no=session_no,
                drug_name=drug_name,
                dosage=dosage,
                chemo_date=d
            )

        messages.success(request, "Chemotherapy sessions added successfully")
        return redirect('doctor_appointments')

    return render(request, 'doctor/add_chemotherapy.html', {
        'appointment': appointment
    })


def add_radiotherapy(request, id):
    appointment = get_object_or_404(Appointment, pk=id)

    # Existing sessions
    existing_radio = Radiotherapy.objects.filter(
        appointment=appointment
    ).order_by('-radio_date')   # ✅ updated

    # Block if last session not completed
    if existing_radio.exists():
        last_radio = existing_radio.first()

        if last_radio.radio_date >= date.today():   # ✅ updated
            messages.warning(
                request,
                "Radiotherapy already scheduled. Cannot add new sessions until last session is completed."
            )

            return render(request, 'doctor/radio_list.html', {
                'appointment': appointment,
                'radio_list': existing_radio,
                'patient': appointment.patient
            })

    if request.method == "POST":

        session_no = request.POST.get('session_no')

        if not session_no:
            messages.error(request, "Session number required")
            return redirect(request.path)

        session_no = int(session_no)

        radiation_type = request.POST.get('radiation_type')
        dose = request.POST.get('dose')
        radio_dates = request.POST.getlist('radio_dates[]')

        # Validate session count
        if len(radio_dates) != session_no:
            messages.error(request, "Number of dates must match session number")
            return redirect(request.path)

        # Validate past dates
        for d in radio_dates:
            if date.fromisoformat(d) < date.today():
                messages.error(request, "Past dates are not allowed")
                return redirect(request.path)

        # Save each session
        for d in radio_dates:
            Radiotherapy.objects.create(
                appointment=appointment,
                session_no=session_no,
                radiation_type=radiation_type,
                dose=dose,
                radio_date=d   # ✅ updated
            )

        messages.success(request, "Radiotherapy sessions added successfully")
        return redirect('doctor_appointments')

    return render(request, 'doctor/add_radiotherapy.html', {
        'appointment': appointment
    })

def patient_details(request, id):

    patient = get_object_or_404(Patient, pk=id)

    health_details = PatientHealthDetails.objects.filter(patient=patient).first()
    appointments = Appointment.objects.filter(patient=patient).order_by('-appointment_date')
    oncology_cases = OncologyCase.objects.filter(patient=patient)

    lab_tests = PatientLabTest.objects.filter(patient=patient)
    feedbacks = Feedback.objects.filter(patient=patient)
    complaints = Complaint.objects.filter(patient=patient)

    context = {
        'patient': patient,
        'health': health_details,
        'appointments': appointments,
        'oncology_cases': oncology_cases,
        'lab_tests': lab_tests,
        'feedbacks': feedbacks,
        'complaints': complaints,
    }

    return render(request, 'doctor/patient_report.html', context)




def treatment_details(request, id):
    patient = get_object_or_404(Patient, pk=id)

    oncology_case = OncologyCase.objects.filter(patient=patient).first()
    appointments = Appointment.objects.filter(patient=patient).order_by('-appointment_date')
    lab_tests = PatientLabTest.objects.filter(patient=patient)

    context = {
        'patient': patient,
        'oncology_case': oncology_case,
        'appointments': appointments,
        'lab_tests': lab_tests,
    }

    return render(request, 'doctor/treatment_details.html', context)

def dr_appointment_history(request):
    if 'dname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(
        Doctor,
        login__username=request.session['dname']
    )

    appointments = Appointment.objects.filter(
        doctor=doctor,status='Approved',appointment_date__lte=today
    ).order_by('-appointment_date', '-appointment_time')

    context = {
        'doctor': doctor,
        'appointments': appointments
    }

    return render(request, 'doctor/dr_appointment_history.html', context)


def todays_chemo(request):
    if 'dname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(
        Doctor,
        login__login_id=request.session['slogid']
    )

    today = now().date()

    chemo_sessions = Chemotherapy.objects.filter(
        appointment__doctor=doctor,
        chemo_date=today
    ).order_by('chemo_date')

    context = {
        'chemo_sessions': chemo_sessions,
        'today': today
    }

    return render(request, 'doctor/todays_chemo.html', context)
def todays_radio(request):
    if 'dname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(Doctor, login__login_id=request.session['slogid'])
    today = now().date()

    radio_sessions = Radiotherapy.objects.filter(
        appointment__doctor=doctor,
        radio_date=today
    )

    context = {
        'radio_sessions': radio_sessions,
        'today': today
    }

    return render(request, 'doctor/todays_radio.html', context)

def dr_all_chemo(request):
    if 'dname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(
        Doctor,
        login__login_id=request.session['slogid']
    )

    today = now().date()

    chemo_sessions = Chemotherapy.objects.filter(
        appointment__doctor=doctor,
       
    ).order_by('chemo_date')

    context = {
        'chemo_sessions': chemo_sessions,
        'today': today
    }

    return render(request, 'doctor/all_chemo.html', context)
def dr_all_radio(request):
    if 'dname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(Doctor, login__login_id=request.session['slogid'])
    today = now().date()

    radio_sessions = Radiotherapy.objects.filter(
        appointment__doctor=doctor,
       
    )

    context = {
        'radio_sessions': radio_sessions,
        'today': today
    }

    return render(request, 'doctor/all_radio.html', context)



# Today's Chemotherapy
def p_todays_chemo(request):
    if 'pname' not in request.session:
        return redirect('log')
    patient = get_object_or_404(Patient, login_id=request.session['slogid'])
    today = now().date()
    chemo_sessions = Chemotherapy.objects.filter(
        appointment__patient=patient,
        chemo_date=today
    )
    return render(request, 'patient/p_todays_chemo.html', {'chemo_sessions': chemo_sessions, 'today': today})

# Today's Radiotherapy
def p_todays_radio(request):
    if 'pname' not in request.session:
        return redirect('log')
    patient = get_object_or_404(Patient, login_id=request.session['slogid'])
    today = now().date()
    radio_sessions = Radiotherapy.objects.filter(
        appointment__patient=patient,
        radio_date=today
    )
    return render(request, 'patient/p_todays_radio.html', {'radio_sessions': radio_sessions, 'today': today})

# All Chemotherapy
def p_all_chemo(request):
    if 'pname' not in request.session:
        return redirect('log')
    patient = get_object_or_404(Patient, login_id=request.session['slogid'])
    chemo_sessions = Chemotherapy.objects.filter(
        appointment__patient=patient
    ).order_by('chemo_date')
    return render(request, 'patient/p_all_chemo.html', {'chemo_sessions': chemo_sessions})

# All Radiotherapy
def p_all_radio(request):
    if 'pname' not in request.session:
        return redirect('log')
    patient = get_object_or_404(Patient, login_id=request.session['slogid'])
    radio_sessions = Radiotherapy.objects.filter(
        appointment__patient=patient
    ).order_by('radio_date')
    return render(request, 'patient/p_all_radio.html', {'radio_sessions': radio_sessions})



def message_to_doctor(request):
    if 'pname' not in request.session:
        return redirect('log')

    # Get patient
    patient = get_object_or_404(Patient, login_id=request.session['slogid'])

    # Get all doctors who have confirmed oncology cases for this patient
    consulted_doctors = Doctor.objects.filter(
        oncologycase__patient=patient,
        oncologycase__detection_status='Confirmed'
    ).distinct()

    if request.method == "POST":
        doctor_id = request.POST.get('doctor_id')
        message_text = request.POST.get('message')

        doctor = get_object_or_404(Doctor, pk=doctor_id)

        # Save message
        PatientDoctorMessage.objects.create(
            patient=patient,
            doctor=doctor,
            message=message_text
        )

        return redirect('message_to_doctor')  # refresh page
    messages_list = PatientDoctorMessage.objects.filter(patient=patient)
    return render(request, 'patient/message_to_doctor.html', {
        'consulted_doctors': consulted_doctors,
        'patient': patient,
        'messages_list':messages_list
    })
def message_from_patient(request):
    if 'dname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(Doctor, login_id=request.session['slogid'])

    # Get all messages sent to this doctor
    messages_list = PatientDoctorMessage.objects.filter(doctor=doctor)

    return render(request, 'doctor/message_from_patient.html', {
        'messages_list': messages_list
    })
def reply_patient(request, message_id):
    if 'dname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(Doctor, login_id=request.session['slogid'])
    message = get_object_or_404(PatientDoctorMessage, pk=message_id, doctor=doctor)

    if request.method == "POST":
        reply_text = request.POST.get('reply')

        message.reply = reply_text
        message.status = "Replied"
        message.save()

        return redirect('message_from_patient')

    return render(request, 'doctor/reply_patient.html', {
        'message': message
    })



def admin_appointments(request):
    search = request.GET.get("search")

    appointments = Appointment.objects.all().order_by('-appointment_id')

    if search:
        appointments = appointments.filter(
            Q(patient__name__icontains=search) |
            Q(doctor__name__icontains=search)
        )



    return render(request, "master/appointments.html", {
        "appointments": appointments,'type':'All'
    })



def admin_pending_appointments(request):
    appointments = Appointment.objects.filter(
        status="Pending"
    ).order_by('-appointment_id')

    return render(request, "master/appointments.html", {
        "appointments": appointments, 'type':'Pending'
    })



def admin_approved_appointments(request):
    appointments = Appointment.objects.filter(
        status="Approved"
    ).order_by('-appointment_id')

    return render(request, "master/appointments.html", {
        "appointments": appointments,'type':'Approved'
    })


# =============================
# ❤️ ONCOLOGY CASES
# =============================


def admin_oncology_cases(request):
    cases = OncologyCase.objects.all().order_by('-oncology_case_id')

    return render(request, "master/oncology_cases.html", {
        "cases": cases
    })



def admin_confirmed_cases(request):
    cases = OncologyCase.objects.filter(
        detection_status="Confirmed"
    ).order_by('-oncology_case_id')

    return render(request, "master/oncology_cases.html", {
        "cases": cases
    })


# =============================
# 💉 TREATMENTS
# =============================


def admin_chemo_list(request):
    chemo = Chemotherapy.objects.all().order_by('-chemo_id')

    return render(request, "master/chemo_list.html", {
        "chemos": chemo
    })



def admin_radio_list(request):
    radio = Radiotherapy.objects.all().order_by('-radio_id')

    return render(request, "master/radio_list.html", {
        "radios": radio
    })


# =============================
# 💬 MESSAGES
# =============================


def admin_messages(request):
    messages = PatientDoctorMessage.objects.all().order_by('-message_id')

    return render(request, "master/messages.html", {
        "messages": messages
    })





def search_appointments(request):

    print("🔎 search_appointments called")

    if 'dname' not in request.session:
        print("❌ Unauthorized access attempt")
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    doctor = get_object_or_404(
        Doctor,
        login__login_id=request.session['slogid']
    )

    today = timezone.now().date()
    search_query = request.GET.get('search', '')

    print("📅 Today:", today)
    print("🔍 Search Query:", search_query)

    appointments = Appointment.objects.filter(
        doctor=doctor,
        appointment_date__gt=today
    ).filter(
        Q(patient__patient_id__icontains=search_query) |
        Q(appointment_id__icontains=search_query)
    ).select_related('patient', 'health_details')

    print("📊 Total Results Found:", appointments.count())
    print("=====================================")

    data = []

    for index, appt in enumerate(appointments, start=1):

        lifestyle = appt.health_details.lifestyle_habits if appt.health_details else "-"
        symptoms = appt.health_details.symptoms if appt.health_details else "-"

        print(f"Result {index}")
        print("Appointment ID :", appt.appointment_id)
        print("Patient Name   :", appt.patient.name)
        print("Patient ID     :", appt.patient.patient_id)
        print("Status         :", appt.status)
        print("Lifestyle      :", lifestyle)
        print("Symptoms       :", symptoms)
        print("-------------------------------------")

        data.append({
            'appointment_id': appt.appointment_id,
            'patient_name': appt.patient.name,
            'patient_id': appt.patient.patient_id,
            'status': appt.status,
            'lifestyle': lifestyle,
            'symptoms': symptoms,
        })

    print("=====================================")
    print("✅ JSON Response Sent\n")

    return JsonResponse({'appointments': data})


def search_appointments_today(request):

    print("🔎 search_appointments_today called")

    if 'dname' not in request.session:
        print("❌ Unauthorized access attempt")
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    doctor = get_object_or_404(
        Doctor,
        login__login_id=request.session['slogid']
    )

    today = timezone.now().date()
    search_query = request.GET.get('search', '')

    print("📅 Today:", today)
    print("🔍 Search Query:", search_query)

    appointments = Appointment.objects.filter(
        doctor=doctor,
        appointment_date=today
    ).filter(
        Q(patient__patient_id__icontains=search_query) |
        Q(appointment_id__icontains=search_query)
    ).select_related('patient', 'health_details')

    print("📊 Total Results Found:", appointments.count())
    print("=====================================")

    data = []

    for index, appt in enumerate(appointments, start=1):

        lifestyle = appt.health_details.lifestyle_habits if appt.health_details else "-"
        symptoms = appt.health_details.symptoms if appt.health_details else "-"

        print(f"Result {index}")
        print("Appointment ID :", appt.appointment_id)
        print("Patient Name   :", appt.patient.name)
        print("Patient ID     :", appt.patient.patient_id)
        print("Status         :", appt.status)
        print("Lifestyle      :", lifestyle)
        print("Symptoms       :", symptoms)
        print("-------------------------------------")

        data.append({
            'appointment_id': appt.appointment_id,
            'patient_name': appt.patient.name,
            'patient_id': appt.patient.patient_id,
            'status': appt.status,
            'lifestyle': lifestyle,
            'symptoms': symptoms,
        })

    print("=====================================")
    print("✅ JSON Response Sent\n")

    return JsonResponse({'appointments': data})

def search_appointments_history(request):
    if 'dname' not in request.session:
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    doctor = get_object_or_404(Doctor, login__login_id=request.session['slogid'])
    search_query = request.GET.get('search', '')
    today = timezone.now().date()

    appointments = Appointment.objects.filter(
        doctor=doctor,
        appointment_date__lte=today,
        status="Approved"
    ).filter(
        Q(patient__patient_id__icontains=search_query) |
        Q(appointment_id__icontains=search_query)
    ).select_related('patient', 'department', 'clinical', 'prescription')

    data = []
    for appt in appointments:
        data.append({
            'appointment_id': appt.appointment_id,
            'appointment_date': appt.appointment_date,
            'appointment_time': appt.appointment_time,
            'patient_name': appt.patient.name,
            'patient_id': appt.patient.patient_id,
            'patient_phone': appt.patient.phone,
            'department': appt.department.name,
            'status': appt.status,
             # Safely check if related objects exist
    'clinical': hasattr(appt, 'clinical') and appt.clinical is not None,
    'prescription': hasattr(appt, 'prescription') and appt.prescription is not None,
        })

    return JsonResponse({'appointments': data})


from django.http import JsonResponse
from django.db.models import Q
from django.utils import timezone

def search_oncology_cases(request):
    if 'dname' not in request.session:
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    doctor = Doctor.objects.get(login_id=request.session['slogid'])
    query = request.GET.get('search', '').strip()

    cases = OncologyCase.objects.select_related('patient', 'appointment').filter(
        doctor=doctor
    )

    if query:
        cases = cases.filter(
              Q(patient__patient_id__icontains=query) |
            Q(appointment__appointment_id__icontains=query)
        )

    data = []
    for case in cases:
        data.append({
            'oncology_case_id': case.oncology_case_id,
            'patient_name': case.patient.name,
            'age': case.patient.age,
            'gender': case.patient.gender,
            'phone': case.patient.phone,
            'appointment_date': case.appointment.appointment_date.strftime("%Y-%m-%d"),
            'detection_status': case.detection_status,
        })

    return JsonResponse({'cases': data})




def search_lab_tests(request):
    if 'lname' not in request.session:
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    lab = get_object_or_404(Lab, login__login_id=request.session['slogid'])
    query = request.GET.get('search', '').strip()

    tests = PatientLabTest.objects.filter(
        lab_test__lab=lab,
        status='Pending'
    ).select_related('patient', 'lab_test', 'appointment')

    if query:
        tests = tests.filter(
            Q(patient__patient_id__icontains=query) |
            Q(appointment__appointment_id__icontains=query)
        )

    data = []
    for test in tests:
        data.append({
            'id': test.id,
            'patient_id': test.patient.patient_id,
            'name': test.patient.name,
            'age': test.patient.age,
            'gender': test.patient.gender,
            'phone': test.patient.phone,
            'email': test.patient.email,
            'test_name': test.lab_test.test_name,
            'appointment_date': test.appointment.appointment_date.strftime("%Y-%m-%d"),
            'status': test.status,
        })

    return JsonResponse({'tests': data})

def search_lab_tests_processing(request):
    if 'lname' not in request.session:
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    lab = get_object_or_404(Lab, login__login_id=request.session['slogid'])
    query = request.GET.get('search', '').strip()

    tests = PatientLabTest.objects.filter(
        lab_test__lab=lab,
        status='Processing'
    ).select_related('patient', 'lab_test', 'appointment')

    if query:
        tests = tests.filter(
            Q(patient__patient_id__icontains=query) |
            Q(appointment__appointment_id__icontains=query)
        )

    data = []
    for test in tests:
        data.append({
            'id': test.id,
            'patient_id': test.patient.patient_id,
            'name': test.patient.name,
            'age': test.patient.age,
            'gender': test.patient.gender,
            'phone': test.patient.phone,
            'email': test.patient.email,
            'test_name': test.lab_test.test_name,
            'appointment_date': test.appointment.appointment_date.strftime("%Y-%m-%d"),
            'status': test.status,
        })

    return JsonResponse({'tests': data})


def search_completed_tests(request):
    if 'lname' not in request.session:
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    lab = get_object_or_404(Lab, login__login_id=request.session['slogid'])
    query = request.GET.get('search', '').strip()

    tests = PatientLabTest.objects.filter(
        lab_test__lab=lab,
        status='Completed'
    ).select_related('patient', 'lab_test', 'appointment')

    if query:
        tests = tests.filter(
            Q(patient__patient_id__icontains=query) |
            Q(appointment__appointment_id__icontains=query)
        )

    data = []
    for test in tests:
        data.append({
            'id': test.id,
            'patient_id': test.patient.patient_id,
            'name': test.patient.name,
            'age': test.patient.age,
            'gender': test.patient.gender,
            'phone': test.patient.phone,
            'email': test.patient.email,
            'test_name': test.lab_test.test_name,
            'appointment_date': test.appointment.appointment_date.strftime("%Y-%m-%d"),
            'status': test.status,
            'report_url': test.report_file.url if test.report_file else None
        })

    return JsonResponse({'tests': data})

def all_patient_details(request):

    patient = Patient.objects.get(login__login_id=request.session['slogid'])


    oncology_case = OncologyCase.objects.filter(patient=patient).first()
    appointments = Appointment.objects.filter(patient=patient).order_by('-appointment_date')
    lab_tests = PatientLabTest.objects.filter(patient=patient)

    context = {
        'patient': patient,
        'oncology_case': oncology_case,
        'appointments': appointments,
        'lab_tests': lab_tests,
    }

    return render(request, 'Patient/all_patient_details.html', context)

# =============================================================================

def emergency_to_doctor(request):
    if 'pname' not in request.session:
        return redirect('log')

    # Get patient
    patient = get_object_or_404(Patient, login_id=request.session['slogid'])

    # Get all doctors who have confirmed oncology cases for this patient
    consulted_doctors = Doctor.objects.filter(
        oncologycase__patient=patient,
        oncologycase__detection_status='Confirmed'
    ).distinct()

    if request.method == "POST":
        doctor_id = request.POST.get('doctor_id')
        message_text = request.POST.get('message')

        doctor = get_object_or_404(Doctor, pk=doctor_id)

        # Save message
        EmergencyMessage.objects.create(
            patient=patient,
            doctor=doctor,
            message=message_text
        )

        return redirect('emergency_to_doctor')  # refresh page
    messages_list = EmergencyMessage.objects.filter(patient=patient)
    return render(request, 'patient/emergency_to_doctor.html', {
        'consulted_doctors': consulted_doctors,
        'patient': patient,
        'messages_list':messages_list
    })
def emergency_message_patient(request):
    if 'dname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(Doctor, login_id=request.session['slogid'])

    # Get all messages sent to this doctor
    messages_list = EmergencyMessage.objects.filter(doctor=doctor)

    return render(request, 'doctor/emergency_message_patient.html', {
        'messages_list': messages_list
    })
def reply_emergency_patient(request, message_id):
    if 'dname' not in request.session:
        return redirect('log')

    doctor = get_object_or_404(Doctor, login_id=request.session['slogid'])
    message = get_object_or_404(EmergencyMessage, pk=message_id, doctor=doctor)

    if request.method == "POST":
        reply_text = request.POST.get('reply')

        message.reply = reply_text
        message.status = "Replied"
        message.save()

        return redirect('emergency_message_patient')

    return render(request, 'doctor/reply_emergency_patient.html', {
        'message': message
    })

def adm_patient_details(request,id):

    patient = Patient.objects.get(patient_id=id)


    oncology_case = OncologyCase.objects.filter(patient=patient).first()
    appointments = Appointment.objects.filter(patient=patient).order_by('-appointment_date')
    lab_tests = PatientLabTest.objects.filter(patient=patient)

    context = {
        'patient': patient,
        'oncology_case': oncology_case,
        'appointments': appointments,
        'lab_tests': lab_tests,
    }

    return render(request, 'master/all_patient_details.html', context)

def get_doctors(request, department_id):
    doctors = Doctor.objects.filter(department_id=department_id, status='Available')
    doctor_list = [
        {'doctor_id': doc.doctor_id, 'name': doc.name}
        for doc in doctors
    ]
    return JsonResponse({'doctors': doctor_list})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def profile_edit(request):
    if 'pname' not in request.session:
        return redirect('log')

    patient = get_object_or_404(
        Patient,
        login_id=request.session['slogid']
    )

    if request.method == "POST":
        patient.name = request.POST.get('name')
        patient.age = request.POST.get('age')
        patient.gender = request.POST.get('gender')
        patient.phone = request.POST.get('phone')
        patient.email = request.POST.get('email')
        patient.address = request.POST.get('address')

        if request.FILES.get('image'):
            patient.image = request.FILES.get('image')

        patient.save()
        messages.success(request, "Profile updated successfully")
        return redirect('profile_edit')

    return render(request, 'patient/profile_edit.html', {
        'patient': patient
    })