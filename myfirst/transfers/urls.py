from django.contrib import admin
from django.urls import path, include
from patients.views import *

app_name ='transfers'
urlpatterns = [
    path('transfers/create/', PatientCreateView.as_view()),
    path('all/', PatientListView.as_view()),
    path('transfers/detail/<int:pk>/', PatientDetailView.as_view())
]

