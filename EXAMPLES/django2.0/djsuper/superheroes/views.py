from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Superhero

def home(request):
    return HttpResponse("Welcome to my SuperHero App!!! Bam!!")

def hero(request, hero_name):
    s = get_object_or_404(Superhero, name=hero_name)
    powers = [p.name for p in s.powers]
    return HttpResponse(
        "{} is really {}".format(s.secret_identity, s.name
                                 )
    )

