# URLs for auth app
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from apps.accounts.views import AuthViewSet, login_view

# Create router for ViewSet endpoints (register, me, etc.)
router = DefaultRouter()
router.register(r'', AuthViewSet, basename='auth')

urlpatterns = [
    # PURE FUNCTION-BASED LOGIN - MUST BE FIRST (Bypasses ViewSet routing issues)
    path('login/', login_view, name='login'),
    
    # JWT token endpoints (SimpleJWT provides these)
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Routed endpoints for register, me, etc. (LAST to avoid conflicts)
    path('', include(router.urls)),
]
