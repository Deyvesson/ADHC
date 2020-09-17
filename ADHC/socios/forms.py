from django import forms

from .models import Socio

class SocioForm(forms.ModelForm):

    class Meta:
        model = Socio
        fields = ('socio_numero','socio_rg','socio_cpf','socio_patente','socio_nome', 'socio_email', 'socio_telefone', 'socio_endereco', 'socio_cidade', 'socio_cep', 'socio_estado')