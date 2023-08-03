from django.db import models


class TaskModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.IntegerField(choices=[(1, "Low"), (2, "Medium"), (3, "High")])
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'task'
