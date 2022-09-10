import django_filters
from .models import Client


class ClientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="contains")

    class Meta:
        model = Client
        fields = ["name", "is_active"]
