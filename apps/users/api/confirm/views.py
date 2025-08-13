from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User

from .serializers import UserConfirmSerializer


class UserConfirmView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        phone_number = serializer.validated_data['phone_number']
        # confirmation_code = serializer.validated_data['confirmation_code']
        
        try:
            user = User.objects.get(phone_number=phone_number, is_confirmed=False)
            
            # Bu yerda confirmation_code tekshiriladi (aslida SMS service bilan integratsiya)
            # if not verify_confirmation_code(phone_number, confirmation_code):
            #     return Response(
            #         {"success": False, "message": "Tasdiqlash kodi noto'g'ri"},
            #         status=status.HTTP_400_BAD_REQUEST
            #     )
            
            user.is_confirmed = True
            user.save()
            
            return Response({
                "success": True,
                "message": "Hisob muvaffaqiyatli tasdiqlandi"
            })
            
        except User.DoesNotExist:
            return Response({
                "success": False,
                "message": "Foydalanuvchi topilmadi yoki allaqachon tasdiqlangan"
            }, status=status.HTTP_404_NOT_FOUND)
        
__all__ = [
    UserConfirmView
]