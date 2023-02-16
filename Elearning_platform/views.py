from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication

from .models import User
from .serializers import UserSerializer, LoginSerializer


# --------Viewsets
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        auth = authenticate(username=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if auth:
            try:
                email = User.objects.get(email=serializer.validated_data['email'])
            except:
                return Response({'Fatal error': 'Detection of extinct animals'})
            user = User.objects.get(email=email)
            # user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            person = UserSerializer(user).data
            return Response({'token': token.key, 'user': person})
        else:
            return Response({'Fatal error': 'Detection of extinct animals'})

    # serializer_class = LoginSerializer
    # authentication_classes = [TokenAuthentication]
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = AuthTokenSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data['user']
    #     token = Token.objects.create(user)
    #
    #     return Response({'status': 'logged in successfully'})
    #
    # def list(self, request, *args, **kwargs):
    #     user=self.request.user
    #     return Response({"data":user})
    # def get_queryset(self):
    #     pass


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'ok': 'OO gya ee'})