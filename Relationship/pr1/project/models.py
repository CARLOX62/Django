from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    

# One to Many

class ProjectReview(models.Model):
    project = models.ForeignKey(projectVarity, on_delete=models.CASCADE, related_name="reviews")    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    commit = models.TextField()
    data_added = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.user.username} review for {self.project.name}'


## Many to Many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    project_varieties = models.ManyToManyField(projectVarity, related_name='stores')


    def __str__(self):
        return self.name
    

# One to One    

class ProjectCertificate(models.Model):
    project = models.OneToOneField(projectVarity, on_delete=models.CASCADE, related_name='certifiacte')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.project}'
    