from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from .models import Receta


# Create your views here.

class RecetaListView(ListView):
    model = Receta
    context_object_name = 'listado_recetas'
    template_name = 'web/recetas_listado.html'

class RecetaCreateView(CreateView):
    model = Receta
    template_name = 'web/receta_crear.html'
    success_url = '/'
    fields = ['Nombre', 'Imagen', 'Descripcion', 'Ingredientes', 'Preparacion']

    def get_context_data(self, **kwargs):
        context = super(RecetaCreateView, self).get_context_data(**kwargs) # get the default context data
        context['listado_recetas'] = Receta.objects.all() # add extra field to the context
        return context

class RecetaDetailView(DetailView):
    model = Receta
    template_name = 'web/receta_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(RecetaDetailView, self).get_context_data(**kwargs) # get the default context data
        context['listado_recetas'] = Receta.objects.all() # add extra field to the context
        return context


class RecetaUpdateView(UpdateView):
    model = Receta
    template_name = 'web/receta_modificar.html'
    fields = ['Nombre', 'Imagen', 'Descripcion', 'Ingredientes', 'Preparacion']

    def get_success_url(self):
        return reverse('receta_detalle', kwargs={'pk': self.object.pk})
    def get_context_data(self, **kwargs):
        context = super(RecetaUpdateView, self).get_context_data(**kwargs) # get the default context data
        context['listado_recetas'] = Receta.objects.all() # add extra field to the context
        return context

class RecetaDeleteView(DeleteView):
    model = Receta
    template_name = 'web/receta_borrar.html'
    success_url = reverse_lazy('recetas_listado')

    def get_context_data(self, **kwargs):
        context = super(RecetaDeleteView, self).get_context_data(**kwargs) # get the default context data
        context['listado_recetas'] = Receta.objects.all() # add extra field to the context
        return context