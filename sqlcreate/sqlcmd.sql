SELECT TOP 6 CONVERT(varchar, VnDate, 3) AS VnDateTH, PtLabResFiltered.LabResultCode, LabApp.LabNameTh, PtLabResFiltered.* 
FROM (SELECT PtLabRes.*, ROW_NUMBER() OVER(PARTITION BY PtLabRes.VnDate ORDER BY PtLabRes.VnDate) AS RowNum 
FROM PtLabRes INNER JOIN LabResultDetail ON PtLabRes.LabResultCode = LabResultDetail.LabResultCode 
INNER JOIN PatientInHos ON PtLabRes.VN = PatientInHos.VN AND PtLabRes.VnDate = PatientInHos.VnDate 
INNER JOIN PatientData ON PatientData.HN = PatientInHos.HN AND PatientData.HnYear = PatientInHos.HnYear 
INNER JOIN LabApplication ON LabApplication.LabResultCode = LabResultDetail.LabResultCode 
WHERE PatientData.CitizenID = @CitizenID AND LabResultDetail.LabResultCode = @LabResultCode ) AS PtLabResFiltered 
INNER JOIN LabApplication AS LabApp ON PtLabResFiltered.LabResultCode = LabApp.LabResultCode 
WHERE PtLabResFiltered.RowNum = 1 ORDER BY VnDate DESC;

select * from LabApplication;

SELECT * FROM RchApplication WHERE CitizenID=@CitizenID;

WITH TopDates AS ( SELECT TOP 10 MAX(PtLabRes.VnDate) AS VnDate FROM PtLabRes INNER JOIN LabResultDetail ON PtLabRes.LabResultCode = LabResultDetail.LabResultCode 
INNER JOIN PatientInHos ON PtLabRes.VN = PatientInHos.VN AND PtLabRes.VnDate = PatientInHos.VnDate INNER JOIN PatientData ON PatientData.HN = PatientInHos.HN AND PatientData.HnYear = PatientInHos.HnYear WHERE CitizenID = @CitizenID 
GROUP BY PtLabRes.VN ORDER BY MAX(PtLabRes.VnDate) DESC ) SELECT DISTINCT CONVERT(varchar, VnDate, 23) AS VnDate FROM TopDates ORDER BY VnDate DESC;

select CONVERT(varchar, PtLabRes.VnDate, 23)as VnDate from PtLabRes INNER JOIN LabResultDetail ON PtLabRes.LabResultCode = LabResultDetail.LabResultCode INNER JOIN PatientInHos ON PtLabRes.VN = PatientInHos.VN AND PtLabRes.VnDate = PatientInHos.VnDate
INNER JOIN PatientData ON PatientData.HN = PatientInHos.HN and PatientData.HnYear = PatientInHos.HnYear where CitizenID=@CitizenID GROUP BY PtLabRes.VnDate ORDER BY PtLabRes.VnDate;

select CONVERT(varchar, PtLabRes.VnDate, 23)as VnDate from PtLabRes INNER JOIN LabResultDetail ON PtLabRes.LabResultCode = LabResultDetail.LabResultCode INNER JOIN PatientInHos ON PtLabRes.VN = PatientInHos.VN AND PtLabRes.VnDate = PatientInHos.VnDate 
INNER JOIN PatientData ON PatientData.HN = PatientInHos.HN and PatientData.HnYear = PatientInHos.HnYear where CitizenID=@CitizenID GROUP BY PtLabRes.VnDate ORDER BY PtLabRes.VnDate

select CONVERT(varchar, PtLabRes.VnDate, 23)as VnDate from PtLabRes INNER JOIN LabResultDetail ON PtLabRes.LabResultCode = LabResultDetail.LabResultCode INNER JOIN PatientInHos ON PtLabRes.VN = PatientInHos.VN AND PtLabRes.VnDate = PatientInHos.VnDate
INNER JOIN PatientData ON PatientData.HN = PatientInHos.HN and PatientData.HnYear = PatientInHos.HnYear where CitizenID=@CitizenID GROUP BY PtLabRes.VnDate ORDER BY PtLabRes.VnDate

SELECT * FROM RchApplication WHERE CitizenID=@CitizenID and password=@password

SELECT * FROM RchApplication WHERE CitizenID=@CitizenID

select * from LabApplication

WITH TopDates AS ( SELECT TOP 10 MAX(PtLabRes.VnDate) AS VnDate FROM PtLabRes INNER JOIN LabResultDetail ON PtLabRes.LabResultCode = LabResultDetail.LabResultCode
INNER JOIN PatientInHos ON PtLabRes.VN = PatientInHos.VN AND PtLabRes.VnDate = PatientInHos.VnDate INNER JOIN PatientData ON PatientData.HN = PatientInHos.HN AND PatientData.HnYear = PatientInHos.HnYear WHERE CitizenID = @CitizenID 
GROUP BY PtLabRes.VN ORDER BY MAX(PtLabRes.VnDate) DESC ) SELECT DISTINCT CONVERT(varchar, VnDate, 23) AS VnDate FROM TopDates ORDER BY VnDate DESC;

select CONVERT(varchar, PtLabRes.VnDate, 23)as VnDatetime,* from PtLabRes INNER JOIN LabResultDetail ON PtLabRes.LabResultCode = LabResultDetail.LabResultCode INNER JOIN PatientInHos ON PtLabRes.VN = PatientInHos.VN AND PtLabRes.VnDate = PatientInHos.VnDate 
INNER JOIN PatientData ON PatientData.HN = PatientInHos.HN and PatientData.HnYear = PatientInHos.HnYear where CitizenID=@CitizenID and ( PtLabRes.VnDate=@VnDate0 or PtLabRes.VnDate=@VnDate1 or PtLabRes.VnDate=@VnDate2 or PtLabRes.VnDate=@VnDate3 or PtLabRes.VnDate=@VnDate4 or PtLabRes.VnDate=@VnDate5) ORDER BY LabResult;

select * from LabApplication

select CONVERT(varchar, PtLabRes.VnDate, 23)as VnDatetime,* from PtLabRes INNER JOIN LabResultDetail ON PtLabRes.LabResultCode = LabResultDetail.LabResultCode INNER JOIN PatientInHos ON PtLabRes.VN = PatientInHos.VN AND PtLabRes.VnDate = PatientInHos.VnDate
INNER JOIN PatientData ON PatientData.HN = PatientInHos.HN and PatientData.HnYear = PatientInHos.HnYear where CitizenID=@CitizenID and ( PtLabRes.VnDate=@VnDate1 or PtLabRes.VnDate=@VnDate2) ORDER BY LabResult;

select * from PtLabRes INNER JOIN LabResultDetail ON PtLabRes.LabResultCode = LabResultDetail.LabResultCode
INNER JOIN PatientInHos ON PtLabRes.VN = PatientInHos.VN AND PtLabRes.VnDate = PatientInHos.VnDate INNER JOIN PatientData ON PatientData.HN = PatientInHos.HN and PatientData.HnYear = PatientInHos.HnYear 
INNER JOIN LabApplication ON LabApplication.LabResultCode = LabResultDetail.LabResultCode where CitizenID =@CitizenID and PtLabRes.VnDate IN(SELECT MAX(PtLabRes.VnDate) AS Vndate FROM PtLabRes INNER JOIN LabResultDetail ON PtLabRes.LabResultCode = LabResultDetail.LabResultCode
INNER JOIN PatientInHos ON PtLabRes.VN = PatientInHos.VN AND PtLabRes.VnDate = PatientInHos.VnDate INNER JOIN PatientData ON PatientData.HN = PatientInHos.HN and PatientData.HnYear = PatientInHos.HnYear where CitizenID =@CitizenID) ORDER BY LabResult;

select * from PtLabRes INNER JOIN LabResultDetail ON PtLabRes.LabResultCode = LabResultDetail.LabResultCode INNER JOIN PatientInHos ON PtLabRes.VN = PatientInHos.VN AND PtLabRes.VnDate = PatientInHos.VnDate 
INNER JOIN PatientData ON PatientData.HN = PatientInHos.HN and PatientData.HnYear = PatientInHos.HnYear INNER JOIN LabApplication ON LabApplication.LabResultCode = LabResultDetail.LabResultCode where CitizenID=@CitizenID and PtLabRes.VnDate=@VnDate ORDER BY LabResult;


SELECT * FROM RchApplication WHERE CitizenID=@CitizenID;

SELECT * FROM PatientData WHERE CitizenID=@CitizenID

