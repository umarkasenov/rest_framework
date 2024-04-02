from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView

from .serializers import UserCreateSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import ConfirmationCode
from rest_framework.generics import CreateAPIView


class RegisterView(CreateAPIView):
    queryset = ConfirmationCode.objects.all()
    serializer_class = UserCreateSerializer

    def register(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            is_active=False,
        )

        confirmation_code = ConfirmationCode.create(user)

        return Response(data={"user_id": user.id, "confirmation_code": confirmation_code.code},
                        status=status.HTTP_201_CREATED)


class LoginView(CreateAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if user:
            # Token.objects.get_or_create(user=user)
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)

            return Response(data={"key": token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "User doesn't exists"})


class ConfirmAPIView(APIView):
    def post(self, request):
        confirmation_code = request.data.get('confirmation_code')

        try:
            code_object = ConfirmationCode.objects.get(code=confirmation_code)
        except ConfirmationCode.DoesNotExist:
            return Response({"error": "Invalid confirmation code"}, status=status.HTTP_400_BAD_REQUEST)

        code_object.is_verified = True
        code_object.save()

        return Response({"message": "Confirmation code verified successfully"}, status=status.HTTP_200_OK)
