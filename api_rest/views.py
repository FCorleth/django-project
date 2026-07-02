from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

@api_view(['GET'])
def get_users(request):
    if request.method != 'GET':
        return Response(status=status.HTTP_400_BAD_REQUEST)

    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)
    
@api_view(['GET'])
def get_users_by_nickaname(request, nickname):
    if request.method != 'GET':
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.get(pk=nickname)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)  

    serializer = UserSerializer(user) 

    return Response(serializer.data) 

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):
    try:
        if request.method == 'GET':
            nickname = request.GET['user']

            try:
                user = User.objects.get(pk=nickname)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
            serializer = UserSerializer(user)

            return Response(serializer.data)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        new_user = request.data
        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        nickname = request.data['nickname']
        try:
            updated_user = User.objects.get(pk=nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(updated_user, data=request.data)
        

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)

        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)
