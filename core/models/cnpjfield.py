from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from core.models.validators import validate_cnpj, format_cnpj

class CNPJField(models.CharField):
    description = "Field to store Brazilian CNPJ numbers"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        kwargs['validators'] = [validate_cnpj]
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        value = super().to_python(value)
        if value is None or value == '':
            return value
        
        # Remove formatação (pontos e traços)
        value = ''.join(filter(str.isdigit, value))

        if len(value) != 14:
            raise ValidationError(_('Invalid CNPJ length.'))

        validate_cnpj(value)

        return value

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        # Retorna limpo do banco, ou formatado se preferir
        return value

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is None:
            return value
        # Garante que salva apenas números no banco
        return ''.join(filter(str.isdigit, str(value)))

    def get_cnpj_display(self, value):
        return format_cnpj(value)   
