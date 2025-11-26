from rest_framework import serializers
from .models import Population

# class PopulationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Population
#         fields = '__all__'  # or specify individual fieldsfrom rest_framework import serializers
# from .models import Population

class PopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Population
        fields = '__all__'

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("Start date must be earlier than end date.")
        return data
