from django.http import HttpResponse
from django.shortcuts import render


def homepage(request: HttpResponse):
    # return HttpResponse("<h1>Hello world!</h1>")
    return render(request, 'home.html')