from django.shortcuts import render
from .models import Detail, OwnerShipProof, Rule
from .serializers import DetailSerializer, OwnerShipProofSerializer, UserSerializer, AccommodationPictureSerializer, RuleSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from deepface import DeepFace
import cv2
from .compareFaces import compare
from PIL import Image
from .decypher import extractText
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
import datetime
import jwt

#from rest_framework.sessions import is_authenticated
# Create your views here.


@api_view(["POST"])
def post(request):
    serializer = DetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    print(serializer.errors)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def verifier(request):
    serializer = OwnerShipProofSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("serializer is valid")
        data = OwnerShipProof.objects.last()
        img1 = str(data.idPic)
        img2 = str(data.img)
        img3 = str(data.proofOfResidence)
        if compare(img1, img2):
            print("your face matched with your id")
            text = extractText(img1)
            x = text.find("Names")
            x += 4
            y = text.find(" ")
            name = text[x+2:y]
            print(name)
            proof = extractText(img3)
            if name.strip() not in proof.split():
                print("process failed")
                return Response("you id details could not be pinned to ")
                data.delete()
            print("details matched proof of residence")
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            data.delete()
            print("restart the process")
            render(serializer.data, status.HTTP_403_FORBIDDEN)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def Login(request):
    if request.user.is_authenticated:
        print("user already logged in")
    else:
        if request.method == 'POST':
            #serializer = UserSerializer(data=request.data)
            username = request.data.get("username")
            password = request.data.get("password")
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            #user = User.objects.filter(username=username).first()
            if user is not None:
                print("found")

                payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
                    'iat': datetime.datetime.utcnow()

                }
                token = jwt.encode(payload, 'secret',
                                   algorithm='HS256')

                print(token)
                response = Response()
                response.set_cookie(key='jwt', value=token, httponly=True)
                response.data = {
                    'jwt': token
                }
                return response({'message': "successfully logged in"})

            else:
                print("user not found")
    return Response("Failed")


@api_view(["POST"])
def register(request):
    if request.user.is_authenticated:
        print("user is already authenticated")

    serializer = UserSerializer(data=request.data)
    """username = request.data
    email = request.data.email
    password = request.data.password
    print(username + " "+password+" "+email)"""
    password = request.data.get("password")

    if serializer.is_valid():
        user = serializer
        #user.password = make_password(password)
        user.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class RegisterApiView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=12)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["POST"])
def postPics(request):
    serializer = AccommodationPictureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def accommodationDetails(request):
    id = request.user.id
    data = Detail.objects.filter(user=id)
    serializer = DetailSerializer(data, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def postRule(request):
    serializer = RuleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRules(request):
    id = request.user.id
    data = Rule.objects.filter(user=id)
    serializer = RuleSerializer(data, many=True)
    return Response(serializer.data)
