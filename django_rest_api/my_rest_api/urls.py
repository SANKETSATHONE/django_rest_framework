from django.urls import path, include
from rest_framework.routers import SimpleRouter
from my_rest_api.views import AnimalViewSets, OwnerViewSet, AnimalViewSetslist, AnimalDestroy

animal_router = SimpleRouter()
animal_router.register('animalapi',AnimalViewSets)

owner_router = SimpleRouter()
owner_router.register('ownerapi', OwnerViewSet)

urlpatterns = [
    # path('',include(animal_router.urls)),
    # path('/',include(owner_router.urls))
    path("animalapilist/", AnimalViewSetslist.as_view()),
    path("animalapi/<int:pk>", AnimalViewSets.as_view()),
    path("animalapidel/<int:pk>", AnimalDestroy.as_view(),

]
