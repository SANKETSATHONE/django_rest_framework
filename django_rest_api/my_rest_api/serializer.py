from rest_framework.serializers import ModelSerializer
from my_rest_api.models import Animal, Owner


class AnimalSerializer(ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class OwnerSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'
