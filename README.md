# 🚀 ORATRACK – ML Powered Oral Cancer Detection & Oncology Management System

ORATRACK is an intelligent, full-stack healthcare application designed to improve early detection and management of oral cancer. The system integrates Machine Learning with a structured clinical workflow to support screening, biopsy tracking, treatment planning, and continuous patient monitoring.

---

## 💡 Key Features

- 🔐 **Role-Based Access Control**
  - Admin, Doctor, Oncologist, Lab Technician, Patient

- 🧠 **ML-Based Cancer Risk Prediction**
  - Uses Random Forest Classifier
  - Predicts: Normal, Low, Moderate, High risk

- 📍 **Clinical Data-Based Screening**
  - No expensive imaging required
  - Uses real clinical parameters

- 🧪 **Automated Biopsy Workflow**
  - Generates biopsy requests for high-risk cases
  - Tracks lab progress in real-time

- 🏥 **Oncology Management System**
  - Treatment planning
  - Therapy scheduling (Chemo/Radiotherapy)
  - Progress tracking

- 👨‍⚕️ **Doctor–Patient Communication**
  - Messaging system
  - Emergency alerts

- 📊 **Centralized Patient Records**
  - Complete medical history
  - Reports, prescriptions, and analytics

---

## 🛠️ Tech Stack

- **Backend:** Python (Django Framework)  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** MySQL  
- **Machine Learning:** Scikit-learn (Random Forest)  
- **Server:** Localhost (XAMPP / Django Server)

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Classifier  
- **Input Parameters:**
  - Lesion size  
  - Ulcer duration  
  - Pain intensity  
  - Bleeding  
  - Smoking habits  
  - Alcohol consumption  
  - Medical history  

- **Output:**
  - Normal  
  - Low Risk  
  - Moderate Risk  
  - High Risk  

---

## 🔄 System Workflow

1. Patient registers and enters health details  
2. Doctor inputs clinical parameters  
3. ML model predicts cancer risk  
4. If risk is moderate/high → biopsy request generated  
5. Lab updates biopsy status and uploads report  
6. Confirmed cases are assigned to oncologist  
7. Treatment planning and monitoring begins  

##  Demo Link
https://oratrack.onrender.com
## 📸 Screenshots

### 🔐 Login Page
<img width="603" height="236" alt="image" src="https://github.com/user-attachments/assets/3e5c8c6d-bd71-4baf-896e-7cc7b27dad4e" />


### 🧠 ML Prediction
<img width="620" height="206" alt="image" src="https://github.com/user-attachments/assets/e97129fd-8963-47d8-bb13-71243a04ad09" />


### 🏥Admin Dashboard
<img width="676" height="223" alt="image" src="https://github.com/user-attachments/assets/0ce8633f-58f6-4704-ad0a-a5eea73dbec4" />
