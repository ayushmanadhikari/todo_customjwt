from django.urls import path, include
from .views import TaskListView, TaskDetailView

urlpatterns = [
    path('list/', TaskListView.as_view(), name='task-list'),
    path('create/', TaskListView.as_view(), name='task-create'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('update/<int:pk>/', TaskDetailView.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDetailView.as_view(), name='task-delete'),
]