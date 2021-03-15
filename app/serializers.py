from rest_framework import serializers
from .models import Crud


class CrudSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=222)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=222)
    password = serializers.CharField(max_length=222)

    def create(self, validated_data):
        return Crud.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

