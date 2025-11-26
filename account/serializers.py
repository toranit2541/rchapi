from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Account, UserProfile, PatientData

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['gender', 'birthday', 'phonenumber']

    def validate_phonenumber(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Phone number must be 10 digits.")
        return value

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    account = AccountSerializer()  # Nested AccountSerializer

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name', 'account')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Password fields didn't match.")
        return attrs

    def create(self, validated_data):
        account_data = validated_data.pop('account')  # Extract nested account data

        with transaction.atomic():
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
            )
            user.set_password(validated_data['password'])
            user.save()

            Account.objects.create(user=user, **account_data)

        return user

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        request = self.context.get('request')
        if not request or not hasattr(request, 'user') or not request.user.check_password(value):
            raise serializers.ValidationError("Old password is not correct.")
        return value

    def update(self, instance, validated_data):
        user = self.context.get('request').user
        if user.pk != instance.pk:
            raise serializers.ValidationError("You don't have permission to update this user.")

        instance.set_password(validated_data['password'])
        instance.save()
        return instance

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError("This username is already in use.")
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.pk != instance.pk:
            raise serializers.ValidationError("You don't have permission to update this user.")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class UserProfileSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)  # No need for `source='user.account'`
    patient_data = serializers.SerializerMethodField()

    class Meta:
        model = User  # Use the actual User model
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'account', 'patient_data']

    def get_patient_data(self, obj):
        """Fetch related PatientData using username as the key."""
        patient = PatientData.objects.filter(citizenID=obj.username).first()
        if patient:
            return {
                "citizenID": patient.citizenID,
                "HN": patient.HN,
                "HnYear": patient.HnYear,
                "titlename": patient.titlename,
                "addressNo": patient.addressNo,
                "street": patient.street,
                "moo": patient.moo,
                "tambol": patient.tambol.TambolDesc if patient.tambol else None,
                "aumper": patient.aumper.AumperDesc if patient.aumper else None,
                "province": patient.province.ProvinceDesc if patient.province else None,
                "zipCode": patient.zipCode,
            }
        return None  # No matching patient data