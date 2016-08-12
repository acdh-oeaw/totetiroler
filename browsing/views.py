from django_tables2 import SingleTableView, RequestConfig
from persons.models import Person
from places.models import Place
from .filters import PersonListFilter
from .forms import GenericFilterFormHelper
from .tables import PersonTable


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'
    paginate_by = 25

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class PersonListView(GenericListView):
    model = Person
    table_class = PersonTable
    template_name = 'browsing/person_list_generic.html'
    filter_class = PersonListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        death = set([x.sterbeort.id for x in Person.objects.all()])
        deathplaces = []
        for x in Place.objects.filter(pk__in=death):
            deathplaces.append(x.name)
        context["deathplaces"] = set(deathplaces)
        brith = set([x.geburtsort.id for x in Person.objects.all()])
        brithplaces = []
        for x in Place.objects.filter(pk__in=brith):
            brithplaces.append(x.name)
        context["brithplaces"] = set(brithplaces)
        return context
