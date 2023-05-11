from django import forms
from django.forms import ModelForm
from .models import DetailCar

# creer une formulaire 

class InputForm(ModelForm):
  class Meta:
      model = DetailCar 
      fields = ('nom', 'resumer', 'contenu', 'auteur', 'date_creer', 'date_mise_en_vente', 'images')
      
      
      labels = {
        'nom':'',
        'resumer':'',
        'contenu':'',
        'contenu':'',
        'auteur':'',
        'date_creer':'',
        'date_mise_en_vente':'',
        'images':'Ajouter une photo ',
      }
      
      widgets = {
        'nom':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Non de votre Vehicule'}),
        'resumer':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Petite Resumer'}),
        # 'images':forms.ImageField(attrs={'class':'form-control'}),
        'contenu':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Description complet'}),
        'auteur':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':"L'auteur du vehicule"}),
        'date_creer':forms.DateInput(attrs={'class':'form-control form-control-lg', 'placeholder':'La date de creation'}),
        'date_mise_en_vente':forms.DateInput(attrs={'class':'form-control form-control-lg', 'placeholder':'La date de mise en vente'}),
      }