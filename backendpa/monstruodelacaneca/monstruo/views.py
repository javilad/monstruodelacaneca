from django.shortcuts import render
from django.shortcuts import render_to_response
from monstruo.permissions import IsPostOrIsAuthenticated
from monstruo.models import *
from rest_framework import generics
from monstruo.serializers import *
from rest_framework.decorators import permission_classes


# TODO revisar ranking de usuarios con ViewSets

# Create your views here.
def home(request):
    return render_to_response("home.html")

#@permission_classes((IsPostOrIsAuthenticated, ))
class RecicladorList(generics.ListCreateAPIView):
    serializer_class = RecicladorSerializer
    queryset = Reciclador.objects.all()


class RecicladorList10(generics.ListCreateAPIView):
    serializer_class = RecicladorSerializer
    queryset = Reciclador.objects.order_by('-puntos')[:10]

class RecicladorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecicladorSerializer
    queryset = Reciclador.objects.all()

class TipoRecicladorList(generics.ListCreateAPIView):
    serializer_class = TipoRecicladorSerializer
    queryset = TipoReciclador.objects.all()

class TipoRecicladorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TipoRecicladorSerializer
    queryset = TipoReciclador.objects.all()

class TipoUsoList(generics.ListCreateAPIView):
    serializer_class = TipoUsoSerializer
    queryset = TipoUso.objects.all()

class TipoUsoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TipoUsoSerializer
    queryset = TipoUso.objects.all()    

class CanecaList(generics.ListCreateAPIView):
    serializer_class = CanecaSerializer
    queryset = Caneca.objects.all()

class CanecaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CanecaSerializer
    queryset = Caneca.objects.all()        

class ResiduoList(generics.ListCreateAPIView):
    serializer_class = ResiduoSerializer
    queryset = Residuo.objects.order_by('?')[:50]

class ResiduoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResiduoSerializer
    queryset = Residuo.objects.all()            

class PartidaList(generics.ListCreateAPIView):
    serializer_class = PartidaSerializer
    queryset = Partida.objects.all()

class PartidaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PartidaSerializer
    queryset = Partida.objects.all()           

class NivelList(generics.ListCreateAPIView):
    serializer_class = NivelSerializer
    queryset = Nivel.objects.all()

class NivelDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NivelSerializer
    queryset = Nivel.objects.all()      
