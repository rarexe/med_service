from django.urls import path, include
from .views import *
from rest_framework import routers
app_name = 'anketa_app'

urlpatterns = [
    path('anketa', AnketaCreateAPIView.as_view()),
    path('anketa/list', AnketaListAPIView.as_view()),
    path('anketa_fake', FakeAnketaCreateAPIView.as_view()),
    path('doctor/', DoctorListAPIView.as_view()),
    path('doctor/create', DoctorCreateAPIView.as_view()),
    path('department/', DepartmentListAPIView.as_view()),
    path('department/create', DepartmentCreateAPIView.as_view()),
    path('hospital/', HospitalListAPIView.as_view()),
    path('hospital/create', HospitalCreateAPIView.as_view()),
    path('check_anketa', PerceptronPredictView.as_view()),
    path('anketa-xlsx/', AnketaXlsxView.as_view()),
    path('fake_anketa-xlsx/', FakeAnketaXlsxView.as_view()),
]