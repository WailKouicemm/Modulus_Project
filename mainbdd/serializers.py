
from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerialzers
from rest_framework import serializers

from .models import *


class UserCreateSerialzers(BaseUserSerialzers) :
    class Meta(BaseUserSerialzers.Meta) :
        fields = ['id' , 'password' , 'email' , 'first_name' , 'last_name' ]


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'





class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'



class HoraireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horaire
        fields = '__all__'


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire()
        fields = '__all__'


class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = '__all__'


class LieuSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer()
    horaires = HoraireSerializer(many = True)
    theme = ThemeSerializer(many = True)
    transport = TransportSerializer(many = True)
    class Meta:
        model = Lieu
        fields = '__all__'