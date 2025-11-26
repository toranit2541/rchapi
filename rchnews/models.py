from django.db import models

class ActiveNewsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Is_Delete=False)

# Create your models here.
class News(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='news/')  # Specify your upload directory
    uploaded_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    Is_Delete = models.BooleanField(default=False)

    objects = models.Manager()  # Default manager
    active_objects = ActiveNewsManager() 
    