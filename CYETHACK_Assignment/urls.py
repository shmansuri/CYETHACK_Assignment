
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Events.views import EventViewSet
from Alert.views import AlertViewSet
from users.views import UserViewSet
from users.views import LoginAPIView

router = DefaultRouter()
router.register(r'Events', EventViewSet)
router.register(r'Alert', AlertViewSet)
router.register(r'users', UserViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
     path('login/', LoginAPIView.as_view()),
]
 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns += [
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


