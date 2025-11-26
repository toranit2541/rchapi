from rest_framework import serializers
from .models import PtLabRes, PatientInHos, PatientData, LabApplication ,LabResultDetail, VResultApp

class PtLabResSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PtLabRes
        fields = '__all__'  # or specify individual fields

class PatientInHosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInHos
        fields = '__all__'  # or specify fields as needed
        
class PatientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientData
        fields = '__all__'  # or specify fields as needed
        
class LabApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabApplication
        fields = '__all__'  # or specify fields as needed
        
class LabResultDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabResultDetail
        fields = '__all__'  # or specify fields as needed
        
class VResultAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = VResultApp
        fields = '__all__'  # or specify fields as needed