from django.shortcuts import render, redirect
from .models import TaskModel
from .serializers import TaskModelSerializer
from rest_framework import generics
from .forms import TaskForm


class ListCreateTaskView(generics.ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelSerializer


class ReadUpdateDeleteTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelSerializer


def home(request):
    tasks = TaskModel.objects.all()
    context = {'tasks': tasks}
    return render(request, 'base/home.html', context)


def createTask(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/task_form.html', context)
