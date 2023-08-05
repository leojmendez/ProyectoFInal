from django.shortcuts import render, get_object_or_404
from ShowApp.models import Art, Cooking, HandWork, ProjectsDesign, Travel, Economy, Comentario
from django.http import HttpResponse
from ShowApp.forms import ArtFormulario, ArtEditFoto, FormularioComentario
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.


def home(request):
    #avatares= Avatar.objects.filter(user=request.user.id)
    return render (request,"home.html") #,{"url": avatares[0].imagen.url})

def art(request):
    return render (request,'art.html')

@login_required
def artFormulario(request):
      if request.method == "POST":
          miFormulario=ArtFormulario(request.POST, request.FILES) #dodne llega la información del html
          print(request.FILES)
          print(miFormulario)
          if miFormulario.is_valid():
              information = miFormulario.cleaned_data
              art = Art(category= information['category'],
                        name=information['name'],
                        description=information['description'],
                        contactNumber=information['contactNumber'],
                        email=information['email'],
                        pics=request.FILES['pics'])
              art.save()
              return render(request, 'art.html')
      else:
          miFormulario=ArtFormulario()
      return render(request, "artForm.html",{"miFormulario":miFormulario})

def artReadFotografia(request):
    artFoto=Art.objects.filter(category__startswith='fotografia')
    context={"artFoto":artFoto}
    return render(request, 'artReadFoto.html', context)

def artDeleteFoto(request, foto_name):
    artFoto= Art.objects.filter(name__startswith=foto_name)
    artFoto.delete()

    artFotos = Art.objects.filter(category__startswith='fotografia')  
 
    context = {"artFotos": artFotos}
 
    return render(request, 'art.html', context)

class FotoUpdate(LoginRequiredMixin, UpdateView):
    model = Art
    form_class = ArtEditFoto
    success_url = reverse_lazy('ArtReadFoto')
    context_object_name = 'fotografia'
    template_name = 'artEditFoto.html'

@login_required
def expandObject(request, foto_name):
    artFoto = get_object_or_404(Art, name__startswith=foto_name)
    comentarios = artFoto.comentarios.all()  # Obtener todos los comentarios asociados al objeto
    context = {'artFoto': artFoto, 'comentarios': comentarios}
    return render(request, 'expandObject.html', context)


class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('ArtReadFoto')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)
    
def team(request):
    return render(request, 'team.html', {})

def workinprogress(request):
    return render(request, 'workinprogress.html', {})

    