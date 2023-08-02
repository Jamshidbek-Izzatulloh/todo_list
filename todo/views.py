from django.shortcuts import render
from .models import TaskModel
from .serializers import TaskModelSerializer
from rest_framework import generics

class ListCreateTaskView(generics.ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelSerializer

class ReadUpdateDeleteTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelSerializer


