from django.urls import path
from .views import *

urlpatterns = [
    path('v1/login', LoginManager.as_view()),
    path('v1/checkIn', CheckInManager.as_view()),
    path('v1/statusUpdate', StatusUpdateMagaer.as_view()),
]