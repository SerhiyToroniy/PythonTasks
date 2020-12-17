from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Patient(models.Model):
    name = models.CharField(verbose_name='Name', db_index=True, max_length=100)
    date = models.CharField(verbose_name='Date', db_index=True, max_length=100)
    time = models.CharField(verbose_name='Time', db_index=True, max_length=100)
    duration = models.IntegerField(verbose_name='Duration', db_index=True)
    doctor_name = models.CharField(verbose_name='Doctor_name', db_index=True, max_length=100)
    DEPARTMENT_TYPES = (
        (1, 'Osteopathy'),
        (2, "Dentistry"),
        (3, "Ophthalmology"),
        (4, 'Dermatology')
    )
    department = models.CharField(verbose_name='Department', max_length=100, choices=DEPARTMENT_TYPES)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
