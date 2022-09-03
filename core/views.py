from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from .models import Bottle
from .forms import LoginForm


def contacts(request):
    return render(request, 'core/contacts.html')


def about(request):
    return render(request, 'about.html')


def makers_list(request):
    context = {}
    # SELECT * FROM Bottle
    bottles_list = Bottle.objects.all()
    context["bottles_list"] = bottles_list
    html_page = render(request, 'makers.html', context)
    return html_page


class MyView(View):
    def get(self, request):
        return render(request, "about.html")


class LoginView(View):
    def get(self, request):
        context = {"form": LoginForm()}
        return render(request, 'auth/sign_in.html', context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        user_login = data["username"]
        password = data["password"]
        user = authenticate(request, username=user_login, password=password)
        if user is not None:
            login(request, user)
            return redirect(about)
        else:
            return HttpResponse("Неверный логин или пароль")
