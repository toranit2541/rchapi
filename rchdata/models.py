from decimal import Decimal, InvalidOperation
from django.db import models

# Create your models here.
class PatientData(models.Model):
    HN = models.IntegerField(primary_key=True)
    HnYear = models.DateTimeField()
    BrhCode = models.CharField(max_length=50, null=True, blank=True)
    WhereFile = models.CharField(max_length=50, null=True, blank=True)
    TitleName = models.CharField(max_length=50, null=True, blank=True)
    FName = models.CharField(max_length=100, null=True, blank=True)
    LName = models.CharField(max_length=100, null=True, blank=True)
    Sex = models.CharField(max_length=50, null=True, blank=True)
    IDTypeCode = models.CharField(max_length=1, null=True, blank=True)
    CitizenID = models.CharField(max_length=50, null=True, blank=True)
    BirthDate = models.DateTimeField(null=True, blank=True)
    BloodGroup = models.CharField(max_length=50, null=True, blank=True)
    DrugAllergy = models.CharField(max_length=250, null=True, blank=True)
    OpTaken = models.TextField(null=True, blank=True)
    SmokeHis = models.CharField(max_length=100, null=True, blank=True)
    AlcoholHis = models.CharField(max_length=100, null=True, blank=True)
    Nation = models.CharField(max_length=50, null=True, blank=True)
    Vaccine = models.TextField(null=True, blank=True)
    NationCode = models.CharField(max_length=50, null=True, blank=True)
    Status = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    AddressNo = models.CharField(max_length=50, null=True, blank=True)
    Street = models.CharField(max_length=50, null=True, blank=True)
    Moo = models.CharField(max_length=50, null=True, blank=True)
    TambolCode = models.CharField(max_length=50, null=True, blank=True)
    AumperCode = models.CharField(max_length=50, null=True, blank=True)
    ProvinceCode = models.CharField(max_length=50, null=True, blank=True)
    ZipCode = models.CharField(max_length=50, null=True, blank=True)
    Tel = models.CharField(max_length=50, null=True, blank=True)
    Fax = models.CharField(max_length=50, null=True, blank=True)
    EmrContact = models.CharField(max_length=50, null=True, blank=True)
    HomeAddress = models.CharField(max_length=50, null=True, blank=True)
    HomeStreet = models.CharField(max_length=50, null=True, blank=True)
    HomeMoo = models.CharField(max_length=50, null=True, blank=True)
    HomeTambolCode = models.CharField(max_length=50, null=True, blank=True)
    HomeAumperCode = models.CharField(max_length=50, null=True, blank=True)
    HomeProvinceCode = models.CharField(max_length=50, null=True, blank=True)
    HomeZipCode = models.CharField(max_length=50, null=True, blank=True)
    HomeTel = models.CharField(max_length=50, null=True, blank=True)
    HomeFax = models.CharField(max_length=50, null=True, blank=True)
    PaymentCode = models.CharField(max_length=50, null=True, blank=True)
    CompanyCode = models.CharField(max_length=50, null=True, blank=True)
    OccCode = models.CharField(max_length=50, null=True, blank=True)
    Occupation = models.CharField(max_length=50, null=True, blank=True)
    FinNote2 = models.TextField(null=True, blank=True)
    FinNote = models.CharField(max_length=100, null=True, blank=True)
    FinAdded = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    HisNote = models.CharField(max_length=200, null=True, blank=True)
    Portrait = models.CharField(max_length=100, null=True, blank=True)
    Last_EmID = models.CharField(max_length=50, null=True, blank=True)
    VipCode = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        unique_together = (("HN", "HnYear"),)
        db_table = "PatientData"
        managed = False
        

    def __str__(self):
        return f"HN: {self.HN}, Year: {self.HnYear}"
    
class PatientInHos(models.Model):
    HN = models.IntegerField(null=True, blank=True)
    HnYear = models.DateTimeField(null=True, blank=True)
    VN = models.IntegerField(primary_key=True)
    VnDate = models.DateTimeField()
    BrhCode = models.CharField(max_length=50, null=True, blank=True)
    CheckCode = models.CharField(max_length=50)
    Height = models.CharField(max_length=50, null=True, blank=True)
    Weight = models.CharField(max_length=50, null=True, blank=True)
    BPsys = models.CharField(max_length=50, null=True, blank=True)
    BPdias = models.CharField(max_length=50, null=True, blank=True)
    Temper = models.CharField(max_length=50, null=True, blank=True)
    Pulse = models.CharField(max_length=50, null=True, blank=True)
    ResRate = models.CharField(max_length=50, null=True, blank=True)
    Eye = models.CharField(max_length=50, null=True, blank=True)
    Ear = models.CharField(max_length=50, null=True, blank=True)
    LastMens = models.CharField(max_length=100, null=True, blank=True)
    Symtom = models.TextField(null=True, blank=True)
    Observe = models.CharField(max_length=50, null=True, blank=True)
    Severity = models.SmallIntegerField(null=True, blank=True)
    Back5Day = models.BooleanField(null=True, blank=True)
    Treat = models.TextField(null=True, blank=True)
    PaymentCode = models.CharField(max_length=50, null=True, blank=True)
    SenderName = models.CharField(max_length=50, null=True, blank=True)
    SenderRelation = models.CharField(max_length=50, null=True, blank=True)
    SenderAddress = models.CharField(max_length=100, null=True, blank=True)
    TimeIn = models.DateTimeField(null=True, blank=True)
    TimeOut = models.DateTimeField(null=True, blank=True)
    AdmFlag = models.CharField(max_length=1, null=True, blank=True)
    AdmDrID = models.CharField(max_length=50, null=True, blank=True)
    ForensicFlag = models.BooleanField()
    CompanyCode = models.CharField(max_length=50, null=True, blank=True)
    InsurCode = models.CharField(max_length=50, null=True, blank=True)
    InsurTypeCode = models.CharField(max_length=10, null=True, blank=True)
    XrayFlag = models.CharField(max_length=1, null=True, blank=True)
    PharFlag = models.CharField(max_length=1, null=True, blank=True)
    LabFlag = models.CharField(max_length=1, null=True, blank=True)
    PhytFlag = models.CharField(max_length=1, null=True, blank=True)
    DFFlag = models.CharField(max_length=1, null=True, blank=True)
    TrtFlag = models.CharField(max_length=1, null=True, blank=True)
    DenFlag = models.CharField(max_length=1, null=True, blank=True)
    ORFlag = models.CharField(max_length=1, null=True, blank=True)
    FinStatus = models.CharField(max_length=100, null=True, blank=True)
    face = models.CharField(max_length=100, null=True, blank=True)
    RFhand = models.CharField(max_length=100, null=True, blank=True)
    LFhand = models.CharField(max_length=100, null=True, blank=True)
    RBhand = models.CharField(max_length=100, null=True, blank=True)
    LBhand = models.CharField(max_length=100, null=True, blank=True)
    Fbody = models.CharField(max_length=100, null=True, blank=True)
    Bbody = models.CharField(max_length=100, null=True, blank=True)
    Rbody = models.CharField(max_length=100, null=True, blank=True)
    Lbody = models.CharField(max_length=100, null=True, blank=True)
    EyePic = models.CharField(max_length=100, null=True, blank=True)
    PriceStatus = models.CharField(max_length=5, null=True, blank=True)
    CanCelVN = models.BooleanField(null=True, blank=True)
    EmployeeID = models.CharField(max_length=50, null=True, blank=True)
    Comment = models.CharField(max_length=100, null=True, blank=True)
    CC_PI = models.TextField(null=True, blank=True)
    PE_VE = models.TextField(null=True, blank=True)
    SIG_VE = models.TextField(null=True, blank=True)
    Ix = models.TextField(null=True, blank=True)
    Dx = models.TextField(null=True, blank=True)
    D_Dx = models.TextField(null=True, blank=True)
    Advice_Plan = models.TextField(null=True, blank=True)
    Note = models.TextField(null=True, blank=True)
    NurseNote = models.TextField(null=True, blank=True)
    PrintCount = models.IntegerField(null=True, blank=True)
    SSO_PassA = models.BooleanField(null=True, blank=True)
    API_Epidem_sent = models.BooleanField(null=True, blank=True)

    class Meta:
        unique_together = (("VN", "VnDate"),)
        db_table = "PatientInHos"
        managed = False
        
    def __str__(self):
        return f"VN: {self.VN}, Date: {self.VnDate}"
    
class LabApplication(models.Model):
    ID = models.AutoField(primary_key=True)
    LabNameTH = models.CharField(max_length=255, null=True, blank=True)
    LabNameEN = models.CharField(max_length=255, null=True, blank=True)
    H = models.CharField(max_length=255, null=True, blank=True)
    LabResultCode = models.CharField(max_length=255, null=True, blank=True)
    LabType = models.CharField(max_length=255, null=True, blank=True)
    LabMax = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "LabApplication"
        managed = False
        
    def __str__(self):
        return f"ID: {self.VN}, LabNameEN: {self.LabNameEN}"
    
class PtLabRes(models.Model):
    RunNo = models.AutoField(primary_key=True, default="DEFAULT_CODE")
    VN = models.IntegerField(null=True, blank=True)
    VnDate = models.DateTimeField(null=True, blank=True)
    LabReqNo = models.IntegerField(null=True, blank=True)
    LabResultCode = models.CharField(max_length=50, null=True, blank=True)
    LabResultValue = models.CharField(max_length=500, null=True, blank=True)
    AN = models.IntegerField(null=True, blank=True)
    AnYear = models.DateTimeField(null=True, blank=True)
    EmployeeID = models.CharField(max_length=50, null=True, blank=True)
    ProveByID = models.CharField(max_length=50, null=True, blank=True)
    ProveByIDOld = models.CharField(max_length=50, null=True, blank=True)
    LabResDate = models.DateTimeField(null=True, blank=True)
    LabProveDate = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "PtLabRes"
        managed = False
        
    def __str__(self):
        return f"RunNo: {self.RunNo}, VN: {self.VN}"
        
class LabResultDetail(models.Model):
    LabResultCode = models.CharField(max_length=8, primary_key=True, default="DEFAULT_CODE")
    LabCode = models.CharField(max_length=50, null=True, blank=True)
    LabResult = models.CharField(max_length=100, null=True, blank=True)
    LabResultMIN = models.CharField(max_length=50, null=True, blank=True)
    LabResultMAX = models.CharField(max_length=50, null=True, blank=True)
    LabResultUnit = models.CharField(max_length=50, null=True, blank=True)
    LabResultSort = models.IntegerField(null=True, blank=True)
    LISLabCode = models.CharField(max_length=6, null=True, blank=True)
    LISLabResultCode = models.CharField(max_length=6, null=True, blank=True)

    class Meta:
        db_table = "LabResultDetail"
        managed = False
        
    def __str__(self):
        return f"LabResultCode: {self.LabResultCode}"
    
class VResultApp(models.Model):
    lab_name_th = models.CharField(max_length=255, db_column="LabNameTH")
    lab_result_value = models.CharField(max_length=255, db_column="LabResultValue")
    lab_result_min = models.DecimalField(max_digits=10, decimal_places=2, db_column="LabResultMIN", null=True, blank=True)
    lab_result_max = models.DecimalField(max_digits=10, decimal_places=2, db_column="LabResultMAX", null=True, blank=True)
    lab_result_unit = models.CharField(max_length=50, db_column="LabResultUnit")
    vn_date = models.DateTimeField(db_column="VnDate")
    citizen_id = models.CharField(max_length=13, db_column="CitizenID",primary_key=True)
    
    # @property
    # def lab_result_min(self):
    #     try:
    #         return Decimal(self.LabResultMIN)
    #     except (InvalidOperation, TypeError, ValueError):
    #         return Decimal('0.00')  # Default value in case of conversion failure

    # @property
    # def lab_result_max(self):
    #     try:
    #         return Decimal(self.LabResultMAX)
    #     except (InvalidOperation, TypeError, ValueError):
    #         return Decimal('0.00')  # Default value in case of conversion failure

    class Meta:
        managed = False  # No migrations will be created for this model
        db_table = "V_ResultApp"  # Name of the view in the database
        verbose_name = "Result Application"
        verbose_name_plural = "Result Applications"
        
    