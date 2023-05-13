
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('me/',views.me ),
    path('search/',views.search),
    path('AllLieux/',views.getallLieux),
    path('lieu/<int:id>/',views.getLieu),
    path('commentairs/<int:id>/',views.getallCommentairs),
    path('commenter/<int:id>/',views.Commenter ),
    path('evenements_adj/',views.evenements_adj ),
]






