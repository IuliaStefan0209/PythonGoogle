from django.shortcuts import render

# Create your views here.
# CreateView => adaugare date in formular
# UpdateView => modificare date in formular
# DeleteView => stergere date in DB
# IndexView => informare cu privire la formular
# ListView => informatii de tip lista din DB
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView

from aplicatie2.models import Location


class CreateLocationView(CreateView):
    model = Location
    # fields = '__all__'
    fields = ['city', 'country']
    template_name = 'aplicatie2/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:listare')

class UpdateLocationView(UpdateView):
    model = Location
    # fields = '__all__'
    fields = ['city', 'country']
    template_name = 'aplicatie2/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:listare')

class ListLocationView(ListView):
    model = Location
    template_name = 'aplicatie2/location_index.html'
