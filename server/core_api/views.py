from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *

# Create your views here.
class LoginManager(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            bookingNo = serializer.data.get("bookingNo")

            try:
                user = User.objects.filter(bookingNo=bookingNo)[0]
                baggages = Baggage.objects.filter(owner=user).values()
                baggages = [entry for entry in baggages]
                baggages = sorted(baggages, key=lambda d: d['serialID']) 

                error = "error_OK"
                metadata = {
                    "name": user.name,
                    "passportNo": user.passportNo
                }
                return Response({   "error": error,
                                    "metadata": metadata,
                                    "payload": baggages})

            except:
                error = "error_user_not_found"
                return Response({"error": error})


class StatusUpdateMagaer(APIView):
    serializer_class = StatusUpdateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serialID = serializer.data.get("serialID")
            status = serializer.data.get("status")

            try:
                baggage = Baggage.objects.get(serialID=serialID)
                baggage.status = status

                # Remove this section for future development on belt notification
                if status == "Landed" or status == "Arrived":
                    baggage.belt = 7

                baggage.save()
                error = "error_OK"
                return Response({"error": error})
            
            except:
                error = "error_bag_not_found"
                return Response({"error": error})

class CheckInManager(APIView):
    serializer_class = CheckInSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            passportNo = serializer.data.get("passportNo")
            bookingNo = serializer.data.get("bookingNo")
            serialID = serializer.data.get("checkInExtended")['serialID']
            status = serializer.data.get("checkInExtended")['status']
            airline = serializer.data.get("checkInExtended")['airline']

            try:
                user = User.objects.get(name=name, passportNo=passportNo)
            except:
                user = User(name=name, passportNo=passportNo, bookingNo=bookingNo)
                user.save()

            try:
                baggage = Baggage.objects.get(serialID=serialID)
                baggage.status = status
                error = "error_bag_checked_in"

                return Response({"error": error})
  
            except:
                baggage = Baggage(serialID=serialID, owner=user, status=status, airline=airline)
                baggage.save()
                error = "error_OK"

                return Response({"error": error})

        else:
            print(serializer.data)

class BeltUpdateManager(APIView):
    serializer_class = BeltUpdateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            belt = serializer.data.get("belt")
            serialID = serializer.data.get("serialID")

            try:
                bag = Baggage.objects.get(serialID=serialID)
                bag.belt = belt
                bag.save()
                error = "error_OK"
                return Response({"error": error})

            except:
                error = "error_bag_not_found"
                return Response({"error": error})