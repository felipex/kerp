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



def validate_cnpj(cnpj: str) -> bool:
    if not cnpj:
        raise ValidationError(_('CNPJ is required.'))

    cnpj = ''.join(filter(str.isdigit, str(cnpj)))
    if len(cnpj) != 14:
        raise ValidationError(_('Invalid CNPJ length.'))

    if cnpj == cnpj[0] * 14:
        raise ValidationError(_('Invalid CNPJ sequence.'))

    weigths = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    part = cnpj[:12]

    sum_1 = 0
    for d, w in zip(part, weigths):
        sum_1 += int(d) * w

    remainder_1 = sum_1 % 11
    digit_1 = 0 if remainder_1 < 2 else 11 - remainder_1

    if int(cnpj[12]) != digit_1:
        raise ValidationError(_('Invalid CNPJ check digit 1.'))

    part_2 = cnpj[:13]
    sum_2 = 0
    weigths.insert(0, 6)
    for d, w in zip(part_2, weigths):
        sum_2 += int(d) * w

    remainder_2 = sum_2 % 11
    digit_2 = 0 if remainder_2 < 2 else 11 - remainder_2

    if int(cnpj[13]) != digit_2:
        raise ValidationError(_('Invalid CNPJ check digit 2.'))

    return True    


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
