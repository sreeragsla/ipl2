from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1><marquee>Hardhik Pandya is the captain of MI</marquee></h1>')

def vicecaptain(request):
    return HttpResponse('<h1><marquee>Jasprit Bumrah is the ViceCaptain of MI</marquee></h1>')

