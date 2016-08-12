import django_filters
from places.models import Landgericht
from persons.models import Todesart, Beruf

django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


class PersonListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label="Nachname des Verstorbenen")
    vorname = django_filters.CharFilter(lookup_expr='icontains', label="Vorname des Verstorbenen")
    geburtsort__name = django_filters.CharFilter(
        lookup_expr='icontains', label="Geburtsort des Verstorbenen")
    sterbeort__name = django_filters.CharFilter(
        lookup_expr='icontains', label="Sterbeort des Verstorbenen")
    geburtsort__landgericht__name = django_filters.ModelMultipleChoiceFilter(
        queryset=Landgericht.objects.all(), label="Landgericht des Geburtsortes")
    sterbeort__landgericht__name = django_filters.ModelMultipleChoiceFilter(
        queryset=Landgericht.objects.all(), label="Landgericht des Sterbeortes")
    beruf__name = django_filters.ModelMultipleChoiceFilter(
        queryset=Beruf.objects.all(), label="Berufsgruppe des Verstorbenen")
    todesart__name = django_filters.ModelMultipleChoiceFilter(
        queryset=Todesart.objects.all(), label="Todesart")
