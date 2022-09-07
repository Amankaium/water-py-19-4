from django.shortcuts import render, HttpResponse, redirect
from .models import Client, Order
from .forms import OrderForm, ClientForm
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required


# def clients_list(request):
#     context = {}
#     context["clients"] = Client.objects.all() # model
#     return render(request, 'clients.html', context) # template

@login_required
def order_list(request):
    context = {}
    context["object_list"] = Order.objects.all()
    return render(request, 'order_list.html', context)

class ClientListView(ListView):
    model = Client
    template_name = 'clients.html'


# class OrderListView(ListView):
#     model = Order
#     template_name = 'order_list.html'


def client_detail(request, id):
    try:
        client = Client.objects.get(id=id)
        context = {
            "client": client
        } # SELECT * FROM CLient WHERE id=id;
        return render(request, "client_info.html", context)
    except Client.DoesNotExist:
        return HttpResponse("Не найдено!")


def client_update(request, id):
    context = {}
    client_object = Client.objects.get(id=id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client_object)
        if form.is_valid():
            client_object = form.save()

    context["form"] = ClientForm(instance=client_object)
    return render(request, 'client_update.html', context)


# def create_order(request):
#     if request.method == "POST":
#         data = request.POST
#         order = Order()
#         order.name = data["name"]
#         order.contacts = data["contacts"]
#         order.description = data["description"]
#         order.save()
#         return HttpResponse("Форма обработана")
#     return render(request, 'core/order_form.html')


class CreateOrderView(View):
    def post(self, request):
        data = request.POST
        order = Order()
        order.name = data["name"]
        order.contacts = data["contacts"]
        order.description = data["description"]
        order.save()
        return HttpResponse("Форма обработана")

    def get(self, request):
        return render(request, 'core/order_form.html')


# def order_djangoform(request):
#     context = {}
#     if request.method == "POST":
#         order_form = OrderForm(request.POST)
#         if order_form.is_valid():
#             order_form.save()
#             return HttpResponse("Форма обработана")
#         return HttpResponse("Данные не валидны")
#
#     context["order_form"] = OrderForm()
#     return render(request, 'order_djangoform.html', context)

class CreateOrderDjangoFormView(CreateView):
    model = Order
    template_name = 'order_djangoform.html'
    fields = ["name", "contacts", "description"]
    success_url = "/orders/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["our_number"] = 7
        return context


# def order_list(request):
#     return render(request, 'order_list.html', {"order_list": Order.objects.all()})


# def order_info(request, id):
#     try:
#         return render(
#             request,
#             'order_info.html',
#             {'order_object': Order.objects.get(id=id)}
#         )
#     except Order.DoesNotExist:
#         return HttpResponse("Такой заказ не найден!")
#

class OrderDetailView(DetailView):
    model = Order
    template_name = "order_info.html"


class ClientOrderList(DetailView):
    template_name = 'order_list.html'
    model = Order

    def get(self, request, *args, **kwargs):
        context = {}
        pk = kwargs.get("pk")
        client = Client.objects.get(id=kwargs.get("pk"))
        context["object_list"] = Order.objects.filter(client=client)
        return render(request, self.template_name, context)
