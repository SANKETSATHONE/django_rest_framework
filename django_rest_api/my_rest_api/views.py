# Create your views here.
from rest_framework.authentication import BasicAuthentication
from rest_framework.mixins import DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from my_rest_api.models import Animal, Owner
from my_rest_api.serializer import AnimalSerializer, OwnerSerializer
from rest_framework import mixins
from rest_framework.generics import GenericAPIView


class AnimalViewSets(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin, mixins.UpdateModelMixin):

    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class AnimalViewSetslist(GenericAPIView,mixins.ListModelMixin):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class AnimalDestroy(GenericAPIView,DestroyModelMixin):
    queryset=Animal.objects.all()
    serializer_class = AnimalSerializer

    def delete(self,request, *args , **kwargs):
        return self.destroy(request, *args, **kwargs)


class OwnerViewSet(ReadOnlyModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

