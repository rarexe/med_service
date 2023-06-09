from rest_framework import generics
from anketa_app.serializers import *
import pickle
import numpy as np
from rest_framework.response import Response
from django.views.generic import View
from openpyxl import Workbook
from django.http import HttpResponse
from .models import Anketa, FakeAnketa
from datetime import datetime
from django.shortcuts import get_object_or_404

class AnketaCreateAPIView(generics.CreateAPIView):
    serializer_class = AnketaSerializer

class AnketaListAPIView(generics.ListAPIView):
    serializer_class = AnketaSerializer
    queryset = Anketa.objects.all()

class FakeAnketaCreateAPIView(generics.CreateAPIView):
    serializer_class = FakeAnketaSerializer

class DoctorListAPIView(generics.ListAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DoctorCreateAPIView(generics.CreateAPIView):
    serializer_class = DoctorSerializer

class HospitalListAPIView(generics.ListAPIView):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()

class HospitalCreateAPIView(generics.CreateAPIView):
    serializer_class = HospitalSerializer

class DepartmentListAPIView(generics.ListAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class DepartmentCreateAPIView(generics.CreateAPIView):
    serializer_class = DepartmentSerializer

with open('anketa_app/perceptron_model.pkl', 'rb') as file:
    model = pickle.load(file)

class PerceptronPredictView(generics.GenericAPIView):
    serializer_class = MyModelSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # получаем данные из сериализатора
        data = serializer.validated_data['data']

        # преобразуем список в numpy array
        data = np.array(data).reshape(1, -1)

        # обрабатываем данные и передаем их в модель
        prediction = model.predict(data)

        # возвращаем результат в формате JSON
        return Response({'prediction': prediction.tolist()})


class AnketaXlsxView(View):
    def get(self, request):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="anketa.xlsx"'

        # Создание книги Excel
        workbook = Workbook()
        worksheet = workbook.active

        # Добавление заголовков в таблицу
        headers = ['personal_number', 'data_time', 'hospital', 'department', 'doctor', 'age', 'gender', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'result_treatment', 'result_relationship', 'result_stigma', 'result_condition', 'result_total']

        worksheet.append(headers)

        # Получение данных из модели Anketa
        anketa_list = Anketa.objects.all().values_list('personal_number', 'data_time', 'hospital', 'department', 'doctor', 'age', 'gender', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'result_treatment', 'result_relationship', 'result_stigma', 'result_condition', 'result_total')

        # Добавление данных в таблицу
        for anketa in anketa_list:
            row = []
            for i, cell in enumerate(anketa):
                if i == 2:
                    hospital_id = cell
                    hospital = get_object_or_404(Hospital, id=hospital_id)
                    cell = hospital.hospital_name
                elif i == 3:
                    department_id = cell
                    department = get_object_or_404(Department,
                                                   id=department_id)
                    cell = department.department_name
                elif i == 4:
                    doctor_id = cell
                    doctor = get_object_or_404(Doctor, id=doctor_id)
                    cell = doctor.doctor_name
                elif isinstance(cell, datetime):
                    cell = cell.replace(tzinfo=None)
                    cell = cell.strftime("%Y-%m-%d %H:%M:%S")
                row.append(cell)
            worksheet.append(row)

        workbook.save(response)
        return response

class FakeAnketaXlsxView(View):
    def get(self, request):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="fake_anketa.xlsx"'

        # Создание книги Excel
        workbook = Workbook()
        worksheet = workbook.active

        # Добавление заголовков в таблицу
        headers = ['personal_number', 'data_time', 'hospital', 'department', 'doctor', 'age', 'gender', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'result_treatment', 'result_relationship', 'result_stigma', 'result_condition', 'result_total']

        worksheet.append(headers)

        # Получение данных из модели Anketa
        anketa_list = FakeAnketa.objects.all().values_list('personal_number', 'data_time', 'hospital', 'department', 'doctor', 'age', 'gender', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'result_treatment', 'result_relationship', 'result_stigma', 'result_condition', 'result_total')

        # Добавление данных в таблицу
        for anketa in anketa_list:
            row = []
            for i, cell in enumerate(anketa):
                if i == 2:
                    hospital_id = cell
                    hospital = get_object_or_404(Hospital, id=hospital_id)
                    cell = hospital.hospital_name
                elif i == 3:
                    department_id = cell
                    department = get_object_or_404(Department, id=department_id)
                    cell = department.department_name
                elif i == 4:
                    doctor_id = cell
                    doctor = get_object_or_404(Doctor, id=doctor_id)
                    cell = doctor.doctor_name
                elif isinstance(cell, datetime):
                    cell = cell.replace(tzinfo=None)
                    cell = cell.strftime("%Y-%m-%d %H:%M:%S")
                row.append(cell)
            worksheet.append(row)

        workbook.save(response)
        return response