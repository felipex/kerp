from django import forms

from crm.models import Contact, Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'customer_type', 'name', 'cpf', 'company_name', 'cnpj',
            'email', 'phone', 'website', 'address', 'city', 'state', 'country',
        ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['customer', 'name', 'email', 'phone', 'position', 'is_primary']