from django.db import models
from django.utils import timezone

# Create your models here.
class Art(models.Model):
    classification=(('fotografia','Fotografía'), 
                    ('danza','Danza'),
                    ('dibujo_y_pintura', 'Dibujo y Pintura'),
                     ('manualidades', 'Manualidades'),
                      ('otro', 'Otro'))
    category= models.CharField(max_length=30, choices=classification, default='Fotografía')
    name=models.CharField(max_length=30)
    description=models.TextField(null=True, blank=True)
    date_publish=models.DateField (auto_now_add=True)
    contactNumber = models.IntegerField()
    email = models.EmailField()
    pics = models.ImageField(null=True, blank=True, upload_to="media/")
    def __str__(self):
        #formatted_date = timezone.localtime(self.date_publish).strftime('%d/%m/%Y')
        return f"Categoria: {self.category} - Título: {self.name} - Fecha de Publicación: {self.date_publish}"

class Cooking(models.Model):
    classification=(('tradicional','Tradicional'),
                    ('vegetariana','Vegetariana'),
                    ('vegana','Vegana'),
                    ('sin_tacc','Sin T.A.C.C.'),
                     ('otro', 'Otro'))
    category= models.CharField(max_length=15, choices=classification, default='Tradicional')
    name=models.CharField(max_length=20)
    description=models.TextField(null=True, blank=True)
    date_publish=models.DateTimeField(auto_now_add=True)
    contactNumber = models.IntegerField()
    email = models.EmailField()
    pics = models.ImageField(null=True, blank=True, upload_to="images/")

class HandWork(models.Model):
    classification=(('herreria','Herreria'),
                    ('carpinteria','Carpintería'),
                    ('plomeria','Plomeria'),
                    ('electricidad','Electricidad'),
                    ('otro', 'Otro'))
    category= models.CharField(max_length=15, choices=classification, default='Otro')
    name=models.CharField(max_length=20)
    description=models.TextField(null=True, blank=True)
    date_publish=models.DateTimeField(auto_now_add=True)
    contactNumber = models.IntegerField()
    email = models.EmailField()
    pics = models.ImageField(null=True, blank=True, upload_to="images/")

class ProjectsDesign(models.Model):
    classification=(('ingenieria','Ingeniería'),
                    ('arquitectura','Arquitectura'),
                    ('telecomunicaciones','Telecomunicaciones'),
                    ('otro','Otro'))
    category= models.CharField(max_length=30, choices=classification, default='Otro')
    name=models.CharField(max_length=20)
    description=models.TextField(null=True, blank=True)
    date_publish=models.DateTimeField(auto_now_add=True)
    contactNumber = models.IntegerField()
    email = models.EmailField()
    pics = models.ImageField(null=True, blank=True, upload_to="images/")

class Travel(models.Model):
    classification=(('vuelos','Vuelos'),
                    ('actividades','Actividades'),
                    ('hospedaje','Hospedaje'),
                    ('otro','Otro'))
    category= models.CharField(max_length=15, choices=classification, default='Otro')
    name=models.CharField(max_length=20)
    description=models.TextField(null=True, blank=True)
    date_publish=models.DateTimeField(auto_now_add=True)
    contactNumber = models.IntegerField()
    email = models.EmailField()
    pics = models.ImageField(null=True, blank=True, upload_to="images/")

class Economy(models.Model):
    classification=(('inveriones','Inversiones'),
                    ('contaduria','Contaduria'),
                    ('balances','Balances'),
                    ('otro','Otro'))
    category= models.CharField(max_length=15, choices=classification, default='Otro')
    name=models.CharField(max_length=20)
    description=models.TextField(null=True, blank=True)
    date_publish=models.DateTimeField(auto_now_add=True)
    contactNumber = models.IntegerField()
    email = models.EmailField()
    pics = models.ImageField(null=True, blank=True, upload_to="images/")

class Comentario(models.Model):
    comentario = models.ForeignKey(Art, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)