from rest_framework import serializers
from .models import *

class AnketaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anketa
        fields = "__all__"

class FakeAnketaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeAnketa
        fields = "__all__"

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class ChartDataSerializer(serializers.Serializer):
    gender = serializers.CharField()
    result_treatment = serializers.FloatField()
    result_relationship = serializers.FloatField()
    result_stigma = serializers.FloatField()
    result_total = serializers.FloatField()

class MyModelSerializer(serializers.Serializer):
    data = serializers.ListField(child=serializers.IntegerField())