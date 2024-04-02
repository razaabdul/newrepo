from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class genr(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

class language(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class auther(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True,blank=True)

    class Meta:
        ordering=['last_name','first_name']
    def __str__ (self):
        return f"{self.first_name} {self.last_name}"   


    def get_absolute_url(self):
        return reverse('auther_detail',kwargs={'pk':self.pk })    

class book(models.Model):
    title=models.CharField(max_length=100)
    auther=models.ForeignKey(auther,on_delete=models.SET_NULL,null=True) 
    summary=models.TextField(max_length=50,unique=True)   
    isbn=models.CharField('ISBN',max_length=13)
    language=models.ForeignKey(language,on_delete=models.SET_NULL,null=True)

    genre=models.ManyToManyField(genr)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return  reverse('book_detail',kwargs={'pk':self.pk})
import uuid

class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    book=models.ForeignKey(book,on_delete=models.RESTRICT,null=True)
    imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True,blank=True)
    borrower = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    LOAN_STATUS=(
        ('m','Maintenance'),
        ('o','On Loan'),
        ('a','available'),
        ('r','reversed')
    )
    status=models.CharField(max_length=100,choices=LOAN_STATUS,blank=True,default='m')

    class  META:
        ordering=['due_back']
    
    def  __str__(self):
        return f'{self.id}({self.book.title})'