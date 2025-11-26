from django.db import models
from django.db.models import Manager
from django.core.exceptions import ValidationError

class PopulationManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Is_Delete=False)

class Population(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='population/')  # Specify your upload directory
    uploaded_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    Is_Delete = models.BooleanField(default=False)

    # Manager for soft deletion
    objects = models.Manager()  # Default manager
    active_objects = PopulationManager()  # Custom manager excluding deleted items

    class Meta:
        ordering = ['-uploaded_at']

    def clean(self):
        # Validate start and end dates
        if self.start_date >= self.end_date:
            raise ValidationError("Start date must be before end date.")
        
        # Validate file size (5 MB limit)
        if self.file and self.file.size > 5 * 1024 * 1024:
            raise ValidationError("File size should not exceed 5 MB.")
    
    def __str__(self):
        return self.title
