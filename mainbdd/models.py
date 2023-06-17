from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , BaseUserManager
from django.core.exceptions import ValidationError

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
        
    def set_password_manually(self, user, password):
        user.set_password(password)
        user.save(using=self._db)





class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to=upload_to, default='posts/default.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True




class Categorie(models.Model):
    CATEGORIE_CHOIX = [
        ('musé', 'musé'),
        ('plage', 'plage'),
        ('forét', 'forét'),
        ('ville', 'ville'),
        ('montagne', 'montagne'),
        ('campagne', 'campagne'),
        ('lac', 'lac'),
        ('rivière', 'rivière'),
        ('désert', 'désert'),
        ('grotte', 'grotte'),
        ('falaise', 'falaise'),
        ("chute d'eau", "chute d'eau"),
        ("mosqué", "mosqué"),
        ("Parc national", "Parc national"),
        ("Patrimoine mondial", "Patrimoine mondial"),

   ]
    nom = models.CharField( max_length=50 , unique = True, )#choices=CATEGORIE_CHOIX )

    def __str__(self):
        return self.nom


class Theme(models.Model):
    nom = models.CharField(max_length=50 , unique = True)
    def __str__(self):
         return self.nom 

class Transport(models.Model):
    transport_CHOIX = [
        ('Car', 'Car'),
        ('Train', 'Train'),
        ('Bus', 'Bus'),
        ('Metro', 'Metro'),
        ('Trame', 'Trame'),
        ('CableCar', 'CableCar'),
    ]
    nom = models.CharField(max_length=50 ,choices=transport_CHOIX , unique = True)
    def __str__(self):
        return self.nom   

class Lieu(models.Model):
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank = True )
    address = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    categorie = models.ForeignKey(Categorie,related_name='lieux', on_delete=models.CASCADE)
    theme = models.ManyToManyField(Theme, related_name='lieux')
    transport = models.ManyToManyField(Transport,related_name='lieux' ,blank=True)
    def __str__(self):
        return self.nom



class Photo(models.Model):
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='photos', null=True)
    photo = models.ImageField(upload_to=upload_to, )
    def __str__(self):
        return self.lieu.nom


class Horaire(models.Model):
    JOUR_CHOIX = [
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'),
        ('Samedi', 'Samedi'),
        ('Dimanche', 'Dimanche'),
    ]
    jour = models.CharField(max_length=10 , choices =JOUR_CHOIX )
    heur_ouverture = models.TimeField(auto_now=False, auto_now_add=False)
    heur_fermeture = models.TimeField(auto_now=False, auto_now_add=False)
    lieu = models.ForeignKey(Lieu,related_name='horaires' , on_delete=models.CASCADE )

    class Meta:
        unique_together = ('jour','lieu')

    def __str__(self):
        return self.lieu.nom + '_' + self.jour





class Commentaire(models.Model):
    commentaire = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='commentairs')
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='commentairs')
    time = models.DateTimeField( auto_now_add=True )
    def __str__(self):
        return self.user.first_name +" "+ self.user.last_name + " : " + self.commentaire


class Evenement(models.Model):
    nom = models.CharField(max_length=50)
    date_debut = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_fin = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=200)
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='evenements')
    def __str__(self):
        return self.nom
    def clean(self):
        if self.date_debut > self.date_fin:
            raise ValidationError('La date de début doit être inférieure à la date de fin.')




