from django.shortcuts import render
from django.http import HttpResponse


def tarun(request):
    return HttpResponse('<h1><i>i am good boy</i></h1>')

