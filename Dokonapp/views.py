from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class SuvApiView(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = Suv_serializers


class MijozApiView(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = Mijoz_serializers

class AdminApiView(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = Admin_serializers

class HaydovchiApiView(ModelViewSet):
    queryset = Haydovchi.objects.all()
    serializer_class = Haydovchi_serializers

class BuyurtmaApiView(ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = Buyurtma_serializers
