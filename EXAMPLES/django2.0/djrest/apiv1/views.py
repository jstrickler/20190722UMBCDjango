from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, get_object_or_404
)
from rest_framework.parsers import JSONParser
from rest_framework import status

from superheroes.models import Superhero, Enemy, Power, City

from .serializers import (
    SuperheroSerializer, PowerSerializer, EnemySerializer, CitySerializer
)

# hero endpoints
@api_view(['GET', 'POST'])
def superheroes(request):
    """
    Get list of heroes or create a new hero

    :param request: incoming request object
    :return: JSON for one hero
    """
    if request.method == 'GET':
        heroes = Superhero.objects.all()
        serialized = SuperheroSerializer(heroes, many=True)
        return Response(serialized.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SuperheroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def superheroes_detail(request, pk=None):
    """
    Get one hero, update a hero, delete a hero

    :param request: incoming request object
    :param pk: primary key of hero record
    :return: JSON for one hero
    """
    hero = get_object_or_404(Superhero, pk=pk)

    if request.method == "GET":
        serialized = SuperheroSerializer(hero)
        return Response(serialized.data)

    if request.method == 'DELETE':
        hero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SuperheroSerializer(hero, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def powers(request):
    powers = Power.objects.all()
    serialized = PowerSerializer(powers, many=True)

    return Response(serialized.data)


@api_view(['GET'])
def powers_detail(request, pk):
    power_obj = get_object_or_404(Power, pk=pk)
    serialized = PowerSerializer(power_obj)

    return Response(serialized.data)


class EnemiesList(ListAPIView):
    queryset = Enemy.objects.all()
    model = Enemy
    serializer_class = EnemySerializer


class EnemiesDetail(RetrieveAPIView):
    queryset = Enemy.objects.all()
    model = Enemy
    serializer_class = EnemySerializer

# city endpoints
