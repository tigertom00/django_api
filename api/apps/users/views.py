from rest_framework import viewsets, permissions, mixins, status, generics
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenViewBase
from .serializers import UsersSerializer, MyTokenObtainPairSerializer, TokenObtainLifetimeSerializer, TokenRefreshLifetimeSerializer
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import CustomUser, PictureProfile

User = get_user_model()

class UsersViewSet(viewsets.ModelViewSet):

    serializer_class = UsersSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    # queryset = User.objects.all()
    
    # def get_object(self, queryset=None, **kwargs):
    #     item = self.kwargs.get('pk')
    #     print('########', item)
    #     return get_object_or_404(User, username=item)

    def get_queryset(self):
        
        # return self.queryset.filter(username=self.request.user)
        return User.objects.all().filter(username=self.request.user)
        # return User.objects.all()

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


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




class UserUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print('################################################################# post >', request.data)
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FileUploadView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_class = (FileUploadParser,)
    

    @csrf_exempt
    def uploaduserprofile( request):

        #fetches specific user image
        if request.method == 'GET':
            print('hello world ########################')
            user_data=JSONParser().parse(request)
            obj=PictureProfile.objects.filter(user=user_data["user"])
            serializer=UserProfileSerializer(obj,many=True)
            return JsonResponse(serializer.data,safe=False)



        if request.method == 'POST':
            print('=====================================================================================>',request.FILES['profile_picture'])
            
            print("##################################################################################### ",request.POST['user'])
            try:
                s = PictureProfile.objects.create(user_id = request.POST['user'], profile_picture=request.FILES['profile_picture'])
                s.save()
            except:
                return JsonResponse('Failed to upload Integrity error',safe=False)

            

            # file_serializer=UserProfileSerializer(request.POST,request.FILES)
        
            # if file_serializer.is_valid():
            #     file_serializer.save()
            return JsonResponse('profile uploded Sucessfully!!',safe=False)
        return JsonResponse('Failed to upload',safe=False)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }






class RefreshTokenView(generics.GenericAPIView):
    
    permission_classes = [
        permissions.AllowAny
    ]
    
    def post(self, request, *args, **kwargs):
        try:
            # data = super().validate(request)
            # refresh = RefreshToken(request['refresh'])
            # print(refresh)
            # refresh_token = request.data["refresh_token"]
            # print(refresh_token)
            print(self.request)
            
            token_data = RefreshToken.for_user(self.request.user)
            return Response({
                'user': UsersSerializer(self.request.user, context=self.get_serializer_context()).data,
                'access_token': str(token_data.access_token),
                'refresh_token': str(token_data),
                    })
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
