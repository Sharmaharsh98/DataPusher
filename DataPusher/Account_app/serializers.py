from rest_framework import serializers
from .models import User_Account

class AccountSerializers(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User_Account
        fields = ['account_id', 'email', 'name', 'password']

    def create(self, validated_data):
        return User_Account.objects.create_user(**validated_data)