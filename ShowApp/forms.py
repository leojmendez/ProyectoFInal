from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User 
from ShowApp.models import Art, Comentario

class ArtFormulario(forms.ModelForm):
    class Meta:
        model = Art
        fields = ('category', 'name', 'description', 'contactNumber', 'email', 'pics')

        widgets = {
            'category' : forms.Select(attrs={'class': 'form-control'}),
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'contactNumber' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
             }

        
class ArtEditFoto(forms.ModelForm):
    class Meta:
        model = Art
        fields = ('category', 'name', 'description', 'email', 'contactNumber','pics')

        widgets = {
            'category' : forms.Select(attrs={'class': 'form-control'}),
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'contactNumber' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            
                        
        }

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }