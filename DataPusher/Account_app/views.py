from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import AccountSerializers, User_Account
from rest_framework import viewsets, mixins
from rest_framework.authtoken.views import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny


# Register View
""" class Register(viewsets.GenericViewSet, mixins.CreateModelMixin,):
   serializer_class = AccountSerializers

   def register(self, request):

      data_dict = self.request.data

      name = data_dict['name']
      email = data_dict['email']
      password = data_dict['password']

      data = User_Account.objects.create(name=name, email=email, password=password)

      if data:
          user = data.set_password(password)
          data.save()
          token = Token.objects.create(user=data)

          return Response({"message": "Registered Successfully", "code": "HTTP_201_CREATED", "Token": token.key})
      else:
          return Response({"message": "Sorry Try Next Time!!!",  "code": "HTTP_403_FORBIDDEN"}) """

# To ckeck if user is Authenticated or Not, use Login
class Login(viewsets.GenericViewSet, mixins.CreateModelMixin,):
    permission_classes = (AllowAny,)
    serializer_class = AccountSerializers

    def create(self, request, *args, **kwargs):

        data_dict = self.request.data

        email = data_dict['email']
        password = data_dict['password']

        data = authenticate(email=email, password=password)

        if data:
            users = Token.objects.filter(user=data).first()

            userData = AccountSerializers(data)

            return Response({"message": "Login Successfully",  "code": "HTTP_200_OK", "token": users.key, "user": userData.data})

        else:
            return Response({"message": "Un Authenticatd User",  "code": "HTTP_401_UNAUTHORIZED"})
        



# Create your views here.
class AccountView(ModelViewSet):
    serializer_class = AccountSerializers
    queryset = User_Account.objects.all()
