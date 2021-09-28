from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ('__all__')
class PersonSerializer(serializers.Serializer):
    
    def create(self, validated_data):
        return Person.objects.create(**validated_data)
    
    class Meta:
        model = Person
        field = ('__all__')
    