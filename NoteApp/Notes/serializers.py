from rest_framework import serializers
from .models import Note



class noteserializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        field = ['id','title','content','catagory','created','author']
        # extra_kwargs = {"author":{"read_only":True}}