from django.contrib import admin

from .models import *


class HoraireInline(admin.TabularInline):
    model = Horaire
    extra = 1

class LieuAdmin(admin.ModelAdmin):
    inlines = [HoraireInline]
    
    


admin.site.register(User)
admin.site.register(Lieu , LieuAdmin)
admin.site.register(Categorie)
admin.site.register(Theme)
#admin.site.register(Horaire)
admin.site.register(Transport)
admin.site.register(Commentaire)
admin.site.register(Evenement)
