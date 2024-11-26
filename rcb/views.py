from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1>King Kohli is the captain of RCB</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>Phil Salt is the vicecaptain of RCB</h1>')
    