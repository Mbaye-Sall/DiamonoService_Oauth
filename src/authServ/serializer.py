from rest_framework import serializers
from .models import UserAccount
from .emails import sendMail


class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ("first_name", "last_name", "email", "password", "phoneNo", "blocked",
                  "isActive", "removed", "role", "lastActivity", "lat", "lastIpAddress", "lng")

        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):

        password = validated_data.pop('password', None)
        email = validated_data["email"]
        instance = UserAccount(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        sendMail(email)

        return instance

