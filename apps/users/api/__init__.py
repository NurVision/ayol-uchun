from .confirm import UserConfirmView
from .delete import UserDeleteView
from .login import CustomTokenObtainPairView
from .profile import UserProfileView
from .register import UserRegisterView
from .update import UserUpdateView

__all__ = [
    "CustomTokenObtainPairView",
    "UserConfirmView",
    "UserDeleteView",
    "UserProfileView",
    "UserRegisterView",
    "UserUpdateView",
]
