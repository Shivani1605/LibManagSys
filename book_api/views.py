
from functools import partial
from django.shortcuts import render

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Books
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def student_api(request , pk=None):
    if request.method ==  'GET':
        id = pk
        if id is not None:                       # this block for when we get id
            stu = Books.objects.get(id=id)
            serializer = BookSerializer(stu)
            return Response(serializer.data)
        stu = Books.objects.all()                 # this is for all data or Query set
        serializer = BookSerializer(stu,many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created !!!' },status = status.HTTP_201_CREATED )

        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'PUT':
        id = pk
        stu = Books.objects.get(pk=id)
        serializer = BookSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Compleate Data Updated !!!'})

        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = pk
        stu = Books.objects.get(pk=id)
        serializer = BookSerializer(stu, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partial Data Updated !!!'})

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        id = pk
        stu = Books.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted !!!'})



            