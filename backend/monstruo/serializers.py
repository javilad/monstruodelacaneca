from rest_framework import serializers
from monstruo.models import *
from django.contrib.auth.models import User

class TipoRecicladorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoReciclador
        fields = ('nombre','id')

class RecicladorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, source="user.username")
    password = serializers.CharField(write_only=True,source="user.password")
    nivelActual = serializers.IntegerField(required=False)
    alias = serializers.CharField(required=False)
    correo = serializers.CharField(required=False)
    imagen = serializers.ImageField(required=False)
    monedas = serializers.IntegerField(required=False)
    puntos = serializers.IntegerField(required=False)
    tipoReciclador = TipoRecicladorSerializer(required=False)

    class Meta:
        model = User
        fields = ('id','username', 'password','alias','tipoReciclador','correo','imagen','monedas','puntos','nivelActual')
     #
    def create(self, validated_data, instance=None):
        
   
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(Reciclador.correo)
        user.save()

        Reciclador.objects.update_or_create(user=user,**validated_data)
        reciclador = Reciclador.objects.get(user=user)
        reciclador.monedas = 1000
        reciclador.alias = user.username
        return reciclador

    def update(self, instance, validated_data):

        instance.puntos = validated_data.get('puntos', instance.puntos)
        return instance


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
    
    reciclador = serializers.PrimaryKeyRelatedField(queryset=Reciclador.objects.all())
    puntaje = serializers.IntegerField(required=False)
    
    class Meta:
            model = Partida
            fields = ('id','reciclador','puntaje','niveldesbloqueado','fecha')

    def create(self, validated_data, instance=None):

        partida = Partida.objects.create(**validated_data)
        reciclador = validated_data.pop('reciclador')
        reciclador.puntos =   reciclador.puntos + partida.puntaje
        reciclador.save()
        return partida


class NivelSerializer(serializers.ModelSerializer):
    caneca1 = CanecaSerializer(many=False)
    caneca2 = CanecaSerializer(many=False)
    caneca3 = CanecaSerializer(many=False)

    class Meta:
            model = Nivel
            fields = ('id','nombre','descripcion', 'caneca1' ,'caneca2','caneca3')
       