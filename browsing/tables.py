import django_tables2 as tables
from django_tables2.utils import A
from persons.models import Person


class PersonTable(tables.Table):
    name = tables.LinkColumn('persons:person_detail', args=[A('pk')], verbose_name='Name')
    vorname = tables.Column(verbose_name='Vorname')
    geburtsort = tables.Column(verbose_name='Geburtsort')
    lg = tables.Column(
        accessor='geburtsort.landgericht.name', verbose_name='Landgericht')
    sterbeort = tables.Column(verbose_name='Sterbeort')
    vorname = tables.Column(verbose_name='Vorname')

    class Meta:
        model = Person
        fields = ['name', 'vorname', 'geburtsort', 'lg', 'sterbeort']
        attrs = {"class": "table table-hover table-striped table-condensed"}
        exclude = [
            'id', 'kramer_index', 'alter', 'beruf',
            'todesart_original', 'beruf_original', 'todesart',
            'todesjahr', 'todesmonat', 'todestag', 'todestag_original',
            'anmerkung', 'quelle']
