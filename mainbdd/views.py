from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from djoser.views import TokenCreateView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from django.db.models import Q
# my imports
from rest_framework.exceptions import NotFound, bad_request
from rest_framework import status




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
    try:
        l = Lieu.objects.get(id=id)
        if not l:
            raise NotFound("Lieu non trouvé, il faut l'ajouter s'il est dans l'algérie")
        ser = LieuSerializer(l)
        return Response(ser.data)
    except Exception as e:
        return(Response(data="Lieu non trouvé, il faut l'ajouter s'il est dans l'algérie", status=status.HTTP_404_NOT_FOUND))

#les commentairs d un lieu
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getallCommentairs(request,id):
    try:
        comentaire=Commentaire.objects.filter(lieu=id).order_by("-time")
        ser = CommentaireSerializer(comentaire, many=True)
        return Response(ser.data)
    except Exception as e:
        return(Response(data="Cemmentaire demandé por un lieu non trouvé, il faut l'ajouter s'il est dans l'algérie", status=status.HTTP_404_NOT_FOUND))




# à ne pas faire
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
    try:

        queryset = Lieu.objects.all()
        categorie = request.query_params.get('categorie')
        theme = request.query_params.get('theme')
        search = request.query_params.get('search')
        if categorie:
            queryset = queryset.filter(categorie__nom__icontains=categorie)
        if theme:
            queryset = queryset.filter(themes__nom__icontains=theme)
        if search:
            queryset = queryset.filter(nom__icontains=search)
        if not categorie and not theme and not search:
            raise bad_request()
        ser = LieuSerializer(queryset, many = True)

        return Response(ser.data)
    except Exception as e:
        return(Response(data="il n' y a aucun critère pour chercher", status=status.HTTP_400_BAD_REQUEST))


    




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Commenter(request,id):
    try:
        user = request.user
        comm = request.data["commentaire"]
        lieu = Lieu.objects.get(id=id)
        if not lieu:
            raise NotFound("Lieu non trouvé, il faut l'ajouter s'il est dans l'algérie")
        c = Commentaire.objects.create(
            lieu = lieu ,
            user = user,
            commentaire = comm
        )
        ser = CommentaireSerializer(c)
        return Response(ser.data)
    except Exception as e:
        return(Response(e.args, status=status.HTTP_400_BAD_REQUEST))