from django.db import models

class Event(models.Model):
    HN = models.CharField(max_length=10)
    HnYear = models.IntegerField()
    Reason = models.CharField(max_length=255, blank=True, null=True)
    MDate = models.DateTimeField(blank=True, null=True)
    MTime = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ScheduleDoctor"
        unique_together = (("HN", "HnYear"),)

    def __str__(self):
        return f"{self.HN} - {self.HnYear} - {self.MDate}"
