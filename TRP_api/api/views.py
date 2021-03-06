from django.shortcuts import render

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

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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

##########LOGIN END#####################

@api_view(['POST'])
def gettruckowner(request):
    if request.method =='POST':
        id = request.data.get('id',None)
        if id is not None:
            stu = TruckOwnerModel.objects.get(email_id=id)
            serializer = TruckOwnerModelSerializer(stu)
            return  Response(serializer.data,status=status.HTTP_200_OK)
        else:
            stu =TruckOwnerModel.objects.all()
            serializer = TruckOwnerModelSerializer(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['POST'])
def gettransporter(request):
    if request.method =='POST':
        id = request.data.get('id',None)
        if id is not None:
            stu = TransporterModel.objects.get(email=id)
            serializer = TransporterModelSerializer(stu)
            return  Response(serializer.data,status=status.HTTP_200_OK)
        else:
            stu =TransporterModel.objects.all()
            serializer = TransporterModelSerializer(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['POST'])
def getagent(request):
    if request.method =='POST':
        id = request.data.get('id',None)
        if id is not None:
            stu = Tranage_Agent.objects.get(email_id=id)
            serializer = Tranage_AgentSerializer(stu)
            return  Response(serializer.data,status=status.HTTP_200_OK)
        else:
            stu =Tranage_Agent.objects.all()
            serializer = Tranage_AgentSerializer(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['POST'])
def getdriver(request):
    if request.method =='POST':
        id = request.data.get('id',None)
        if id is not None:
            stu = DriverRegistrationModel.objects.filter(registered_by=id)
            serializer = DriverRegistrationSerializer(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)
        else:
            stu =DriverRegistrationModel.objects.all()
            serializer = DriverRegistrationSerializer(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['POST'])
def getvehicle(request):
    if request.method =='POST':
        id = request.data.get('id',None)
        if id is not None:
            stu = VehicleRegistraionModel.objects.filter(registered_by=id)
            serializer = VehicleRegistraionModelSerializer(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)
        else:
            stu =VehicleRegistraionModel.objects.all()
            serializer = VehicleRegistraionModelSerializer(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)
class TruckOwnerModel_View(ModelViewSet):
    queryset  = TruckOwnerModel.objects.all()
    serializer_class = TruckOwnerModelSerializer
    authetication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
class TransporterModel_View(ModelViewSet):
    queryset  = TransporterModel.objects.all()
    serializer_class = TransporterModelSerializer
    authetication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
class Tranage_AgentSerializer_View(ModelViewSet):
    queryset  = Tranage_Agent.objects.all()
    serializer_class = Tranage_AgentSerializer
    authetication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
class VehicleRegistraionModelSerializer_View(ModelViewSet):
    queryset  = VehicleRegistraionModel.objects.all()
    serializer_class = VehicleRegistraionModelSerializer
    authetication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
class DriverRegistrationSerializer_View(ModelViewSet):
    queryset  = DriverRegistrationModel.objects.all()
    serializer_class = DriverRegistrationSerializer
    authetication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]



# class GetTruckOwner(ModelViewSet):
#     serializer_class = TruckOwnerModelSerializer
#     queryset = TruckOwnerModel.objects.all()
#     def get_queryset(self):
#         queryset = self.queryset
#         query_set = queryset.filter(id=pk)
#         return query_set