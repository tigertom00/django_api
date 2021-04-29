from rest_framework import viewsets, permissions, mixins, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenViewBase
from .serializers import UsersSerializer, MyTokenObtainPairSerializer, TokenObtainLifetimeSerializer, TokenRefreshLifetimeSerializer
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()


class UsersViewSet(viewsets.ModelViewSet):

    serializer_class = UsersSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = User.objects.all()
    

    def get_queryset(self):
              
        return self.queryset.filter(username=self.request.user)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)



class RefreshTokenView(generics.GenericAPIView):
    
    permission_classes = [
        permissions.AllowAny
    ]
    
    def post(self, request, *args, **kwargs):
        try:
            token_data = RefreshToken.for_user(self.request.user)
            return Response({
                'user': UsersSerializer(self.request.user, context=self.get_serializer_context()).data,
                'access_token': str(token_data.access_token),
                'refresh_token': str(token_data),
                    })
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class BlacklistTokenView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request,):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

class TokenObtainPairView(TokenViewBase):
    """
        Return JWT tokens (access and refresh) for specific user based on username and password.
    """
    serializer_class = TokenObtainLifetimeSerializer


class TokenRefreshView(TokenViewBase):
    """
        Renew tokens (access and refresh) with new expire time based on specific user's access token.
    """
    serializer_class = TokenRefreshLifetimeSerializer
    permission_classes = [permissions.AllowAny]
