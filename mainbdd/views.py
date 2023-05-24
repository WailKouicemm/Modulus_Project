from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from djoser.views import TokenCreateView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from django.db.models import Q,Count
from rest_framework.exceptions import NotFound, bad_request
from rest_framework import status

from random import choice
from datetime import datetime, timedelta
from .remplir import import_lieux_from_csv






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
        long = l.longitude
        lat = l.latitude
        events = Evenement.objects.filter(lieu__latitude__range=(lat-1, lat+1),lieu__longitude__range=(long-1, long+1))
        ser = LieuSerializer(l)
        ser2 = EvenementSerializer(events, many=True)

        res = {
            "details":ser.data,
            "evenements_adj":ser2.data
        }
      
        return Response(data=res)
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
@permission_classes([])
def topPlaces(request):
    q = Lieu.objects.all().annotate(c=Count('commentairs')).order_by('-c')[:10]
    ser = LieuSerializer(q, many=True)
    return Response(ser.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search(request):
    try:
        queryset = Lieu.objects.all()
        categorie = request.query_params.get('categorie')
        search = request.query_params.get('search')
        if categorie:
            queryset = queryset.filter(categorie__nom__icontains=categorie)
        if search:
            queryset = queryset.filter(nom__icontains=search)
        if not categorie and not search:
            raise bad_request()
        ser = LieuSerializer(queryset, many = True)

        return Response(ser.data)
    except Exception as e:
        return(Response(data="il n' y a aucun critère pour chercher", status=status.HTTP_400_BAD_REQUEST))


    


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def addphoto(request):
    user = request.user
    file = request.FILES.get('photo')

    if not file :
        return Response("No file uploaded.", status=status.HTTP_400_BAD_REQUEST)

    request.data.pop('photo')
    user.photo = file
    user.save()
    


    return Response("Profile picture updated successfully.", status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creations2(request):
    try:
        # event_names = [
        #     "Algerian Food Festival",
        #     "National Heritage Exhibition",
        #     "Music Concert: Algerian Beats",
        #     "Art Workshop: Expressions of Algeria",
        #     "Cultural Dance Performance: Rhythms of the Sahara"
        # ]

        # event_descriptions = [
        #     "Join us for a delightful celebration of Algerian cuisine.",
        #     "Explore the rich heritage of Algeria through this exhibition.",
        #     "Experience the vibrant music scene of Algeria with this concert.",
        #     "Unleash your creativity at this art workshop inspired by Algeria.",
        #     "Witness mesmerizing dance performances showcasing Algeria's cultural diversity."
        # ]
        event_names = [
    "Algerian Cultural Festival",
    "Traditional Music Showcase",
    "Artisan Craft Fair: Made in Algeria",
    "Exploring Algerian History Symposium",
    "Sahara Adventure Trek",
    "Culinary Delights of Algeria",
    "Photography Exhibition: Colors of Algeria",
    "Youth Sports Tournament",
    "Fashion Show: Algerian Elegance",
    "Film Festival: Algerian Cinema",
    "Sufi Music Concert: Mystical Melodies",
    "Algerian Literature Book Fair",
    "Nature Exploration: Beauty of Algeria",
    "Tech Conference: Innovation Algerie",
    "Charity Gala: Helping Hands for Algeria",
    "Weekend Bazaar: Local Treasures",
    "Dance Workshop: Algerian Rhythms",
    "Educational Symposium: Advancing Algeria",
    "Algerian Tea Tasting Event",
    "Theatre Performance: Stories from Algiers"
]

        event_descriptions = [
    "Celebrate the diverse cultural heritage of Algeria at this festival.",
    "Immerse yourself in the enchanting melodies of traditional Algerian music.",
    "Discover unique handcrafted treasures and support local artisans.",
    "Join us for an insightful symposium exploring Algeria's rich history.",
    "Embark on an exciting adventure through the mesmerizing Sahara desert.",
    "Indulge in a culinary journey through the flavors of Algeria.",
    "Experience the vibrant colors and breathtaking landscapes of Algeria through photography.",
    "Cheer on young athletes as they showcase their skills in various sports.",
    "Witness a showcase of Algerian fashion and elegance.",
    "Explore the world of Algerian cinema through a diverse selection of films.",
    "Immerse yourself in the spiritual experience of Sufi music.",
    "Discover the literary treasures of Algeria at this book fair.",
    "Uncover the natural beauty and wonders of Algeria through guided nature exploration.",
    "Join industry leaders and innovators at this technology conference.",
    "Make a difference in Algeria through this charity gala event.",
    "Shop for unique and locally-made products at this weekend bazaar.",
    "Learn the vibrant dance styles and rhythms of Algeria at this workshop.",
    "Engage in enlightening discussions on advancing education and innovation in Algeria.",
    "Savor the flavors of Algerian tea and learn about its rich cultural significance.",
    "Enjoy a captivating theatre performance showcasing stories from Algiers."
]
        # users = User.objects.all()
        lieux = Lieu.objects.all()
        
        # for _ in range(30):  # Generating 30 commentaires
            # commentaire_text = choice(positive_comments + negative_comments)
            # user = choice(users)
            # lieu = choice(lieux)
            # time = timezone.now()
        start_date = datetime(2023, 5, 12)  # Start date for the first event
        i=0
        for ll in lieux:  # Generating 5 events
            event_duration = timedelta(days=5+i)  # Duration of each event (e.g., 5 days)
            event_name = choice(event_names)
            event_description = choice(event_descriptions)
            event_start = start_date
            event_end = event_start + event_duration
            # event_start = datetime.datetime.now() + datetime.timedelta(days=7)  # Start date 1 week from now
            # event_end = event_start + datetime.timedelta(days=i+3)  # End date 3 days after start
            
            c=Evenement.objects.create(nom=event_name, date_debut=event_start, date_fin=event_end,
                                    description=event_description, lieu=ll)
    
            # c=Commentaire.objects.create(commentaire=commentaire_text, user=user, lieu=lieu, time=time)
            ser = EvenementSerializer(data=c)
            start_date += timedelta(days=7)  # Assuming events occur every 7 days
            if ser.is_valid():
                ser.save()
            i+=1

        return Response(ser.data)
    except Exception as e:
        return(Response(e.args, status=status.HTTP_400_BAD_REQUEST))


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creations(request):
    try: 
        positive_comments = ["Great place to visit!","Excellent service and atmosphere.","Highly recommended!","Loved the experience.","Amazing location.","The staff was incredibly friendly and helpful.",
                            "The food was delicious and well-presented.",
                            "I had a fantastic time at this place.",
                            "The ambiance was cozy and inviting.",
                            "The service was prompt and attentive.",
                            "I would definitely recommend this place to others.",
                            "The prices were reasonable for the quality provided.",
                            "The place had a great atmosphere.",
                            "I was pleasantly surprised by the excellent service.",
                            "The menu had a wide variety of options to choose from.",
                            "The decor was stylish and modern.",
                            "I had a memorable experience at this place.",
                            "The staff went above and beyond to ensure a pleasant visit.",
                            "The drinks were top-notch and well-crafted.",
                            "The place was clean and well-maintained.",
                            "I thoroughly enjoyed my visit to this establishment.",
                            "The portion sizes were generous and satisfying.",
                            "The location was convenient and easy to find.",
                            "The live music added to the enjoyable atmosphere.",
                            "The desserts were heavenly and worth indulging in."]

        negative_comments = ["Poor service, wouldn't go back.","Overpriced for what it offers.","Not worth the hype.","Disappointing experience.","Avoid this place."]

        # users = choice(["1", "2"])
        # lieux = choice(["1", "2", "3", "4"])
        users = User.objects.all()
        lieux = Lieu.objects.all()
        
        for _ in range(40):  # Generating 30 commentaires
            commentaire_text = choice(positive_comments + negative_comments)
            user = choice(users)
            lieu = choice(lieux)
            time = timezone.now()
        
            c=Commentaire.objects.create(commentaire=commentaire_text, user=user, lieu=lieu, time=time)
            ser = CommentaireSerializer(data=c)
            if ser.is_valid():
                ser.save()
        return Response(ser.data)
    except Exception as e:
        return(Response(e.args, status=status.HTTP_400_BAD_REQUEST))



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Commenter(request,id):
    try:
        user = request.user
        comm = request.GET.get('commentaire')
        lieu = Lieu.objects.get(id=id)
        if not lieu:
            raise NotFound("Lieu non trouvé, il faut l'ajouter s'il est dans l'algérie")
        c = Commentaire.objects.create(
            lieu = lieu ,
            user = user,
            commentaire = comm,
            time = timezone.now()
        )
        ser = CommentaireSerializer(data=c)
        if ser.is_valid():
            ser.save()
        return Response({"Commentaire ajouté avec succès"})
    except Exception as e:
        return(Response(e.args, status=status.HTTP_400_BAD_REQUEST))




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def evenements_adj(request):
    try:
        long = float(request.query_params.get('long'))
        lat = float(request.query_params.get('lat'))
    except (ValueError, TypeError):
        return Response("Invalid query parameters", status=status.HTTP_400_BAD_REQUEST)

    events = Evenement.objects.filter(lieu__latitude__range=(lat-2, lat+2),lieu__longitude__range=(long-2, long+2))
    # events=Evenement.objects.all()
    ser = EvenementSerializer(events, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creations3(request):
    try:
        csv_file_path = "dataset/dataset.csv"
        import_lieux_from_csv(csv_file_path)
    except Exception as e:
        print(e.args)
    return Response({"dd":"sq"})