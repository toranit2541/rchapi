from rest_framework import serializers
from .models import Package

# class PackageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Package
#         fields = '__all__'  # or specify individual fieldsfrom rest_framework import serializers
# from .models import Package

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
        read_only_fields = ['uploaded_at']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be a positive value.")
        return value

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("Start date must be earlier than end date.")
        return data
