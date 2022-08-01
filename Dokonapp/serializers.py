from rest_framework import serializers

from .models import *


class Suv_serializers(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = "__all__"

class Admin_serializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

class Mijoz_serializers(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = "__all__"

class Haydovchi_serializers(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = "__all__"

class Buyurtma_serializers(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"