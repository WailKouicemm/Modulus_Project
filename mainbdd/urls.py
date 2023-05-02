
from django.urls import path
from . import views
from .views import CustomTokenCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomTokenCreateView

urlpatterns = [
    path('req/',views.getallLieux ),
    path('filtrer/',views.filtrer ),
    path('AllLieux/',views.getallLieux),
    path('lieu/<int:id>/',views.getLieu),
    path('commentairs/<int:id>/',views.getallCommentairs),
    path('commenter/<int:id>/',views.Commenter ),
]






