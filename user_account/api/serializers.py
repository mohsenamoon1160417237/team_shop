from rest_framework import serializers

from user_account.models import BaseUser


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data['password']
        validated_data.pop('password')
        instance = self.Meta.model.objects.create(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance
