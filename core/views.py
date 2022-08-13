from django.shortcuts import render, HttpResponse
# core/views.py
from .models import Bottle


def contacts(request):
    response = HttpResponse("<h1>Тел.: 348759283745234</h1>")
    return response


def about(request):
    return render(request, 'about.html')


def makers_list(request):
    context = {}
    # SELECT * FROM Bottle
    bottles_list = Bottle.objects.all()
    context["bottles_list"] = bottles_list
    html_page = render(request, 'makers.html', context)
    return html_page
