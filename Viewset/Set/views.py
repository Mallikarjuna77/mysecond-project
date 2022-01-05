from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import SriramaSerializers
from .models import Srirama
from rest_framework import status, permissions, generics, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class StudentCurd(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        students_qs = Srirama.objects.all()
        student_serializers = SriramaSerializers(students_qs, many=True)
        return Response(student_serializers.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        student = get_object_or_404(Srirama, id=pk)
        student_serializers = SriramaSerializers(student)
        return Response(student_serializers.data, status=status.HTTP_200_OK)

    def create(self, request):
        student_serializers = SriramaSerializers(data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, ):
        student = get_object_or_404(Srirama, id=pk)
        student_serializers = SriramaSerializers(instance=student, data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_200_OK)

    def delete(self,request, pk=None, ):
        student = get_object_or_404(Srirama, id=pk)
        student.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)

