from rest_framework import serializers
from . models import *

class book_serializer(serializers.HyperlinkedModelSerializer): # (HyperLined) you can add url also in fields  
    class Meta:
        model=book
        fields=('id','url','title','summary')