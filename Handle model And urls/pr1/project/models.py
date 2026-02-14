from django.db import models
from django.utils import timezone

# Create your models here.
class projectVarity(models.Model):
    PROJECT_TYPE_CHOICE = [
        ('ML', 'MACHINE LEARNING'),
        ('DS', 'DATA SCIENCE'),
        ('FE', 'FRONTEND'),
        ('WD', 'WEBSITE DEVELOPER')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="project/")
    date_added = models.DateTimeField(default = timezone.now)
    type = models.CharField(max_length=2, choices=PROJECT_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name