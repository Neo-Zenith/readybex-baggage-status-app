
from rest_framework import serializers
from .models import User, Baggage

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('passportNo', 'bookingNo')

class StatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baggage
        fields = ('serialID', 'status')

class CheckInExtendedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baggage
        fields = ('serialID', 'status')

class CheckInSerializer(serializers.ModelSerializer):
    checkInExtended = CheckInExtendedSerializer()

    class Meta:
        model = User
        fields = ('name', 'passportNo', 'bookingNo', 'checkInExtended')

