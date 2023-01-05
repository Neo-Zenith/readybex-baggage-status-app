from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=500)
    passportNo = models.CharField(max_length=500)
    bookingNo = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Baggage(models.Model):
    serialID = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=500)
    belt = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.serialID