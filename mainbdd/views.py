from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from djoser.views import TokenCreateView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
class CustomTokenCreateView(TokenCreateView):
    def post(self, request, *args, **kwargs):
        # Call the default TokenCreateView and get the response
        response = super().post(request, *args, **kwargs)

        # Get the access and refresh tokens from the response data
        access_token = response.data['access']
        refresh_token = response.data['refresh']

        # Set the access token as a cookie with HttpOnly, SameSite=None and Secure flag
        response.set_cookie(
            'access_token', access_token, 
            httponly=True, samesite='None', secure=True
        )

        # Set the refresh token as a cookie with HttpOnly, SameSite=None and Secure flag
        response.set_cookie(
            'refresh_token', refresh_token, 
            httponly=True, samesite='None', secure=True
        )

        # Return the modified response
        return response



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def req(request):
    user = request.user
    return Response({'email': user.email})





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getallLieux(request):
    lieus = Lieu.objects.all()
    ser = LieuSerializer(lieus, many=True)
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
def filtrer(request):

    categorie = request.GET["categorie"]
    theme = request.GET["theme"]

    lieu = Lieu.objects.all()   
    if categorie != "" :
         lieu = lieu.filter(categorie__nom = categorie)
    if theme != "" :
         lieu = lieu.filter(themes__nom = theme)

    ser = LieuSerializer(lieu, many = True)
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