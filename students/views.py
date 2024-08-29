from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSreializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSreializer

@api_view(['POST'])
def create_student(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSreializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
