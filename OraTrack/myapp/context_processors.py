from .models import EmergencyMessage, Doctor

def emergency_count(request):
    if 'doctor_id' in request.session:
        try:
            doctor = Doctor.objects.get(
                doctor_id=request.session['doctor_id']
            )

            pending_count = EmergencyMessage.objects.filter(
                doctor=doctor,
                reply__isnull=True
            ).count()

            return {'pending_count': pending_count}

        except Doctor.DoesNotExist:
            return {}

    return {}