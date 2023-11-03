
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate,get_user_model
from rest_framework.authtoken.models import Token

User=get_user_model()

class RegisterView(APIView):
    def post(self,request):
        data=request.data
        serializer=RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response(
                {
                    'status':'False',
                    'message':serializer.errors
                }
            )
        instance=serializer.save()
        print(instance)
        return Response({'message':'User account created'})
    

class LoginView(APIView):

    def post(self , request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors
            }) 

        user = authenticate(username = serializer.data['username'] , password = serializer.data['password'])

        if not user:
            return Response({
                'status':False,
                'message': 'invalid credentials'
            })
        
        token, created = Token.objects.get_or_create(user=user)
        if created:
            token.save()

        return Response({'message':"user login" , 'token':str(token),'user_id': user.id,
            'username': user.username,})