from django.shortcuts import render
from django.shortcuts import render
from .models import *
from .serializers import  *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import  ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView



from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

##########LOGIN#####################
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

##########LOGIN#####################








# Create your views here.
def student_data(request):
    if request.method =='GET':
        id = request.data.get('id',None)
        if id is not None:
            stu = TruckOwnerModel.objects.get(email_id=id)
            serializer = TruckOwnerModelSerializer(stu)
            return  Response(serializer.data,status=status.HTTP_200_OK)
        else:
            stu =TruckOwnerModel.objects.all()
            serializer = TruckOwnerModelSerializer(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)

class MyList(ListAPIView):
    queryset=TruckOwnerModel.objects.all()
    serializer_class= TruckOwnerModelSerializer
    authetication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MyList1(CreateAPIView):
    queryset=TruckOwnerModel.objects.all()
    serializer_class= TruckOwnerModelSerializer
    authetication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class MyList2(RetrieveAPIView):
    queryset=TruckOwnerModel.objects.all()
    serializer_class= TruckOwnerModelSerializer
    authetication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]




