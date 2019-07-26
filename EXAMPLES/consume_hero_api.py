#!/usr/bin/env python
#
from pprint import pprint
import requests


def print_if_ok(response, message):
    print("** {} **".format(message))
    print(response.status_code)
    if response.status_code == requests.codes.OK:
        pprint(response.json())
    else:
        print("Oops:")  # , response.status_code)


hero_response = requests.get('http://127.0.0.1:8000/api/heroes')
print_if_ok(hero_response, 'all heroes')
print('-' * 60)

hero_response = requests.get('http://127.0.0.1:8000/api/heroes/1')
print_if_ok(hero_response, 'hero #1')
print('-' * 60)

hero_response = requests.get('http://127.0.0.1:8000/api/heroes/2')
print_if_ok(hero_response, 'hero #2')

print('=' * 60)
hero_response = requests.get('http://127.0.0.1:8000/api/enemies')
print_if_ok(hero_response, 'all enemies')

print('-' * 60)
hero_response = requests.get('http://127.0.0.1:8000/api/enemies/1')
print_if_ok(hero_response, 'enemy #1')

print('-' * 60)
hero_response = requests.get('http://127.0.0.1:8000/api/enemies/5')
print_if_ok(hero_response, 'enemy #5')
