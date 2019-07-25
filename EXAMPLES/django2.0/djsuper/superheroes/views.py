from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Superhero

def home(request):
    request.session['color'] = 'red'
    request.session['city'] = 'Baltimore'

    return HttpResponse("Welcome to my SuperHero App!!! Bam!!")

def session1(request):
    request.session['animal'] ='wombat'
    return HttpResponse("Set session variable")

def session2(request):
    animal = request.session['animal']
    data = {
        'animal': animal,
        'session': request.session,
    }
    return render(request, 'sessioninfo.html', data)


def hero(request, hero_name):
    color = request.session['color']

    s = get_object_or_404(Superhero, name=hero_name)
    powers = [p.name for p in s.powers]
    return HttpResponse(
        "{} is really {}".format(s.secret_identity, s.name
                                 )
    )

