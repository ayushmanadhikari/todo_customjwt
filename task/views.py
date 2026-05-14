from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Task, TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
# Create your views here.

class TaskListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        task = Task.objects.all()
        taskSer = TaskSerializer(task, many=True)

        return Response(taskSer.data)
    
    def post(self, request):
        taskSer = TaskSerializer(data=request.data)
        if taskSer.is_valid():
            taskSer.save()
        return Response(f'Task created successfully! /n {taskSer.data}')

    

class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request, pk):
        try: 
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            raise NotFound('Task Not Found!')
        return task
    
    def get(self, request, pk):
        task = self.get_object(request, pk)
        taskSer = TaskSerializer(task)
        return Response(taskSer.data)

    def post(self, request, pk):
        task = self.get_object(request, pk)
        taskSer = TaskSerializer(task, data=request.data)
        if taskSer.is_valid():
            taskSer.save()
            return Response(taskSer.data)
        return Response('Invalid Data!')
    
    def delete(self, request, pk):
        task = self.get_object(request, pk)
        task.delete()
        return Response('Task Deleted Successfully!')