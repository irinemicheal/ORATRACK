from django.db import models

# Create your models here.
class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.TextField()
    Usertype = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'tbl_login'



class Patient(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    patient_id = models.AutoField(primary_key=True)
    login= models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    image = models.ImageField(upload_to='patients/', null=True, blank=True)

    registered_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'tbl_patient'


    def __str__(self):
        return self.name
   
   
class DoctorDepartment(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        db_table = 'tbl_department'

    def __str__(self):
        return self.name


from django.db import models

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    login= models.ForeignKey(Login, on_delete=models.CASCADE)
    department = models.ForeignKey(
        DoctorDepartment,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=150)
    experience = models.IntegerField(help_text="Years of experience")
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField(
        upload_to='doctor_images/',
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('Available', 'Available'),
            ('Unavailable', 'Unavailable')
        ],
        default='Available'
    )

    class Meta:
        db_table = 'tbl_doctor'
   
    def __str__(self):
        return self.name


class PatientHealthDetails(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)

    # 🔹 Lifestyle & Risk Factors
    tobacco_use = models.CharField(
        max_length=3,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        null=True, blank=True
    )

    alcohol_consumption = models.CharField(
        max_length=3,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        null=True, blank=True
    )

    betel_quid_use = models.CharField(
        max_length=3,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        null=True, blank=True
    )

    sun_exposure = models.CharField(
        max_length=3,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        null=True, blank=True
    )

    diet_intake = models.CharField(
        max_length=10,
        choices=[
            ('Low', 'Low'),
            ('Moderate', 'Moderate'),
            ('High', 'High')
        ],
        null=True, blank=True
    )

    poor_oral_hygiene = models.CharField(
        max_length=3,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        null=True, blank=True
    )

    family_history = models.CharField(
        max_length=3,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        null=True, blank=True
    )

    immune_compromised = models.CharField(
        max_length=3,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        null=True, blank=True
    )

    hpv_infection = models.CharField(
        max_length=3,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        null=True, blank=True
    )

    # 🔹 General Health Info


    lifestyle_habits = models.TextField(
        blank=True,
        help_text="Optional free text (exercise, habits, diet notes)"
    )

    symptoms = models.TextField(
        blank=True,
        help_text="Patient-described symptoms"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_patient_health_details'

    
    

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.ForeignKey(DoctorDepartment, on_delete=models.CASCADE)
    health_details = models.ForeignKey(
        PatientHealthDetails,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Rejected', 'Rejected'),
        ],
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_appointment'

    def __str__(self):
        return f"{self.patient} - {self.doctor}"




class Lab(models.Model):
    lab_id = models.AutoField(primary_key=True)
    login= models.ForeignKey(Login, on_delete=models.CASCADE)
    lab_name = models.CharField(max_length=150)
    license_number = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    lab_type = models.CharField(
        max_length=100,
        choices=(
            ('Pathology', 'Pathology'),
            ('Biopsy', 'Biopsy'),
            ('Oncology', 'Oncology'),
            ('Dental', 'Dental'),
        )
    )
    registered_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_lab'

    def __str__(self):
        return self.lab_name



class LabTest(models.Model):
    test_id = models.AutoField(primary_key=True)

    lab = models.ForeignKey(
        Lab,
        on_delete=models.CASCADE,
        related_name='tests'
    )
    test_name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_lab_test'

    def __str__(self):
        return self.test_name


class Feedback(models.Model):
    fd_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField()
    reply = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'tbl_feedback'
    def __str__(self):
        return self.test_name
        

class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    complaint = models.TextField()
    reply = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'tbl_complaint'        
    
    def __str__(self):
        return self.test_name
    
    
class ClinicalExamination(models.Model):
    clinical_examination_id = models.AutoField(primary_key=True)

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name='clinical'
    )

    # Doctor-entered examination fields
    symptoms = models.TextField(blank=True, null=True)

    oral_lesions = models.BooleanField(default=False)
    unexplained_bleeding = models.BooleanField(default=False)
    difficulty_swallowing = models.BooleanField(default=False)
    white_red_patches = models.BooleanField(default=False)

    pain_intensity = models.IntegerField(
        blank=True,
        null=True,
        help_text="Pain scale from 0 to 10"
    )

    ulcer_duration = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Eg: 3 days, 2 weeks"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_clinical_examination'

    def __str__(self):
        return f"Clinical Examination - Appointment {self.appointment_id}"

    
    
    
class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name='prescription'
    )

    diagnosis = models.TextField(blank=True, null=True)

    medicine_details = models.TextField(
        blank=True, null=True,
        help_text="Medicine name, dosage, duration"
    )

    medicine_usage = models.TextField(
        blank=True, null=True,
        help_text="How to use medicine (morning/night, before food etc)"
    )

    more_details = models.TextField(
        blank=True, null=True,
        help_text="Extra notes / precautions"
    )

    next_visit_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_prescription'

    def __str__(self):
        return f"Prescription - {self.appointment}"
class PatientLabTest(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    lab_test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=(('Pending', 'Pending'), ('Completed', 'Completed')),
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    report_file = models.FileField(null=True, blank=True)
    class Meta:
        db_table = 'tbl_patient_lab_test'

    def __str__(self):
        return f"{self.patient} - {self.lab_test}"
class OncologyCase(models.Model):
    oncology_case_id = models.AutoField(primary_key=True)

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name='oncology_case'
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    detection_status = models.CharField(
        max_length=50,
        choices=(
            ('Suspected', 'Suspected'),
            ('Confirmed', 'Confirmed'),
            ('Negative', 'Negative'),
        ),
        default='Suspected'
    )



    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_oncology_case'

    def __str__(self):
        return f"Oncology Case - {self.patient.name}"


class Chemotherapy(models.Model):
    chemo_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    session_no = models.IntegerField()
    drug_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    chemo_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_chemotherapy'


class Radiotherapy(models.Model):
    radio_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    session_no = models.IntegerField()
    radiation_type = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    radio_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_radiotherapy'

class PatientDoctorMessage(models.Model):
    message_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    message = models.TextField()  # Message sent by the patient
    reply = models.TextField(null=True, blank=True)  # Reply from doctor

    status = models.CharField(
        max_length=20,
        choices=(('Pending', 'Pending'), ('Replied', 'Replied')),
        default='Pending'
    ),
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    class Meta:
        db_table = 'tbl_patient_doctor_message'
        ordering = ['-date']

    def __str__(self):
        return f"{self.patient.name} → {self.doctor.name}"
class EmergencyMessage(models.Model):
    message_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    message = models.TextField()  # Message sent by the patient
    reply = models.TextField(null=True, blank=True)  # Reply from doctor

    status = models.CharField(
        max_length=20,
        choices=(('Pending', 'Pending'), ('Replied', 'Replied')),
        default='Pending'
    ),
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    class Meta:
        db_table = 'tbl_emergency_message'
        ordering = ['-date']

    def __str__(self):
        return f"{self.patient.name} → {self.doctor.name}"