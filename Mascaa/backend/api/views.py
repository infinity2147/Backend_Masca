from rest_framework.viewsets import ModelViewSet
from ..models import User , lib_Admin
from .serializers import UserSerializer , lib_AdminSerializer 

class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer

class lib_AdminViewSet(ModelViewSet):
    queryset=lib_Admin.objects.all()
    serializer_class = lib_AdminSerializer
