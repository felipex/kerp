from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_cpf(value):
    """
    Validates a CPF number using the modulo-11 algorithm.
    Accepts formatted (123.456.789-09) or unformatted (12345678909) strings.
    """
    if not value:
        return

    # Remove non-numeric characters
    cpf_number = ''.join(filter(str.isdigit, str(value)))

    if len(cpf_number) != 11:
        raise ValidationError(_('Invalid CPF length.'))

    # Check for sequential digits (e.g., 111.111.111-11)
    if cpf_number == cpf_number[0] * 11:
        raise ValidationError(_('Invalid CPF sequence.'))

    # Calculate first check digit
    sum_9 = sum(int(cpf_number[i]) * (10 - i) for i in range(9))
    remainder_9 = (sum_9 * 10) % 11
    digit_10 = 0 if remainder_9 >= 10 else remainder_9

    if int(cpf_number[9]) != digit_10:
        raise ValidationError(_('Invalid CPF check digit 1.'))

    # Calculate second check digit
    sum_10 = sum(int(cpf_number[i]) * (11 - i) for i in range(10))
    remainder_10 = (sum_10 * 10) % 11
    digit_11 = 0 if remainder_10 >= 10 else remainder_10

    if int(cpf_number[10]) != digit_11:
        raise ValidationError(_('Invalid CPF check digit 2.'))


def format_cpf(value):
    """
    Formats a CPF string as 123.456.789-09.
    """
    if not value:
        return ''
    cpf_number = ''.join(filter(str.isdigit, str(value)))
    if len(cpf_number) != 11:
        return value
    return f"{cpf_number[:3]}.{cpf_number[3:6]}.{cpf_number[6:9]}-{cpf_number[9:]}"



import re

def validate_cnpj(cnpj):
    # 1. Limpeza: remove pontos, barras e traços
    cnpj = re.sub(r'[^0-9]', '', str(cnpj))
    
    # 2. Verifica tamanho e se é uma sequência de números iguais
    if len(cnpj) != 14 or len(set(cnpj)) == 1:
        raise ValidationError(_('Invalid CNPJ length.'))
    
    # 3. Cálculo dos dígitos verificadores
    def check_digit(base, weights):
        soma = 0
        for i in range(len(base)):
            soma += int(base[i]) * weights[i]
        
        remainder = soma % 11
        return 0 if remainder < 2 else 11 - remainder

    # Pesos para o cálculo
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    
    # Primeiro dígito
    dv1 = str(check_digit(cnpj[:12], pesos1))
    
    # Segundo dígito
    dv2 = str(check_digit(cnpj[:12] + dv1, pesos2))
    
    # 4. Verifica se os dígitos calculados conferem
    if cnpj[-2] != dv1:
        raise ValidationError(_('Invalid CNPJ check digit 1.'))
    if cnpj[-1] != dv2:
        raise ValidationError(_('Invalid CNPJ check digit 2.'))


def format_cnpj(value):
    """
    Formats a CNPJ string as 12.345.678/0001-90.
    """
    if not value:
        return ''
    cnpj_number = ''.join(filter(str.isdigit, str(value)))
    if len(cnpj_number) != 14:
        return value
    return f"{cnpj_number[:2]}.{cnpj_number[2:5]}.{cnpj_number[5:8]}/{cnpj_number[8:12]}-{cnpj_number[12:]}"
