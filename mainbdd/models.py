from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , BaseUserManager


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


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    nom = models.CharField( max_length=50)

    def __str__(self):
        return self.nom


class Theme(models.Model):
    nom = models.CharField(max_length=50)
    def __str__(self):
        return self.nom

class Transport(models.Model):
    nom = models.CharField(max_length=50)
    description = models.CharField( max_length=200)
    def __str__(self):
        return self.nom   

class Lieu(models.Model):
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    categorie = models.ForeignKey(Categorie,related_name='lieux', on_delete=models.CASCADE)
    theme = models.ManyToManyField(Theme, related_name='lieux')
    transport = models.ManyToManyField(Transport,related_name='lieux')
    def __str__(self):
        return self.nom





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
    def __str__(self):
        return self.user.first_name +" "+ self.user.last_name


class Evenement(models.Model):
    nom = models.CharField(max_length=50)
    date_debut = models.DateField(auto_now=False, auto_now_add=False)
    date_fin = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=200)
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='evenements')

    def __str__(self):
        return self.nom