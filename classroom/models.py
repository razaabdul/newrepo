from django.db import models

# Create your models here.

class contact_info(models.Model):
    name=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return f"{self.name},{self.message}"

class teacher(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name},{self.last_name} teaches  :  {self.subject}"