# Views for auth app
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.models import CustomUser
from apps.accounts.serializers import (
    UserSerializer, 
    UserRegistrationSerializer, 
    LoginSerializer,
    CustomTokenObtainPairSerializer
)


# ============================================================================
# PURE FUNCTION-BASED LOGIN ENDPOINT (Bypasses ViewSet routing issues)
# ============================================================================

@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def login_view(request):
    """
    Raw function-based login endpoint that handles CORS preflight manually.
    This bypasses ViewSet URL routing which was causing 301 redirects.
    """
    
    # Handle CORS preflight
    if request.method == "OPTIONS":
        response = JsonResponse({"status": "ok"})
        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS, GET"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response["Access-Control-Allow-Credentials"] = "true"
        response["Access-Control-Max-Age"] = "3600"
        return response
    
    # Handle POST login request
    try:
        body = json.loads(request.body)
        serializer = LoginSerializer(data=body)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }
            
            response = JsonResponse(response_data, status=200)
            response["Access-Control-Allow-Origin"] = "http://localhost:3000"
            response["Access-Control-Allow-Credentials"] = "true"
            return response
        
        response = JsonResponse(
            {"errors": serializer.errors},
            status=401
        )
        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        response["Access-Control-Allow-Credentials"] = "true"
        return response
        
    except json.JSONDecodeError:
        response = JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )
        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        return response
    except Exception as e:
        response = JsonResponse(
            {"error": str(e)},
            status=500
        )
        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        return response


# ============================================================================
# VIEWSET FOR OTHER ENDPOINTS (register, me)
# ============================================================================

class AuthViewSet(viewsets.ModelViewSet):
    """Authentication endpoints."""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        """Register a new user."""
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Get current user profile."""
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom JWT token view."""
    serializer_class = CustomTokenObtainPairSerializer
