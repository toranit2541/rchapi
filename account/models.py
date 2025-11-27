from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(choices=[('MALE','MALE'),('FEMALE','FEMALE'),('OTHER','OTHER')],max_length=10)
    birthday = models.DateTimeField()
    phonenumber = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True  # No migrations will be created for this model

    
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False  # No migrations will be created for this model
        db_table = "auth_user"
        verbose_name = "Auth User"
        verbose_name_plural = "Auth User"

    def __str__(self):
        return self.username if self.username else "Unknown User"

class Province(models.Model):
    ProvinceCode = models.CharField(max_length=10, primary_key=True)  # Explicit primary key
    ProvinceDesc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "Province"

class Aumper(models.Model):
    AumperCode = models.CharField(max_length=10, primary_key=True)  # Explicit primary key
    AumperDesc = models.CharField(max_length=255)
    province = models.ForeignKey(
        Province, on_delete=models.SET_NULL, null=True, related_name="aumpers", db_column="ProvinceCode"
    )  # Explicit FK column name

    class Meta:
        managed = False
        db_table = "Aumper"

class Tambol(models.Model):
    TambolCode = models.CharField(max_length=10, primary_key=True)  # Explicit primary key
    TambolDesc = models.CharField(max_length=255)
    aumper = models.ForeignKey(
        Aumper, on_delete=models.SET_NULL, null=True, related_name="tambols", db_column="AumperCode"
    )  # Explicit FK column name

    class Meta:
        managed = False
        db_table = "Tambol"

class PatientData(models.Model):
    citizenID = models.CharField(max_length=20, unique=True, primary_key=True)  # Explicit primary key
    HN = models.CharField(max_length=10, blank=True, null=True)
    HnYear = models.CharField(max_length=255, blank=True, null=True)
    titlename = models.CharField(max_length=50, blank=True, null=True)
    addressNo = models.CharField(max_length=10, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    moo = models.CharField(max_length=10, blank=True, null=True)
    
    tambol = models.ForeignKey(
        Tambol, on_delete=models.SET_NULL, null=True, related_name="patient_data", db_column="TambolCode"
    )  # Explicit FK column name

    aumper = models.ForeignKey(
        Aumper, on_delete=models.SET_NULL, null=True, related_name="patient_data", db_column="AumperCode"
    )  # Explicit FK column name

    province = models.ForeignKey(
        Province, on_delete=models.SET_NULL, null=True, related_name="patient_data", db_column="ProvinceCode"
    )  # Explicit FK column name

    zipCode = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False  # No migrations will be created for this model
        db_table = "PatientData"

    def __str__(self):
        return f"Patient {self.citizenID}"

