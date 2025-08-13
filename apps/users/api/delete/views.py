from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserDeleteSerializer


class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserDeleteSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        
        user = request.user
        
        # Save deletion reason if provided
        if 'reason_delete_choices' in serializer.validated_data:
            user.reason_delete_choices = serializer.validated_data['reason_delete_choices']
        if 'reason_delete_str' in serializer.validated_data:
            user.reason_delete_str = serializer.validated_data['reason_delete_str']
        
        # Perform soft deletion
        user.delete_account()
        
        return Response({
            "success": True,
            "message": "Hisob muvaffaqiyatli o'chirildi"
        })
    
__all__ = [
    UserDeleteView
]