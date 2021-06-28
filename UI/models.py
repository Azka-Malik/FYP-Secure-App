from django.db import models

class RequestApi(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phoneNumber = models.CharField(max_length=200, null=True)
    cnic = models.CharField(max_length=200, null=True)
    apiRequestStatus = models.CharField(max_length=200,default='Pending', null=True)