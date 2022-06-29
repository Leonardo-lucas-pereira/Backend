from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import celular_valido, cpf_valido, nome_valido, rg_valido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF deve ter 11 dígitos"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"O nome deve ser em string"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve ter 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve ser o modelo: 99 99999-9999"})
        return data