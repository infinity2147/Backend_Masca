from rest_framework.serializers import ModelSerializer
from ..models import User , lib_Admin

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password','Name','profile_photo','DOB','Branch','Roll_no','Hostel','Room')

class lib_AdminSerializer(ModelSerializer):
    class Meta:
        model = lib_Admin
        fields = ('username', 'password','Name','DOB','POR','lib_Admin_no','Address')