from django.contrib import admin
from django.utils.html import format_html

from .models import *


from django.contrib.auth.hashers import make_password

def set_password_action(User, request, queryset):
    for user in queryset:
        user.set_password('desired_password')
        user.save()

set_password_action.short_description = "Set password for selected user(s)"

# Register the action in the admin site
admin.site.add_action(set_password_action)





class HoraireInline(admin.TabularInline):
    model = Horaire
    extra = 1
class CommentaireInline(admin.TabularInline):
    readonly_fields = ('commentaire','user','lieu')
    model = Commentaire
    extra = 1

class EvenementInline(admin.TabularInline):
    model = Evenement
    extra = 1

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    readonly_fields = ('display_photo',)
    def display_photo(self, obj):
        return format_html('<img src="{}" height="100" />'.format(obj.photo.url))

    display_photo.short_description = 'Photo'





class CommentaireAdmin(admin.ModelAdmin):
    list_filter = ('user','lieu')
    readonly_fields = ('commentaire','user','lieu')

    

class PhotoAdmin(admin.ModelAdmin):
    list_filter = ('lieu',)


    


class LieuAdmin(admin.ModelAdmin):
    inlines = [HoraireInline ,EvenementInline,CommentaireInline,PhotoInline]
    list_filter = ('categorie','nom' , 'theme' , 'address')




class UserAdmin(admin.ModelAdmin):
    inlines = [CommentaireInline]
    

from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.hashers import make_password


class CustomUserChangeForm(UserChangeForm):
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(), required=False)

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm

    def save_model(self, request, obj, form, change):
        password = form.cleaned_data.get('password')
        if password:
            obj.set_password(password)
        super().save_model(request, obj, form, change)





    
    

admin.site.register(User , CustomUserAdmin)
admin.site.register(Lieu , LieuAdmin )
admin.site.register(Categorie)
admin.site.register(Theme)
#admin.site.register(Horaire)
admin.site.register(Transport)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(Commentaire,CommentaireAdmin)
#admin.site.register(Evenement)
