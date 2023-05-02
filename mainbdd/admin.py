from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Lieu)
admin.site.register(Categorie)
admin.site.register(Theme)
admin.site.register(Horaire)
admin.site.register(Transport)
admin.site.register(Commentaire)
admin.site.register(Evenement)
