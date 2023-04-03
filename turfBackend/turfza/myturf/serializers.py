from rest_framework import serializers
from .models import Detail, OwnerShipProof, AccommodationPicture, Rule
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField, Base64FileField
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework import status
from rest_framework.response import Response


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = '__all__'


class OwnerShipProofSerializer(serializers.ModelSerializer):
    img = Base64ImageField(max_length=None, use_url=True)
    #idPic = Base64ImageField(max_length=None, use_url=True)
    #proofOfResidence = Base64FileField(max_length=None, use_url=True)

    class Meta:
        model = OwnerShipProof
        fields = [
            "img",
            "idPic",
            "proofOfResidence"
        ]


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
            "password2"
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("Password did not match")
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data["email"]

        )
        user.set_password(validated_data['password'])
        user.save()
        return Response({'message': 'user has been created'})


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class AccommodationPictureSerializer(serializers.ModelSerializer):
    #img = serializers.ListField(child=serializers.FileField())

    class Meta:
        model = AccommodationPicture
        fields = ['user', 'img']


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ['user', 'rule']
