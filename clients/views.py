from django.shortcuts import render, HttpResponse
from .models import Client

# Read
def clients_list(request):
    context = {}
    context["clients"] = Client.objects.all()
    return render(request, 'clients.html', context)


def client_detail(request, id):
    context = {
        "client": Client.objects.get(id=id)
    } # SELECT * FROM CLient WHERE id=id;
    return render(request, "client_info.html", context)


def create_order(request):
    return render(request, 'core/order_form.html')


def order_form_view(request):
    print(request.POST)
    return HttpResponse("Форма обработана")