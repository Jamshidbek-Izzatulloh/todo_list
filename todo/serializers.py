from rest_framework import serializers
from .models import TaskModel

class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'due_date', 'priority', 'completed']

