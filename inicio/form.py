from django import forms

class SugerenciaFormularioBase(forms.Form):
    titulo = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=20)


class CrearSugerenciaFormulario(SugerenciaFormularioBase):
    ...
    
    
class ModificarSugerenciaFormulario(SugerenciaFormularioBase):
    ...


class BuscarSugerenciaFormulario(forms.Form):
    titulo = forms.CharField(max_length=20, required=False)