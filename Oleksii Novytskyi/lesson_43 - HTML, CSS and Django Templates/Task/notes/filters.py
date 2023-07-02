import django_filters

from .models import Notes


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Notes
        fields = ['categories', 'title', 'reminder']