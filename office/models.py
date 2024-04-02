from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
class patient(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(120)])
    heartrate=models.IntegerField(default=30,validators=[MinValueValidator(0),MaxValueValidator(200)])

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.heartrate}"
class car(models.Model):
    brand=models.CharField(max_length=30)    
    year=models.IntegerField()
    def __str__(self):
        return f"{self.brand},{self.year}"
    
class review(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=30)
    star=models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])    

