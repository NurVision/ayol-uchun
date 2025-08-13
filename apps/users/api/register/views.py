from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.api.register.serializers import UserRegisterSerializer


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response(
            {
                "success": True,
                "message": "Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi",
                "data": {
                    "user_id": user.id,
                    "phone_number": user.phone_number
                }
            },
            status=status.HTTP_201_CREATED
        )
    

__all__ = [
    UserRegisterView
]