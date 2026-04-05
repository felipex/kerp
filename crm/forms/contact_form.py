from django import forms
from crm.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['customer', 'name', 'email', 'phone', 'position', 'is_primary']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'is_primary': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class SearchContactForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Buscar',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar'}))
