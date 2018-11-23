from django.db import models
from django.contrib.auth.models import User

# Modelo del montruo de la caneca
# superuser : reciclador / reciclador
# Pythonanywhere: aecarmona / Aranda123

#Database host address:aecarmona.mysql.pythonanywhere-services.com
#"Username:aecarmona / Aranda123456
#Your databases: 
#Click a database's name to start a MySQL console logged in to it.

#Start a console on:aecarmona$default


class TipoReciclador(models.Model):
    nombre = models.CharField(max_length = 22) # nivel brallan, nivel chucho, nivel JuanPis, reciclador compulsivo
    def __str__(self):
        return self.nombre
     

DEFAULT_TIPO = 1
class Reciclador(models.Model):
    alias = models.CharField(max_length = 20) #Alias del Jugador
    correo = models.CharField(max_length = 30, blank = True) # Correo e identificador 
    imagen = models.ImageField(upload_to='img/fotosapp/', blank=True, null=True) # Avatar del reciclador    
    monedas = models.IntegerField() # Monedas acumuladas del reciclador, revisar si se quita
    puntos = models.IntegerField() # Punto acumulados del reciclador
    nivelActual = models.IntegerField() # Niveles desbloqueados del reciclador
    tipoReciclador = models.ForeignKey(TipoReciclador,default=DEFAULT_TIPO, on_delete = models.SET_NULL, blank = True, null = True) # nivel brallan, nivel chucho, nivel JuanPis, reciclador compulsivo
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Usuario de Django
    # def __str__(self):
    #     return self.alias



class TipoUso(models.Model):
    nombre = models.CharField(max_length = 20) # Tipo de uso, Hogares, Comercial, Institucional, Industrial, Majeno especial
    descripcion = models.CharField(max_length = 500)
    url = models.CharField(max_length = 250) # Url a la normativa a un site que presente la normatividad
    imagen = models.ImageField(upload_to='img/fotosapp/', blank=True, null=True) # Código de colores del uso
    def __str__(self):
        return self.nombre

class Caneca(models.Model):
    nombre = models.CharField(max_length = 20) # Nombre de respositorio de residuos ej. Resuduos ordinarios reciclables
    descripcion = models.CharField(max_length = 500)
    url = models.CharField(max_length = 250) # Url a la normativa a un site que presente la normatividad
    imagen = models.ImageField(upload_to='img/fotosapp/', blank=True, null=True) # Imagen de la caneca
    tipoUso = models.ForeignKey(TipoUso, on_delete = models.CASCADE) # Referencia al tipo de uso
    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return '%d: %s' % (self.id, self.nombre)



class Residuo(models.Model):
    nombre = models.CharField(max_length = 20) # Nombre de residuo, ej cascara de banano
    imagen = models.ImageField(upload_to='img/fotosapp/', blank=True, null=True) # Imagen del residuo
    descripcion = models.CharField(max_length = 500)
    caneca = models.ManyToManyField(Caneca)
    url = models.CharField(max_length = 250) # Link a la norma o al ejemplo en la red
    def __str__(self):
        return self.nombre

class Nivel(models.Model):
    nombre = models.CharField(max_length = 20) # Nombre del nivel de Juego
    descripcion = models.CharField(max_length = 500) # Descripción del residuo
    imagen = models.ImageField(upload_to='img/fotosapp/', blank=True, null=True) # Imagen del nivel
    caneca1 = models.ForeignKey(Caneca, on_delete = models.SET_NULL, blank = True, null = True, related_name="caneca1") # Primera caneca
    caneca2 = models.ForeignKey(Caneca, on_delete = models.SET_NULL, blank = True, null = True, related_name="caneca2") # Segunda caneca
    caneca3 = models.ForeignKey(Caneca, on_delete = models.SET_NULL, blank = True, null = True, related_name="caneca3") # Tercera Caneca
 
    def __str__(self):
        return self.nombre


class Partida(models.Model):
   reciclador = models.ForeignKey(Reciclador, on_delete = models.CASCADE) # Identificador del jugador
   puntaje = models.IntegerField() # Puntaje de la artida
   niveldesbloqueado = models.IntegerField() # Nivel al que llegó
   fecha = models.DateTimeField(auto_now = True) # Fecha del juego
   def __str__(self):
        return str(reciclador.alias) 
