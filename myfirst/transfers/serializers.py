from rest_framework import serializers
from patients.models import Patient
from validation import *





class PatientDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[isValidName])
    date = serializers.CharField(validators=[isValidDate])
    time = serializers.CharField(validators=[isValidTime])
    duration = serializers.IntegerField(validators=[isValidNumber])
    doctor_name = serializers.CharField(validators=[isValidName])
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Patient
        fields = '__all__'

class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'name', 'date', 'time',  'duration',
                  'doctor_name', 'user', 'department')
