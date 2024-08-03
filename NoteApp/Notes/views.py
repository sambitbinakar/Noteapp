from django.shortcuts import render
from .models import Note
from .serializers import noteserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(["GET","POST"])
def notes(request):
    if request.method =="GET":
        notes =Note.objects.all()
        seriallizer = noteserializer(notes ,many =True)
        return Response (seriallizer.data)
    elif request.method == "POST":
        seriallizer = noteserializer(data=request.data)
        if seriallizer.is_valid():
            seriallizer.save()
            return Response(seriallizer.data, status=status.HTTP_201_CREATED)
        return Response(seriallizer.errors ,status=status.HTTP_400_BAD_REQUEST)
