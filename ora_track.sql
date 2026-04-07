-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 24, 2026 at 12:51 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ora_track`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add appointment', 7, 'add_appointment'),
(26, 'Can change appointment', 7, 'change_appointment'),
(27, 'Can delete appointment', 7, 'delete_appointment'),
(28, 'Can view appointment', 7, 'view_appointment'),
(29, 'Can add doctor', 8, 'add_doctor'),
(30, 'Can change doctor', 8, 'change_doctor'),
(31, 'Can delete doctor', 8, 'delete_doctor'),
(32, 'Can view doctor', 8, 'view_doctor'),
(33, 'Can add doctor department', 9, 'add_doctordepartment'),
(34, 'Can change doctor department', 9, 'change_doctordepartment'),
(35, 'Can delete doctor department', 9, 'delete_doctordepartment'),
(36, 'Can view doctor department', 9, 'view_doctordepartment'),
(37, 'Can add lab', 10, 'add_lab'),
(38, 'Can change lab', 10, 'change_lab'),
(39, 'Can delete lab', 10, 'delete_lab'),
(40, 'Can view lab', 10, 'view_lab'),
(41, 'Can add login', 11, 'add_login'),
(42, 'Can change login', 11, 'change_login'),
(43, 'Can delete login', 11, 'delete_login'),
(44, 'Can view login', 11, 'view_login'),
(45, 'Can add clinical examination', 12, 'add_clinicalexamination'),
(46, 'Can change clinical examination', 12, 'change_clinicalexamination'),
(47, 'Can delete clinical examination', 12, 'delete_clinicalexamination'),
(48, 'Can view clinical examination', 12, 'view_clinicalexamination'),
(49, 'Can add lab test', 13, 'add_labtest'),
(50, 'Can change lab test', 13, 'change_labtest'),
(51, 'Can delete lab test', 13, 'delete_labtest'),
(52, 'Can view lab test', 13, 'view_labtest'),
(53, 'Can add patient', 14, 'add_patient'),
(54, 'Can change patient', 14, 'change_patient'),
(55, 'Can delete patient', 14, 'delete_patient'),
(56, 'Can view patient', 14, 'view_patient'),
(57, 'Can add feedback', 15, 'add_feedback'),
(58, 'Can change feedback', 15, 'change_feedback'),
(59, 'Can delete feedback', 15, 'delete_feedback'),
(60, 'Can view feedback', 15, 'view_feedback'),
(61, 'Can add complaint', 16, 'add_complaint'),
(62, 'Can change complaint', 16, 'change_complaint'),
(63, 'Can delete complaint', 16, 'delete_complaint'),
(64, 'Can view complaint', 16, 'view_complaint'),
(65, 'Can add patient health details', 17, 'add_patienthealthdetails'),
(66, 'Can change patient health details', 17, 'change_patienthealthdetails'),
(67, 'Can delete patient health details', 17, 'delete_patienthealthdetails'),
(68, 'Can view patient health details', 17, 'view_patienthealthdetails'),
(69, 'Can add prescription', 18, 'add_prescription'),
(70, 'Can change prescription', 18, 'change_prescription'),
(71, 'Can delete prescription', 18, 'delete_prescription'),
(72, 'Can view prescription', 18, 'view_prescription'),
(73, 'Can add patient lab test', 19, 'add_patientlabtest'),
(74, 'Can change patient lab test', 19, 'change_patientlabtest'),
(75, 'Can delete patient lab test', 19, 'delete_patientlabtest'),
(76, 'Can view patient lab test', 19, 'view_patientlabtest'),
(77, 'Can add oncology case', 20, 'add_oncologycase'),
(78, 'Can change oncology case', 20, 'change_oncologycase'),
(79, 'Can delete oncology case', 20, 'delete_oncologycase'),
(80, 'Can view oncology case', 20, 'view_oncologycase'),
(81, 'Can add radiotherapy', 21, 'add_radiotherapy'),
(82, 'Can change radiotherapy', 21, 'change_radiotherapy'),
(83, 'Can delete radiotherapy', 21, 'delete_radiotherapy'),
(84, 'Can view radiotherapy', 21, 'view_radiotherapy'),
(85, 'Can add chemotherapy', 22, 'add_chemotherapy'),
(86, 'Can change chemotherapy', 22, 'change_chemotherapy'),
(87, 'Can delete chemotherapy', 22, 'delete_chemotherapy'),
(88, 'Can view chemotherapy', 22, 'view_chemotherapy'),
(89, 'Can add patient doctor message', 23, 'add_patientdoctormessage'),
(90, 'Can change patient doctor message', 23, 'change_patientdoctormessage'),
(91, 'Can delete patient doctor message', 23, 'delete_patientdoctormessage'),
(92, 'Can view patient doctor message', 23, 'view_patientdoctormessage'),
(93, 'Can add emergency message', 24, 'add_emergencymessage'),
(94, 'Can change emergency message', 24, 'change_emergencymessage'),
(95, 'Can delete emergency message', 24, 'delete_emergencymessage'),
(96, 'Can view emergency message', 24, 'view_emergencymessage');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$8L9J2j3RGc6eSuiycOcG6e$oCpBKfmG0tC+HQ/QwHeJwSNJ3644UfHxcKU3OUEj5eg=', NULL, 1, 'admin', '', '', '', 1, 1, '2026-01-31 06:24:38.946802');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'myapp', 'appointment'),
(22, 'myapp', 'chemotherapy'),
(12, 'myapp', 'clinicalexamination'),
(16, 'myapp', 'complaint'),
(8, 'myapp', 'doctor'),
(9, 'myapp', 'doctordepartment'),
(24, 'myapp', 'emergencymessage'),
(15, 'myapp', 'feedback'),
(10, 'myapp', 'lab'),
(13, 'myapp', 'labtest'),
(11, 'myapp', 'login'),
(20, 'myapp', 'oncologycase'),
(14, 'myapp', 'patient'),
(23, 'myapp', 'patientdoctormessage'),
(17, 'myapp', 'patienthealthdetails'),
(19, 'myapp', 'patientlabtest'),
(18, 'myapp', 'prescription'),
(21, 'myapp', 'radiotherapy'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-01-31 06:23:33.163113'),
(2, 'auth', '0001_initial', '2026-01-31 06:23:34.050915'),
(3, 'admin', '0001_initial', '2026-01-31 06:23:34.260772'),
(4, 'admin', '0002_logentry_remove_auto_add', '2026-01-31 06:23:34.302087'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2026-01-31 06:23:34.333343'),
(6, 'contenttypes', '0002_remove_content_type_name', '2026-01-31 06:23:34.521258'),
(7, 'auth', '0002_alter_permission_name_max_length', '2026-01-31 06:23:34.613960'),
(8, 'auth', '0003_alter_user_email_max_length', '2026-01-31 06:23:34.645216'),
(9, 'auth', '0004_alter_user_username_opts', '2026-01-31 06:23:34.645216'),
(10, 'auth', '0005_alter_user_last_login_null', '2026-01-31 06:23:34.724961'),
(11, 'auth', '0006_require_contenttypes_0002', '2026-01-31 06:23:34.729962'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2026-01-31 06:23:34.739987'),
(13, 'auth', '0008_alter_user_username_max_length', '2026-01-31 06:23:34.755623'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2026-01-31 06:23:34.771236'),
(15, 'auth', '0010_alter_group_name_max_length', '2026-01-31 06:23:34.804650'),
(16, 'auth', '0011_update_proxy_permissions', '2026-01-31 06:23:34.817035'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2026-01-31 06:23:34.848291'),
(18, 'myapp', '0001_initial', '2026-01-31 06:23:36.848914'),
(19, 'sessions', '0001_initial', '2026-01-31 06:23:36.894482'),
(20, 'myapp', '0002_patienthealthdetails_alcohol_consumption_and_more', '2026-02-10 05:46:55.117940'),
(21, 'myapp', '0003_remove_patienthealthdetails_height_cm_and_more', '2026-02-10 05:48:58.767188'),
(22, 'myapp', '0004_remove_clinicalexamination_lesion_appearance_and_more', '2026-02-10 09:12:34.223168'),
(23, 'myapp', '0005_patientlabtest', '2026-02-11 07:51:59.510160'),
(24, 'myapp', '0006_patientlabtest_report_file', '2026-02-11 10:36:58.441112'),
(25, 'myapp', '0007_oncologycase', '2026-02-12 08:55:02.132722'),
(26, 'myapp', '0008_alter_appointment_status', '2026-02-12 09:19:57.487501'),
(27, 'myapp', '0009_chemotherapy_radiotherapy', '2026-02-13 04:21:01.136767'),
(28, 'myapp', '0010_rename_chemo_date_radiotherapy_radio_date', '2026-02-13 05:01:42.152460'),
(29, 'myapp', '0011_remove_oncologycase_remarks_and_more', '2026-02-13 08:39:50.548628'),
(30, 'myapp', '0012_remove_patientdoctormessage_status_and_more', '2026-02-13 09:06:35.046762'),
(31, 'myapp', '0013_emergencymessage', '2026-02-24 10:08:46.431163');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('gn4r474a7g478q1x2eg1pua82ph08bgi', 'eyJwbmFtZSI6ImdheWF0aHJpIiwic2xvZ2lkIjozLCJoYXNfY2FuY2VyIjp0cnVlfQ:1vuqen:b7dNPLCblnbpl5ydLVWCVEBEHNgzzcQSiRjG36VVt2A', '2026-03-10 11:32:50.000150'),
('j6j6m8y2pla9pez9h79kizarpozk8gty', 'eyJkbmFtZSI6ImpvaG5zbWl0aDEyIiwic2xvZ2lkIjoxLCJkb2N0b3JfaWQiOjF9:1vq38e:GrnCccyG4XudF-FGvA93tatrqr1UxMXZEktW47Q5Pfo', '2026-02-25 05:51:48.722602'),
('wgyujdkzew586qb911vhudbq5frwes48', 'eyJhbmFtZSI6ImFkbWluIiwic2xvZ2lkIjoxfQ:1vqpgK:T6EE85VVlv5dULQhSuMMcg3APismYtNoOhKPIMRyLDM', '2026-02-27 09:41:48.240170');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_appointment`
--

CREATE TABLE `tbl_appointment` (
  `appointment_id` int(11) NOT NULL,
  `appointment_date` date NOT NULL,
  `appointment_time` time(6) NOT NULL,
  `status` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `doctor_id` int(11) NOT NULL,
  `department_id` int(11) NOT NULL,
  `patient_id` int(11) NOT NULL,
  `health_details_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_appointment`
--

INSERT INTO `tbl_appointment` (`appointment_id`, `appointment_date`, `appointment_time`, `status`, `created_at`, `doctor_id`, `department_id`, `patient_id`, `health_details_id`) VALUES
(1, '2026-01-31', '13:00:00.000000', 'Pending', '2026-01-31 06:34:44.467439', 1, 1, 1, 1),
(2, '2026-02-11', '13:00:00.000000', 'Forwarded to Oncology', '2026-02-10 07:06:57.840622', 3, 4, 1, 1),
(3, '2026-02-11', '09:10:00.000000', 'Pending', '2026-02-10 07:07:31.400135', 2, 2, 1, 1),
(4, '2026-02-11', '13:00:00.000000', 'Approved', '2026-02-10 07:06:57.840622', 1, 2, 1, 1),
(5, '2026-02-11', '13:00:00.000000', 'Rejected', '2026-02-10 07:06:57.840622', 1, 2, 1, 1),
(6, '2026-02-11', '09:10:00.000000', 'Pending', '2026-02-10 07:07:31.400135', 2, 2, 1, 1),
(7, '2026-02-11', '13:00:00.000000', 'Pending', '2026-02-10 07:06:57.840622', 1, 2, 1, 1),
(8, '2026-02-13', '18:07:00.000000', 'Approved', '2026-02-12 09:15:46.831491', 3, 4, 1, 1),
(9, '2026-02-12', '15:05:00.000000', 'Approved', '2026-02-12 09:23:17.343952', 3, 4, 1, 1),
(10, '2026-02-24', '09:05:00.000000', 'Approved', '2026-02-24 04:33:14.274265', 3, 4, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_chemotherapy`
--

CREATE TABLE `tbl_chemotherapy` (
  `chemo_id` int(11) NOT NULL,
  `session_no` int(11) NOT NULL,
  `drug_name` varchar(100) NOT NULL,
  `dosage` varchar(100) NOT NULL,
  `chemo_date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `appointment_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_chemotherapy`
--

INSERT INTO `tbl_chemotherapy` (`chemo_id`, `session_no`, `drug_name`, `dosage`, `chemo_date`, `created_at`, `appointment_id`) VALUES
(1, 4, 'XYZ Drug', '12mm', '2026-02-13', '2026-02-13 04:39:18.467132', 8),
(2, 4, 'XYZ Drug', '12mm', '2026-02-24', '2026-02-13 04:39:18.467132', 8),
(3, 4, 'XYZ Drug', '12mm', '2026-02-28', '2026-02-13 04:39:18.475418', 8),
(4, 4, 'XYZ Drug', '12mm', '2026-03-21', '2026-02-13 04:39:18.475418', 8),
(5, 4, 'XYZ Drug', '12mm', '2026-02-19', '2026-02-13 04:40:36.115893', 8),
(6, 4, 'XYZ Drug', '12mm', '2026-02-25', '2026-02-13 04:40:36.130755', 8),
(7, 4, 'XYZ Drug', '12mm', '2026-02-28', '2026-02-13 04:40:36.130755', 8),
(8, 4, 'XYZ Drug', '12mm', '2026-03-21', '2026-02-13 04:40:36.130755', 8);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_clinical_examination`
--

CREATE TABLE `tbl_clinical_examination` (
  `clinical_examination_id` int(11) NOT NULL,
  `ulcer_duration` varchar(100) DEFAULT NULL,
  `symptoms` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `appointment_id` int(11) NOT NULL,
  `difficulty_swallowing` tinyint(1) NOT NULL,
  `oral_lesions` tinyint(1) NOT NULL,
  `pain_intensity` int(11) DEFAULT NULL,
  `unexplained_bleeding` tinyint(1) NOT NULL,
  `white_red_patches` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_clinical_examination`
--

INSERT INTO `tbl_clinical_examination` (`clinical_examination_id`, `ulcer_duration`, `symptoms`, `created_at`, `appointment_id`, `difficulty_swallowing`, `oral_lesions`, `pain_intensity`, `unexplained_bleeding`, `white_red_patches`) VALUES
(1, '5 Days', 'Painful', '2026-02-10 09:57:10.053580', 2, 1, 1, 1, 1, 1),
(2, '1 Week', 'Pain full', '2026-02-24 09:10:42.356567', 10, 0, 0, 4, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_complaint`
--

CREATE TABLE `tbl_complaint` (
  `complaint_id` int(11) NOT NULL,
  `date` datetime(6) NOT NULL,
  `complaint` longtext NOT NULL,
  `reply` longtext DEFAULT NULL,
  `patient_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_complaint`
--

INSERT INTO `tbl_complaint` (`complaint_id`, `date`, `complaint`, `reply`, `patient_id`) VALUES
(1, '2026-01-31 06:35:14.616730', 'guytyuf', NULL, 1),
(2, '2026-02-10 07:32:46.754698', 'Very bad Atmosphere', 'None', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_department`
--

CREATE TABLE `tbl_department` (
  `department_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_department`
--

INSERT INTO `tbl_department` (`department_id`, `name`, `description`) VALUES
(1, 'General Dentist', 'Provides primary oral healthcare, performs routine dental examinations, identifies early signs of oral diseases and suspicious lesions, and refers patients to specialists for advanced evaluation or cancer screening.'),
(2, 'Oral Health Specialist', 'Specializes in the diagnosis and management of oral diseases, including precancerous lesions and early-stage oral cancer. Conducts detailed oral examinations, biopsy recommendations, and coordinates care with oncology and pathology departments.'),
(3, 'ENT (Ear, Nose & Throat) Specialist', 'Focuses on disorders of the ear, nose, throat, head, and neck region. Evaluates suspected head and neck cancers, manages airway involvement, and collaborates with oral oncology teams for comprehensive cancer diagnosis and treatment.'),
(4, 'Oncology', 'An Oncology Department\nspecializes in the diagnosis, treatment, and prevention of cancer, utilizing multidisciplinary teams to provide comprehensive care. Services include medical, surgical, and radiation oncology, offering treatments ');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_doctor`
--

CREATE TABLE `tbl_doctor` (
  `doctor_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `qualification` varchar(150) NOT NULL,
  `experience` int(11) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `department_id` int(11) NOT NULL,
  `login_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_doctor`
--

INSERT INTO `tbl_doctor` (`doctor_id`, `name`, `qualification`, `experience`, `phone`, `email`, `image`, `status`, `department_id`, `login_id`) VALUES
(1, 'Dr. John Smith', 'BDS, MDS', 5, '8974548596', 'johnsmith43@gmail.com', 'doctor_images/download_3_1BbKETF.jpg', 'Available', 1, 1),
(2, 'Dr.John Doe', 'MBBS', 4, '8545123649', 'johndoe34@gmail.com', 'doctor_images/download_4.jpg', 'Available', 2, 4),
(3, 'Dr. Stephan Abraham', 'MBBS', 3, '9874589636', 'stephan@gmail.com', 'doctor_images/1.jpg', 'Available', 4, 7),
(4, 'Dain Tom', 'MBBS', 3, '8965321245', 'dain@gmail.com', 'doctor_images/6..jpg', 'Available', 4, 8);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_emergency_message`
--

CREATE TABLE `tbl_emergency_message` (
  `message_id` int(11) NOT NULL,
  `date` datetime(6) NOT NULL,
  `message` longtext NOT NULL,
  `reply` longtext DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `doctor_id` int(11) NOT NULL,
  `patient_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_emergency_message`
--

INSERT INTO `tbl_emergency_message` (`message_id`, `date`, `message`, `reply`, `created_at`, `doctor_id`, `patient_id`) VALUES
(1, '2026-02-24 10:27:05.173866', 'Pain', 'Take an appointment for tommorrow', '2026-02-24 10:27:05.173866', 3, 1),
(2, '2026-02-24 10:51:30.250074', 'Please change medicine', NULL, '2026-02-24 10:51:30.250074', 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_feedback`
--

CREATE TABLE `tbl_feedback` (
  `fd_id` int(11) NOT NULL,
  `date` datetime(6) NOT NULL,
  `feedback` longtext NOT NULL,
  `reply` longtext DEFAULT NULL,
  `patient_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_feedback`
--

INSERT INTO `tbl_feedback` (`fd_id`, `date`, `feedback`, `reply`, `patient_id`) VALUES
(1, '2026-01-31 06:34:55.103058', 'nice', 'Okay', 1),
(2, '2026-02-10 07:16:49.548436', 'Good Service', 'Okay\r\n', 1),
(3, '2026-02-24 09:52:07.352529', 'Good Service', NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_lab`
--

CREATE TABLE `tbl_lab` (
  `lab_id` int(11) NOT NULL,
  `lab_name` varchar(150) NOT NULL,
  `license_number` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` longtext NOT NULL,
  `lab_type` varchar(100) NOT NULL,
  `registered_date` datetime(6) NOT NULL,
  `login_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_lab`
--

INSERT INTO `tbl_lab` (`lab_id`, `lab_name`, `license_number`, `phone`, `email`, `address`, `lab_type`, `registered_date`, `login_id`) VALUES
(1, 'OraTrack Advanced Biopsy Lab', 'KL/HL/2024/09876', '9654742136', 'ortarckbiopsy45@gmail.com', 'kochi', 'Biopsy', '2026-01-31 06:30:30.280977', 2);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_lab_test`
--

CREATE TABLE `tbl_lab_test` (
  `test_id` int(11) NOT NULL,
  `test_name` varchar(150) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `lab_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_lab_test`
--

INSERT INTO `tbl_lab_test` (`test_id`, `test_name`, `description`, `price`, `created_at`, `lab_id`) VALUES
(1, 'Complete Blood Count (CBC)', 'A blood test used to evaluate your overall health and detect a wide range of disorders, including anemia, infection, and leukemia.', 350.00, '2026-01-31 07:25:11.824405', 1),
(2, 'Fine Needle Aspiration (FNA)', 'A procedure to extract cells from a lump or mass using a thin needle for biopsy.', 1200.00, '2026-01-31 07:30:00.000000', 1),
(3, 'Punch Biopsy', 'A small circular piece of tissue is removed for microscopic examination to diagnose skin or oral lesions.', 1800.00, '2026-01-31 07:35:00.000000', 1),
(4, 'Incisional Biopsy', 'Removal of a portion of abnormal tissue to check for cancer or other disease.', 2500.00, '2026-01-31 07:40:00.000000', 1),
(5, 'Excisional Biopsy', 'Complete removal of a lump or suspicious tissue for detailed pathology examination.', 3000.00, '2026-01-31 07:45:00.000000', 1),
(6, 'Complete Blood Count (CBC)', 'A blood test used to evaluate your overall health and detect a wide range of disorders, including anemia, infection, and leukemia.', 350.00, '2026-01-31 07:25:11.000000', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_login`
--

CREATE TABLE `tbl_login` (
  `login_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` longtext NOT NULL,
  `Usertype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_login`
--

INSERT INTO `tbl_login` (`login_id`, `username`, `password`, `Usertype`, `status`) VALUES
(1, 'johnsmith12', 'johnsmith12', 'Doctor', 'Available'),
(2, 'oratrack_biopsy1', 'oratrack_biopsy1', 'Lab', 'Approved'),
(3, 'gayathri', 'gayathri', 'Patient', 'Approved'),
(4, 'john12', 'john12', 'Doctor', 'Available'),
(5, 'kavya12', 'kavya12', 'Patient', 'Approved'),
(6, 'deepak123', 'deepak123', 'Patient', 'Not Approved'),
(7, 'stephan123', 'stephan123', 'Doctor', 'Available'),
(8, 'dain123', 'dain123', 'Doctor', 'Available');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_oncology_case`
--

CREATE TABLE `tbl_oncology_case` (
  `oncology_case_id` int(11) NOT NULL,
  `detection_status` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `appointment_id` int(11) NOT NULL,
  `doctor_id` int(11) NOT NULL,
  `patient_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_oncology_case`
--

INSERT INTO `tbl_oncology_case` (`oncology_case_id`, `detection_status`, `created_at`, `appointment_id`, `doctor_id`, `patient_id`) VALUES
(1, 'Confirmed', '2026-02-12 09:23:17.350025', 9, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_patient`
--

CREATE TABLE `tbl_patient` (
  `patient_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` longtext NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `registered_date` datetime(6) NOT NULL,
  `login_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_patient`
--

INSERT INTO `tbl_patient` (`patient_id`, `name`, `age`, `gender`, `phone`, `email`, `address`, `image`, `registered_date`, `login_id`) VALUES
(1, 'Gayathri', 25, 'Female', '9687457487', 'gayathri@gmail.com', 'gayathri villa', 'patients/download_2.jpg', '2026-01-31 06:32:01.103087', 3),
(2, 'Kavya Krishnakumar', 30, 'Female', '9874547788', 'kavya43@gmail.com', 'kavya villa', 'patients/download_1_fXay6H6.jpg', '2026-01-31 07:59:19.484776', 5),
(3, 'Depak Raju', 45, 'Male', '9865321245', 'deepakraju@gmail.com', 'Deepak Villa', 'patients/1.jpg', '2026-02-10 04:24:13.697584', 6);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_patient_doctor_message`
--

CREATE TABLE `tbl_patient_doctor_message` (
  `message_id` int(11) NOT NULL,
  `date` datetime(6) NOT NULL,
  `message` longtext NOT NULL,
  `reply` longtext DEFAULT NULL,
  `doctor_id` int(11) NOT NULL,
  `patient_id` int(11) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_patient_doctor_message`
--

INSERT INTO `tbl_patient_doctor_message` (`message_id`, `date`, `message`, `reply`, `doctor_id`, `patient_id`, `created_at`) VALUES
(1, '2026-02-13 08:40:03.085502', 'I am feeling more fatigue than usual today and experiencing mild nausea after my last chemotherapy session.  \r\nThe swelling on my left arm has slightly reduced, but I still feel some discomfort while moving.  \r\nNo new symptoms noticed.  \r\n\r\nPlease advise if I should adjust my medication or schedule a check-up.  ', NULL, 3, 1, '2026-02-13 09:06:35.027764'),
(2, '2026-02-13 08:40:19.571190', 'I am feeling more fatigue than usual today and experiencing mild nausea after my last chemotherapy session.  \r\nThe swelling on my left arm has slightly reduced, but I still feel some discomfort while moving.  \r\nNo new symptoms noticed.  \r\n\r\nPlease advise if I should adjust my medication or schedule a check-up.  ', 'Thank you for your message. Based on your current symptoms, please continue the prescribed medication and monitor your temperature twice daily. If the pain or fever increases, visit the hospital immediately.', 3, 1, '2026-02-13 09:06:35.027764'),
(3, '2026-02-24 10:12:43.742668', 'Going Good', NULL, 3, 1, '2026-02-24 10:12:43.742668'),
(4, '2026-02-24 10:13:58.101409', 'Not Good health Condition', NULL, 3, 1, '2026-02-24 10:13:58.101409');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_patient_health_details`
--

CREATE TABLE `tbl_patient_health_details` (
  `id` bigint(20) NOT NULL,
  `lifestyle_habits` longtext NOT NULL,
  `symptoms` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `patient_id` int(11) NOT NULL,
  `alcohol_consumption` varchar(3) DEFAULT NULL,
  `betel_quid_use` varchar(3) DEFAULT NULL,
  `diet_intake` varchar(10) DEFAULT NULL,
  `family_history` varchar(3) DEFAULT NULL,
  `hpv_infection` varchar(3) DEFAULT NULL,
  `immune_compromised` varchar(3) DEFAULT NULL,
  `poor_oral_hygiene` varchar(3) DEFAULT NULL,
  `sun_exposure` varchar(3) DEFAULT NULL,
  `tobacco_use` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_patient_health_details`
--

INSERT INTO `tbl_patient_health_details` (`id`, `lifestyle_habits`, `symptoms`, `created_at`, `patient_id`, `alcohol_consumption`, `betel_quid_use`, `diet_intake`, `family_history`, `hpv_infection`, `immune_compromised`, `poor_oral_hygiene`, `sun_exposure`, `tobacco_use`) VALUES
(1, 'Non Smoker Excercise Regularly', 'Pains', '2026-01-31 06:34:20.288232', 1, 'Yes', 'Yes', 'Low', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_patient_lab_test`
--

CREATE TABLE `tbl_patient_lab_test` (
  `id` int(11) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `appointment_id` int(11) NOT NULL,
  `lab_test_id` int(11) NOT NULL,
  `patient_id` int(11) NOT NULL,
  `report_file` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_patient_lab_test`
--

INSERT INTO `tbl_patient_lab_test` (`id`, `status`, `created_at`, `appointment_id`, `lab_test_id`, `patient_id`, `report_file`) VALUES
(1, 'Processing', '2026-02-11 09:15:48.130797', 2, 2, 1, ''),
(2, 'Completed', '2026-02-11 09:15:48.142290', 2, 3, 1, 'lab_reports/2.pdf'),
(3, 'Completed', '2026-02-11 09:15:48.148603', 2, 4, 1, 'lab_reports/1.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_prescription`
--

CREATE TABLE `tbl_prescription` (
  `prescription_id` int(11) NOT NULL,
  `diagnosis` longtext DEFAULT NULL,
  `medicine_details` longtext DEFAULT NULL,
  `medicine_usage` longtext DEFAULT NULL,
  `more_details` longtext DEFAULT NULL,
  `next_visit_date` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `appointment_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_prescription`
--

INSERT INTO `tbl_prescription` (`prescription_id`, `diagnosis`, `medicine_details`, `medicine_usage`, `more_details`, `next_visit_date`, `created_at`, `appointment_id`) VALUES
(1, 'Oral aphthous ulcer', 'Mouthwash - Chlorhexidine gluconate 0.12%, twice daily for 7 days; Painkiller - Paracetamol 500mg, thrice daily for 5 days', 'Use mouthwash after meals. Take painkillers with food', 'Avoid spicy and hot foods. Maintain oral hygiene', '2026-02-07', '2026-01-31 06:55:30.239933', 1),
(2, '1. Hexigel Oral Gel – apply locally\r\n2. Becosules Capsules – once daily\r\n3. Dologel CT – apply on ulcer before meals', 'Apply Hexigel gently on the affected area twice daily after meals.\r\nApply Dologel CT 10 minutes before food.\r\nTake Becosules capsule once daily after breakfast.\r\nAvoid spicy and hot food during treatment.', 'Apply Hexigel gently on the affected area twice daily after meals.\r\nApply Dologel CT 10 minutes before food.\r\nTake Becosules capsule once daily after breakfast.\r\nAvoid spicy and hot food during treatment.', 'Maintain good oral hygiene.\r\nAvoid tobacco and alcohol.\r\nDrink plenty of water.\r\nIf pain or ulcer persists beyond 2 weeks, report immediately.', '2026-02-18', '2026-02-10 09:25:29.096799', 2),
(3, '1. Hexigel Oral Gel – apply locally\r\n2. Becosules Capsules – once daily\r\n3. Dologel CT – apply on ulcer before meals', 'Apply Hexigel gently on the affected area twice daily after meals.\r\nApply Dologel CT 10 minutes before food.\r\nTake Becosules capsule once daily after breakfast.\r\nAvoid spicy and hot food during treatment.', 'Apply Hexigel gently on the affected area twice daily after meals.\r\nApply Dologel CT 10 minutes before food.\r\nTake Becosules capsule once daily after breakfast.\r\nAvoid spicy and hot food during treatment.', 'Maintain good oral hygiene.\r\nAvoid tobacco and alcohol.\r\nDrink plenty of water.\r\nIf pain or ulcer persists beyond 2 weeks, report immediately.', '2026-02-27', '2026-02-24 09:10:42.373394', 10);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_radiotherapy`
--

CREATE TABLE `tbl_radiotherapy` (
  `radio_id` int(11) NOT NULL,
  `session_no` int(11) NOT NULL,
  `radiation_type` varchar(100) NOT NULL,
  `dose` varchar(100) NOT NULL,
  `radio_date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `appointment_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_radiotherapy`
--

INSERT INTO `tbl_radiotherapy` (`radio_id`, `session_no`, `radiation_type`, `dose`, `radio_date`, `created_at`, `appointment_id`) VALUES
(1, 4, 'External Beam Radiation Therapy (EBRT)', '2', '2026-02-13', '2026-02-13 05:22:55.466690', 8),
(2, 4, 'External Beam Radiation Therapy (EBRT)', '2', '2026-02-20', '2026-02-13 05:22:55.470954', 8),
(3, 4, 'External Beam Radiation Therapy (EBRT)', '2', '2026-02-28', '2026-02-13 05:22:55.475955', 8),
(4, 4, 'External Beam Radiation Therapy (EBRT)', '2', '2026-03-13', '2026-02-13 05:22:55.479967', 8);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `tbl_appointment`
--
ALTER TABLE `tbl_appointment`
  ADD PRIMARY KEY (`appointment_id`),
  ADD KEY `tbl_appointment_doctor_id_6cf9cfb4_fk_tbl_doctor_doctor_id` (`doctor_id`),
  ADD KEY `tbl_appointment_department_id_edb73c5f_fk_tbl_depar` (`department_id`),
  ADD KEY `tbl_appointment_patient_id_38986c1a_fk_tbl_patient_patient_id` (`patient_id`),
  ADD KEY `tbl_appointment_health_details_id_d0d838b1_fk_myapp_pat` (`health_details_id`);

--
-- Indexes for table `tbl_chemotherapy`
--
ALTER TABLE `tbl_chemotherapy`
  ADD PRIMARY KEY (`chemo_id`),
  ADD KEY `tbl_chemotherapy_appointment_id_2408e0d5_fk_tbl_appoi` (`appointment_id`);

--
-- Indexes for table `tbl_clinical_examination`
--
ALTER TABLE `tbl_clinical_examination`
  ADD PRIMARY KEY (`clinical_examination_id`),
  ADD UNIQUE KEY `appointment_id` (`appointment_id`);

--
-- Indexes for table `tbl_complaint`
--
ALTER TABLE `tbl_complaint`
  ADD PRIMARY KEY (`complaint_id`),
  ADD KEY `tbl_complaint_patient_id_db97cb08_fk_tbl_patient_patient_id` (`patient_id`);

--
-- Indexes for table `tbl_department`
--
ALTER TABLE `tbl_department`
  ADD PRIMARY KEY (`department_id`);

--
-- Indexes for table `tbl_doctor`
--
ALTER TABLE `tbl_doctor`
  ADD PRIMARY KEY (`doctor_id`),
  ADD KEY `tbl_doctor_department_id_ab2bb761_fk_tbl_depar` (`department_id`),
  ADD KEY `tbl_doctor_login_id_7a977e8f_fk_tbl_login_login_id` (`login_id`);

--
-- Indexes for table `tbl_emergency_message`
--
ALTER TABLE `tbl_emergency_message`
  ADD PRIMARY KEY (`message_id`),
  ADD KEY `tbl_emergency_message_doctor_id_7359b951_fk_tbl_doctor_doctor_id` (`doctor_id`),
  ADD KEY `tbl_emergency_messag_patient_id_e3599031_fk_tbl_patie` (`patient_id`);

--
-- Indexes for table `tbl_feedback`
--
ALTER TABLE `tbl_feedback`
  ADD PRIMARY KEY (`fd_id`),
  ADD KEY `tbl_feedback_patient_id_b05fd51a_fk_tbl_patient_patient_id` (`patient_id`);

--
-- Indexes for table `tbl_lab`
--
ALTER TABLE `tbl_lab`
  ADD PRIMARY KEY (`lab_id`),
  ADD KEY `tbl_lab_login_id_d6b181a8_fk_tbl_login_login_id` (`login_id`);

--
-- Indexes for table `tbl_lab_test`
--
ALTER TABLE `tbl_lab_test`
  ADD PRIMARY KEY (`test_id`),
  ADD KEY `tbl_lab_test_lab_id_4ca353a7_fk_tbl_lab_lab_id` (`lab_id`);

--
-- Indexes for table `tbl_login`
--
ALTER TABLE `tbl_login`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `tbl_oncology_case`
--
ALTER TABLE `tbl_oncology_case`
  ADD PRIMARY KEY (`oncology_case_id`),
  ADD UNIQUE KEY `appointment_id` (`appointment_id`),
  ADD KEY `tbl_oncology_case_doctor_id_6f35e0bb_fk_tbl_doctor_doctor_id` (`doctor_id`),
  ADD KEY `tbl_oncology_case_patient_id_8069c2b3_fk_tbl_patient_patient_id` (`patient_id`);

--
-- Indexes for table `tbl_patient`
--
ALTER TABLE `tbl_patient`
  ADD PRIMARY KEY (`patient_id`),
  ADD KEY `tbl_patient_login_id_f930270a_fk_tbl_login_login_id` (`login_id`);

--
-- Indexes for table `tbl_patient_doctor_message`
--
ALTER TABLE `tbl_patient_doctor_message`
  ADD PRIMARY KEY (`message_id`),
  ADD KEY `tbl_patient_doctor_m_doctor_id_236b8bcf_fk_tbl_docto` (`doctor_id`),
  ADD KEY `tbl_patient_doctor_m_patient_id_f56af2ae_fk_tbl_patie` (`patient_id`);

--
-- Indexes for table `tbl_patient_health_details`
--
ALTER TABLE `tbl_patient_health_details`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `patient_id` (`patient_id`);

--
-- Indexes for table `tbl_patient_lab_test`
--
ALTER TABLE `tbl_patient_lab_test`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tbl_patient_lab_test_appointment_id_7dd3c9fb_fk_tbl_appoi` (`appointment_id`),
  ADD KEY `tbl_patient_lab_test_lab_test_id_af338f7a_fk_tbl_lab_t` (`lab_test_id`),
  ADD KEY `tbl_patient_lab_test_patient_id_d6147711_fk_tbl_patie` (`patient_id`);

--
-- Indexes for table `tbl_prescription`
--
ALTER TABLE `tbl_prescription`
  ADD PRIMARY KEY (`prescription_id`),
  ADD UNIQUE KEY `appointment_id` (`appointment_id`);

--
-- Indexes for table `tbl_radiotherapy`
--
ALTER TABLE `tbl_radiotherapy`
  ADD PRIMARY KEY (`radio_id`),
  ADD KEY `tbl_radiotherapy_appointment_id_817dc8b8_fk_tbl_appoi` (`appointment_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `tbl_appointment`
--
ALTER TABLE `tbl_appointment`
  MODIFY `appointment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `tbl_chemotherapy`
--
ALTER TABLE `tbl_chemotherapy`
  MODIFY `chemo_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tbl_clinical_examination`
--
ALTER TABLE `tbl_clinical_examination`
  MODIFY `clinical_examination_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_complaint`
--
ALTER TABLE `tbl_complaint`
  MODIFY `complaint_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_department`
--
ALTER TABLE `tbl_department`
  MODIFY `department_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbl_doctor`
--
ALTER TABLE `tbl_doctor`
  MODIFY `doctor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbl_emergency_message`
--
ALTER TABLE `tbl_emergency_message`
  MODIFY `message_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_feedback`
--
ALTER TABLE `tbl_feedback`
  MODIFY `fd_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_lab`
--
ALTER TABLE `tbl_lab`
  MODIFY `lab_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_lab_test`
--
ALTER TABLE `tbl_lab_test`
  MODIFY `test_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_login`
--
ALTER TABLE `tbl_login`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tbl_oncology_case`
--
ALTER TABLE `tbl_oncology_case`
  MODIFY `oncology_case_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_patient`
--
ALTER TABLE `tbl_patient`
  MODIFY `patient_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_patient_doctor_message`
--
ALTER TABLE `tbl_patient_doctor_message`
  MODIFY `message_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbl_patient_health_details`
--
ALTER TABLE `tbl_patient_health_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_patient_lab_test`
--
ALTER TABLE `tbl_patient_lab_test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_prescription`
--
ALTER TABLE `tbl_prescription`
  MODIFY `prescription_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_radiotherapy`
--
ALTER TABLE `tbl_radiotherapy`
  MODIFY `radio_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `tbl_appointment`
--
ALTER TABLE `tbl_appointment`
  ADD CONSTRAINT `tbl_appointment_department_id_edb73c5f_fk_tbl_depar` FOREIGN KEY (`department_id`) REFERENCES `tbl_department` (`department_id`),
  ADD CONSTRAINT `tbl_appointment_doctor_id_6cf9cfb4_fk_tbl_doctor_doctor_id` FOREIGN KEY (`doctor_id`) REFERENCES `tbl_doctor` (`doctor_id`),
  ADD CONSTRAINT `tbl_appointment_health_details_id_d0d838b1_fk_myapp_pat` FOREIGN KEY (`health_details_id`) REFERENCES `tbl_patient_health_details` (`id`),
  ADD CONSTRAINT `tbl_appointment_patient_id_38986c1a_fk_tbl_patient_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `tbl_patient` (`patient_id`);

--
-- Constraints for table `tbl_chemotherapy`
--
ALTER TABLE `tbl_chemotherapy`
  ADD CONSTRAINT `tbl_chemotherapy_appointment_id_2408e0d5_fk_tbl_appoi` FOREIGN KEY (`appointment_id`) REFERENCES `tbl_appointment` (`appointment_id`);

--
-- Constraints for table `tbl_clinical_examination`
--
ALTER TABLE `tbl_clinical_examination`
  ADD CONSTRAINT `tbl_clinical_examina_appointment_id_dde99a80_fk_tbl_appoi` FOREIGN KEY (`appointment_id`) REFERENCES `tbl_appointment` (`appointment_id`);

--
-- Constraints for table `tbl_complaint`
--
ALTER TABLE `tbl_complaint`
  ADD CONSTRAINT `tbl_complaint_patient_id_db97cb08_fk_tbl_patient_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `tbl_patient` (`patient_id`);

--
-- Constraints for table `tbl_doctor`
--
ALTER TABLE `tbl_doctor`
  ADD CONSTRAINT `tbl_doctor_department_id_ab2bb761_fk_tbl_depar` FOREIGN KEY (`department_id`) REFERENCES `tbl_department` (`department_id`),
  ADD CONSTRAINT `tbl_doctor_login_id_7a977e8f_fk_tbl_login_login_id` FOREIGN KEY (`login_id`) REFERENCES `tbl_login` (`login_id`);

--
-- Constraints for table `tbl_emergency_message`
--
ALTER TABLE `tbl_emergency_message`
  ADD CONSTRAINT `tbl_emergency_messag_patient_id_e3599031_fk_tbl_patie` FOREIGN KEY (`patient_id`) REFERENCES `tbl_patient` (`patient_id`),
  ADD CONSTRAINT `tbl_emergency_message_doctor_id_7359b951_fk_tbl_doctor_doctor_id` FOREIGN KEY (`doctor_id`) REFERENCES `tbl_doctor` (`doctor_id`);

--
-- Constraints for table `tbl_feedback`
--
ALTER TABLE `tbl_feedback`
  ADD CONSTRAINT `tbl_feedback_patient_id_b05fd51a_fk_tbl_patient_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `tbl_patient` (`patient_id`);

--
-- Constraints for table `tbl_lab`
--
ALTER TABLE `tbl_lab`
  ADD CONSTRAINT `tbl_lab_login_id_d6b181a8_fk_tbl_login_login_id` FOREIGN KEY (`login_id`) REFERENCES `tbl_login` (`login_id`);

--
-- Constraints for table `tbl_lab_test`
--
ALTER TABLE `tbl_lab_test`
  ADD CONSTRAINT `tbl_lab_test_lab_id_4ca353a7_fk_tbl_lab_lab_id` FOREIGN KEY (`lab_id`) REFERENCES `tbl_lab` (`lab_id`);

--
-- Constraints for table `tbl_oncology_case`
--
ALTER TABLE `tbl_oncology_case`
  ADD CONSTRAINT `tbl_oncology_case_appointment_id_03d8f439_fk_tbl_appoi` FOREIGN KEY (`appointment_id`) REFERENCES `tbl_appointment` (`appointment_id`),
  ADD CONSTRAINT `tbl_oncology_case_doctor_id_6f35e0bb_fk_tbl_doctor_doctor_id` FOREIGN KEY (`doctor_id`) REFERENCES `tbl_doctor` (`doctor_id`),
  ADD CONSTRAINT `tbl_oncology_case_patient_id_8069c2b3_fk_tbl_patient_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `tbl_patient` (`patient_id`);

--
-- Constraints for table `tbl_patient`
--
ALTER TABLE `tbl_patient`
  ADD CONSTRAINT `tbl_patient_login_id_f930270a_fk_tbl_login_login_id` FOREIGN KEY (`login_id`) REFERENCES `tbl_login` (`login_id`);

--
-- Constraints for table `tbl_patient_doctor_message`
--
ALTER TABLE `tbl_patient_doctor_message`
  ADD CONSTRAINT `tbl_patient_doctor_m_doctor_id_236b8bcf_fk_tbl_docto` FOREIGN KEY (`doctor_id`) REFERENCES `tbl_doctor` (`doctor_id`),
  ADD CONSTRAINT `tbl_patient_doctor_m_patient_id_f56af2ae_fk_tbl_patie` FOREIGN KEY (`patient_id`) REFERENCES `tbl_patient` (`patient_id`);

--
-- Constraints for table `tbl_patient_health_details`
--
ALTER TABLE `tbl_patient_health_details`
  ADD CONSTRAINT `myapp_patienthealthd_patient_id_0b13d021_fk_tbl_patie` FOREIGN KEY (`patient_id`) REFERENCES `tbl_patient` (`patient_id`);

--
-- Constraints for table `tbl_patient_lab_test`
--
ALTER TABLE `tbl_patient_lab_test`
  ADD CONSTRAINT `tbl_patient_lab_test_appointment_id_7dd3c9fb_fk_tbl_appoi` FOREIGN KEY (`appointment_id`) REFERENCES `tbl_appointment` (`appointment_id`),
  ADD CONSTRAINT `tbl_patient_lab_test_lab_test_id_af338f7a_fk_tbl_lab_t` FOREIGN KEY (`lab_test_id`) REFERENCES `tbl_lab_test` (`test_id`),
  ADD CONSTRAINT `tbl_patient_lab_test_patient_id_d6147711_fk_tbl_patie` FOREIGN KEY (`patient_id`) REFERENCES `tbl_patient` (`patient_id`);

--
-- Constraints for table `tbl_prescription`
--
ALTER TABLE `tbl_prescription`
  ADD CONSTRAINT `tbl_prescription_appointment_id_f7b8015b_fk_tbl_appoi` FOREIGN KEY (`appointment_id`) REFERENCES `tbl_appointment` (`appointment_id`);

--
-- Constraints for table `tbl_radiotherapy`
--
ALTER TABLE `tbl_radiotherapy`
  ADD CONSTRAINT `tbl_radiotherapy_appointment_id_817dc8b8_fk_tbl_appoi` FOREIGN KEY (`appointment_id`) REFERENCES `tbl_appointment` (`appointment_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
