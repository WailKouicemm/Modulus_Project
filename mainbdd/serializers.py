
from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerialzers


class UserCreateSerialzers(BaseUserSerialzers) :
    class Meta(BaseUserSerialzers.Meta) :
        fields = ['id' , 'password' , 'email' , 'first_name' , 'last_name' ]
