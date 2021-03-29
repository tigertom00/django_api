from rest_framework import serializers
from django.contrib.auth import get_user_model

Users = get_user_model()


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
