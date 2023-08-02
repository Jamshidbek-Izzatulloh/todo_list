from django.urls import path
from .views import ListCreateTaskView, ReadUpdateDeleteTaskView

urlpatterns = [
    path('', ListCreateTaskView.as_view()),
    path('<pk>', ReadUpdateDeleteTaskView.as_view())
]
