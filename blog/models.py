from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DetailCar(models.Model):
  nom = models.CharField(max_length=120, null=True, blank=True)
  resumer = models.TextField(blank=True)
  contenu = models.TextField(blank=True)
  auteur = models.CharField(max_length=60)
  date_creer = models.DateField()
  images = models.ImageField(upload_to='images/', blank=True, null=True)
  date_mise_en_vente = models.DateTimeField(null=True)
  users = models.ForeignKey(User, on_delete=models.CASCADE, default=True, blank=True, null=True)
    
  
    
  def __str__(self) :
      # return self.list_car
      return str(self.nom)
    