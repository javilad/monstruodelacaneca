from rest_framework import serializers
from monstruo.models import *
from django.contrib.auth.models import User

class RecicladorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, source="user.username")
    nivelActual = serializers.IntegerField(required=False)
    password = serializers.CharField(write_only=True,source="user.password")
    alias = serializers.CharField(required=False)
    correo = serializers.CharField(required=False)
    imagen = serializers.ImageField(required=False)
    monedas = serializers.IntegerField(required=False)
    puntos = serializers.IntegerField(required=False)
    tipoReciclador = serializers.CharField(required=False)
 
    class Meta:
        model = User
        fields = ('id', 'username', 'password','alias','tipoReciclador','correo','imagen','monedas','puntos','nivelActual')
    def create(self, validated_data, instance=None):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        user.save()
        Reciclador.objects.update_or_create(user=user,**validated_data)
        reciclador = Reciclador.objects.get(user=user)
        return reciclador

class TipoRecicladorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoReciclador
        fields = ('nombre','id')

class TipoUsoSerializer(serializers.ModelSerializer):
    class Meta:
            model = TipoUso
            fields = ('id','nombre','descripcion','url','imagen')

class CanecaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Caneca
            fields = ('id','nombre','descripcion','url','imagen','tipoUso')

class ResiduoSerializer(serializers.ModelSerializer):
    class Meta:
            model = Residuo
            fields = ('id','nombre','descripcion','url','imagen','caneca')

class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Partida
            fields = ('id','reciclador','puntaje','niveldesbloqueado','fecha')

