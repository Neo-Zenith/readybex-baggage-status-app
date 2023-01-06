
from rest_framework import serializers
from .models import User, Baggage

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['bookingNo']

class StatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baggage
        fields = ('serialID', 'status')

class BeltUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baggage
        fields = ['belt', 'serialID']


class CheckInExtendedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baggage
        fields = ['serialID', 'status', 'airline']

class CheckInSerializer(serializers.ModelSerializer):

    checkInExtended = CheckInExtendedSerializer(required=True)
    class Meta:
        model = User
        fields = "__all__"

