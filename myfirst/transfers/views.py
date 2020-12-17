from django.shortcuts import render
from rest_framework import generics, filters
from patients.serializers import PatientDetailSerializer, PatientListSerializer
from patients.models import Patient
from patients.pagination import PatientPagination

# Create your views here.


class PatientCreateView(generics.CreateAPIView):
    serializer_class = PatientDetailSerializer

class PatientListView(generics.ListAPIView):
	serializer_class = PatientListSerializer
	queryset = Patient.objects.all()
	filter_backends = (filters.SearchFilter, filters.OrderingFilter)
	search_fields = ['id', 'name', 'date', 'time', 'duration', 'doctor_name', 'department']
	pagination_class = PatientPagination


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientDetailSerializer
    queryset = Patient.objects.all()