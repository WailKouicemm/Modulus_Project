from django.contrib import admin

from .models import *


class HoraireInline(admin.TabularInline):
    model = Horaire
    extra = 1
class CommentaireInline(admin.TabularInline):
    model = Commentaire
    extra = 1

class EvenementInline(admin.TabularInline):
    model = Evenement
    extra = 1

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1




class CommentaireAdmin(admin.ModelAdmin):
    list_filter = ('user','lieu')

    



class LieuAdmin(admin.ModelAdmin):
    inlines = [HoraireInline ,EvenementInline,CommentaireInline,PhotoInline]
    list_filter = ('categorie','nom' , 'theme' , 'address','photos')

class UserAdmin(admin.ModelAdmin):
    inlines = [CommentaireInline]
    
    


admin.site.register(User , UserAdmin)
admin.site.register(Lieu , LieuAdmin )
admin.site.register(Categorie)
admin.site.register(Theme)
#admin.site.register(Horaire)
admin.site.register(Transport)
admin.site.register(Photo)
admin.site.register(Commentaire,CommentaireAdmin)
#admin.site.register(Evenement)
