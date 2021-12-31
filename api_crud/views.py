from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer

from .utilities import *
from django.http import Http404








from rest_framework.views import APIView
from rest_framework.response import Response



#CRUD API
class student_list(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(success_added("Data successfully inserted",serializer.data),status=CREATED)
        return Response(data_fail("Data Invalid",serializer.errors),status=BAD_REQUEST)
    
    
       
class student_detail(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
        

    def get(self, request, pk ):
        stu = self.get_object(pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        stu = self.get_object(pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(update_data("Data successfully updated",serializer.data),status=OK)
        return Response(data_fail("Update Invalid",serializer.errors),status=BAD_REQUEST)
    
    def patch(self, request, pk):
        stu = self.get_object(pk)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(update_data("Data Successfully Updated",serializer.data),status=OK)
  
        return Response(data_fail("Update Invalid",serializer.errors),status=BAD_REQUEST)


    def delete(self, request, pk,):
        stu = self.get_object(pk)
        stu.delete()
        return Response(deleted_data("Data successfully deleted"),status=NO_CONTENT)

    
    