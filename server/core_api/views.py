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
            passportNo = serializer.data.get("passportNo")
            bookingNo = serializer.data.get("bookingNo")

            try:
                user = User.objects.get(passportNo=passportNo)
                if user.bookingNo == bookingNo:
                    baggages = Baggage.objects.filter(owner=user)
                    error = "error_OK"
                    return Response({   "error": error,
                                        "payload": baggages})
                
                else:
                    error = "error_incorrect_credentials"
                    return Response({"error": error})

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
                if status == "claimed":
                    baggage.delete()
                else:
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
            status = serializer.data.get("status")
            passportNo = serializer.data.get("passportNo")
            bookingNo = serializer.data.get("bookingNo")
            serialID = serializer.data.get("serialID")

            user = User(name=name, passportNo=passportNo, bookingNo=bookingNo)
            user.save()
            baggage = Baggage(serialID=serialID, owner=user, status=status)
            baggage.save()

            error = "error_OK"
            return Response({"error": error})


