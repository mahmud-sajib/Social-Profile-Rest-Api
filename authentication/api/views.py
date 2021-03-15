# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from .serializers import UserRegisterSerializer
from django.contrib.auth import get_user_model
from .permissions import IsUnAuthenticated

User = get_user_model()

class RegisterApiView(generics.CreateAPIView):

    """permission for this view"""
    permission_classes = [IsUnAuthenticated]
    
    """queryset for this view"""
    queryset = User.objects.all()

    """serializer class"""
    serializer_class = UserRegisterSerializer
    


