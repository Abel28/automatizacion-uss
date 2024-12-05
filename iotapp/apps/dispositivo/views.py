from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Dispositivo, TipoDeDispositivo
from .forms import DispositivoForm, TipoDeDispositivoForm
from django.db.models import Q


class DispositivoListView(ListView):
    model = Dispositivo
    context_object_name = "dispositivos"

    def get_queryset(self):
        queryset = super().get_queryset()

        search_query = self.request.GET.get("search", "")

        if search_query:
            queryset = queryset.filter(
                Q(mac_adress__icontains=search_query) | 
                Q(nombre__icontains=search_query) |
                Q(tipo__descripcion__icontains=search_query)
            )

        return queryset


class DispositivoCreateView(CreateView):
    model = Dispositivo
    success_url = reverse_lazy('dispositivo:listar')
    form_class = DispositivoForm

class DispositivoUpdateView(UpdateView):
    model = Dispositivo
    success_url = reverse_lazy('dispositivo:listar')
    form_class = DispositivoForm

class DispositivoDeleteView(DeleteView):
    model = Dispositivo
    success_url = reverse_lazy('dispositivo:listar')

class DispositivoDetailView(DetailView):
    model = Dispositivo

class TipoDeDispositivoListView(ListView):
    model = TipoDeDispositivo
    context_object_name = "tipos"

class TipoDeDispositivoCreateView(CreateView):
    model = TipoDeDispositivo
    form_class = TipoDeDispositivoForm
    success_url = reverse_lazy('dispositivo:tipo-listar')

class TipoDeDispositivoUpdateView(UpdateView):
    model = TipoDeDispositivo
    form_class = TipoDeDispositivoForm
    success_url = reverse_lazy('dispositivo:tipo-listar')

class TipoDeDispositivoDeleteView(DeleteView):
    model = TipoDeDispositivo
    success_url = reverse_lazy('dispositivo:tipo-listar')

class TipoDeDispositivoDetailView(DetailView):
    model = TipoDeDispositivo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dispositivos"] = self.object.dispositivo_set.all()
        return context

