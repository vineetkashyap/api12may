from .models import *
from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
class TruckOwnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =TruckOwnerModel
        fields  = '__all__'

class TransporterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =TransporterModel
        fields  = '__all__'

class VehicleRegistraionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =VehicleRegistraionModel
        fields  = '__all__'

class DriverRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model =DriverRegistrationModel
        fields  = '__all__'

class Tranage_AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Tranage_Agent
        fields  = '__all__'