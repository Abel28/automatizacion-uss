from django import forms
from .models import Dispositivo, TipoDeDispositivo
import re


class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = "__all__"
        widgets = {
            'mac_adress': forms.TextInput(attrs={'class':'outline-none mt-1 px-3 py-2 rounded-md border border-gray-400 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400 text-black mb-4', 'placeholder':'Ingrese Mac Address, formato: XX:XX:XX:XX:XX:XX'}),
            'nombre': forms.TextInput(attrs={'class':'outline-none mt-1 px-3 py-2 rounded-md border border-gray-400 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400 text-black mb-4', 'placeholder':'Ingrese estado del dispositivo'}),
            'estado': forms.Select(attrs={'class':'outline-none mt-1 px-3 py-2 rounded-md border border-gray-400 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400 text-black mb-4'}),
            'fecha_fabricacion': forms.DateInput(attrs={'class':'outline-none mt-1 px-3 py-2 rounded-md border border-gray-400 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400 text-black mb-4', 'type':'date'}),
            'criticidad_energetica': forms.Select(attrs={'class':'outline-none mt-1 px-3 py-2 rounded-md border border-gray-400 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400 text-black mb-4', 'placeholder': 'Ingrese criticidad energetica'}),
            'consumo_energia': forms.NumberInput(attrs={'class':'outline-none mt-1 px-3 py-2 rounded-md border border-gray-400 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400 text-black mb-4', 'placeholder': 'Ingrese consumo del dispositivo'}),
            'tipo': forms.Select(attrs={'class':'outline-none mt-1 px-3 py-2 rounded-md border border-gray-400 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400 text-black mb-4'})
        }

    def clean_mac_adress(self):
        mac_adress = self.cleaned_data.get('mac_adress')
        mac_regex = r'^([0-9A-Fa-f]{2}[:\-]){5}([0-9A-Fa-f]{2})$'
        
        if not re.match(mac_regex, mac_adress):
            raise forms.ValidationError("El formato de la dirección MAC es inválido. Use XX:XX:XX:XX:XX:XX o XX-XX-XX-XX-XX-XX.")
        return mac_adress

class TipoDeDispositivoForm(forms.ModelForm):
    
    class Meta:
        model = TipoDeDispositivo
        fields = '__all__'

        widgets = {
            'descripcion': forms.TextInput(attrs={'class':'outline-none mt-1 px-3 py-2 rounded-md border border-gray-400 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400 text-black mb-4', 'placeholder':'Ingrese descripcion'})
        }