from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.DispositivoListView.as_view(), name='listar'),
    path('crear', views.DispositivoCreateView.as_view(), name='crear'),
    path('actualizar/<int:pk>/', views.DispositivoUpdateView.as_view(), name='actualizar'),
    path('eliminar/<int:pk>/', views.DispositivoDeleteView.as_view(), name='eliminar'),
    path('detalle/<int:pk>/', views.DispositivoDetailView.as_view(), name='detalle'),

    path('tipo/listar/', views.TipoDeDispositivoListView.as_view(), name='tipo-listar'),
    path('tipo/crear/', views.TipoDeDispositivoCreateView.as_view(), name='tipo-crear'),
    path('tipo/detalle/<int:pk>/', views.TipoDeDispositivoDetailView.as_view(), name='tipo-detalle'),
    path('tipo/actualizar/<int:pk>/', views.TipoDeDispositivoUpdateView.as_view(), name='tipo-actualizar'),
    path('tipo/eliminar/<int:pk>/', views.TipoDeDispositivoDeleteView.as_view(), name='tipo-eliminar'),
]
