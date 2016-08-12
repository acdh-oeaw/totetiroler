from django.shortcuts import render
from django.views import generic
from django.views.generic.detail import DetailView

from .models import Person


class PersonListView(generic.ListView):
    template_name = 'persons/person_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Person.objects.all()


class PersonDetailView(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        current_object = self.object
        return context

# Create your views here.
