from django.contrib import admin

from .models import *


class HoraireInline(admin.TabularInline):
    model = Horaire
    extra = 1
class CommentaireInline(admin.TabularInline):
    model = Commentaire
    extra = 1
    can_add_related = False

class EvenementInline(admin.TabularInline):
    model = Evenement
    extra = 1


class CommentaireAdmin(admin.ModelAdmin):
    list_filter = ('user','lieu')
    



class LieuAdmin(admin.ModelAdmin):
    inlines = [HoraireInline ,EvenementInline,CommentaireInline ]
    list_filter = ('categorie','nom' , 'theme' , 'address')

class UserAdmin(admin.ModelAdmin):
    inlines = [CommentaireInline]
    
    


admin.site.register(User , UserAdmin)
admin.site.register(Lieu , LieuAdmin)
#admin.site.register(Categorie)
#admin.site.register(Theme)
#admin.site.register(Horaire)
#admin.site.register(Transport)
admin.site.register(Commentaire,CommentaireAdmin)
#admin.site.register(Evenement)
