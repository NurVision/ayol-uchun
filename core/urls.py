from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path("api/common/", include("apps.common.urls", namespace="common")),
    path("api/courses/", include("apps.courses.urls", namespace="courses")),
    # path("api/news/", include("apps.news.urls", namespace="news")),
    path("api/payments/", include("apps.payments.urls", namespace="payments")),
    path("api/paylov/", include("apps.payments.paylov.urls", namespace="paylov")),
    path("api/users/", include("apps.users.urls", namespace="users")),
]

urlpatterns += swagger_urlpatterns

if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]