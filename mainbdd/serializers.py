
from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerialzers
from rest_framework import serializers
from django.utils import timezone
from .models import *
from datetime import datetime




class UserCreateSerialzers(BaseUserSerialzers) :
    class Meta(BaseUserSerialzers.Meta) :
        fields = ['id' , 'password' , 'email' , 'first_name' , 'last_name', ]

class MyUserSerialzer(UserSerializer):
    class Meta(UserSerializer.Meta) :
        fields = ['id', 'email' , 'first_name' , 'last_name','photo' ]




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
    user = UserSerializer()
    class Meta:
        model = Commentaire()
        fields = '__all__'


class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = '__all__'
    def to_representation(self, instance):
        algeria_tz = timezone.get_fixed_timezone(60) 
        if instance.date_fin >= timezone.make_aware(datetime.now(), timezone=algeria_tz):
            return super().to_representation(instance)
        return None





class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class LieuSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer()
    horaires = HoraireSerializer(many = True)
    theme = ThemeSerializer(many = True)
    transport = TransportSerializer(many = True)
    photos = PhotoSerializer(many = True)
    evenements = EvenementSerializer(many = True)
    class Meta:
        model = Lieu
        fields = '__all__'


class LieuSerializer_All(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        fields = ['id' , 'nom' , 'address' , 'latitude' , 'longitude' ]