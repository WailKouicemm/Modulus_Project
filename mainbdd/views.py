from django.shortcuts import render



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def req(request):
    user = request.user
    # do something with the current user
    return Response({'email': user.email})


