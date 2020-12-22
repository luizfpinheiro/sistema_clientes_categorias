from django.forms import model_to_dict
from rest_framework import serializers
from app.models import Categoria, Cliente


class CategoriaSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = model_to_dict(instance)
        data['dt_cadastro'] = instance.dt_cadastro.strftime("%d-%m-%Y")
        
        return data

    class Meta:
        model = Categoria
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        data = model_to_dict(instance)
        
        data['tags'] = [model_to_dict(tag) for tag in instance.tags.all()]
        data['dt_cadastro'] = instance.dt_cadastro.strftime("%d-%m-%Y")
        
        return data

    class Meta:
        model = Cliente
        fields = '__all__'
