from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(req):
    return render(req, 'generator/home.html')


def password(req):
    length = int(req.GET.get('length', 12))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if req.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if req.GET.get('special'):
        characters.extend('!@#$%^&*()')
    if req.GET.get('numbers'):
        characters.extend('1234567890')
    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)
    return render(req, 'generator/password.html', {'password': the_password})
