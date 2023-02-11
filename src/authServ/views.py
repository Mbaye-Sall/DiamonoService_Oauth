import datetime
import jwt
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .emails import sendMail
from .models import UserAccount
from .serializer import UserAccountSerializer


def text(request):
    return HttpResponse("hello world")



class CreateUserView(generics.ListCreateAPIView):

    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer



class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = UserAccount.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("email not correct")
        if user.isActive == False:
            raise AuthenticationFailed("devez activer votre compte")

        if not user.check_password(password):
            raise AuthenticationFailed("incorrect password")

        payload = {"id": user.id,
                   "status": user.role,
                   "exp": datetime.datetime.utcnow() + datetime.timedelta(days=2),
                   "iat": datetime.datetime.utcnow()
                   }

        token = jwt.encode(payload, "DiamonoService", algorithm="HS256")

        response = Response()

        response.set_cookie(key="token", value=token, httponly=True, max_age=datetime.timedelta(days=2))
        response.data = {
            "token": token
        }

        return response


class ActiveCompte(APIView):

    def post(self, request):
        email = request.data["email"]
        user = UserAccount.objects.get(email="email")
        if user.opt == request.data["otp"]:
            user.isActive = True

class ResetPasswordSend(APIView):
    def Post(self,request):
        if "email" in request.data.keys():
            email = request.data["email"]
            sendMail(email)
        else:
            return Response({"message": "email is required"})

        return Response({"message": "go to your mail to check your verification code"})


class ResetPasswordCheck(APIView):
    def Post(self, request):
        data = request.data
        email, opt = data["email"], data["opt"]
        user = UserAccount.objects.get(email=email)
        if user.isActive:
            if data["opt"] == user.otp:
                if "password" in data.keys() and data["password"] != "":
                    user.set_password(data['password'])
                    user.save()
                    return Response({"message": "Updating password sucessfull"})
                else:
                    return Response({"message": "password is required or not empty"})
            else:
                return Response({"message": "opt unchecked"})
        else:
            return Response({"message": "your Account is no longer activated"})


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            payload = jwt.decode(token, "DiamonoService", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")

        userAccount = UserAccount.objects.get(id=payload["id"])

        serialiser = UserAccountSerializer(userAccount)

        return Response(serialiser.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()

        response.delete_cookie("token")
        response.data = {"message": "success"}

        return response





