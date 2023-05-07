from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from djoser.views import TokenCreateView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from django.db.models import Q
class CustomTokenCreateView(TokenCreateView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        access_token = response.data['access']
        refresh_token = response.data['refresh']

        response.set_cookie(
            'access_token', access_token, 
            httponly=True, samesite='None', secure=True
        )

        response.set_cookie(
            'refresh_token', refresh_token, 
            httponly=True, samesite='None', secure=True
        )

        return response



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    user = request.user
    ser = MyUserSerialzer(user)
    return Response(ser.data)





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getallLieux(request):
    lieus = Lieu.objects.all()
    ser = LieuSerializer_All(lieus, many=True)
    return Response(ser.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getLieu(request,id):
    l = Lieu.objects.get(id=id)
    ser = LieuSerializer(l)
    return Response(ser.data)

#les commentairs d un lieu
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getallCommentairs(request,id):
    lieu = Lieu.objects.get(id=id)
    ser = CommentaireSerializer(lieu.commentairs, many=True)
    return Response(ser.data)





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getall(request):
    user = request.user
    q = Lieu.objects.get(id=1)
    q = Lieu.commentairs
    ser = CommentaireSerializer(Lieu.commentairs, many=True)
    return Response(ser.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search(request):


    queryset = Lieu.objects.all()
    search = request.query_params.get('search')

    if search :
        queryset = queryset.filter(Q(categorie__nom__icontains=search) | Q(theme__nom__icontains=search))

    
    ser = LieuSerializer(queryset, many = True)

    return Response(ser.data)


    



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Commenter(request,id):
    user = request.user
    comm = request.data["commentaire"]
    lieu = Lieu.objects.get(id=id)
    c = Commentaire.objects.create(
        lieu = lieu ,
        user = user,
        commentaire = comm
    )
    ser = CommentaireSerializer(c)
    return Response(ser.data)