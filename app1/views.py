from django.shortcuts import render
from django.http import HttpResponse


def first(request):
    return HttpResponse('<h1><marquee>this is my first view<marquee><h1>')

def second(request):
    return HttpResponse('<h2>congratulations</h2>')