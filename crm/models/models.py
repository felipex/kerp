from core.models import BaseModel
from django.db import models
from core.models import CPFField, CNPJField

class Customer(BaseModel):
    """
    Representa a entidade principal do cliente. 
    Pode ser um Indivíduo (Pessoa) ou uma Empresa (Organização).
    """
    TYPE_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    customer_type = models.CharField('Tipo de Cliente', max_length=20, choices=TYPE_CHOICES, default='PF')
    
    # Fields for PF
    name = models.CharField('Nome', max_length=100, blank=True, null=True)
    cpf = CPFField('CPF', blank=True, null=True)
    
    # Fields for PJ
    company_name = models.CharField('Nome da Empresa', max_length=255, blank=True, null=True)
    cnpj = CNPJField('CNPJ', blank=True, null=True)
    
    # Common Fields
    email = models.EmailField('Email')
    phone = models.CharField('Telefone', max_length=20, blank=True)
    website = models.URLField('Website', blank=True)
    address = models.TextField('Endereço', blank=True)
    city = models.CharField('Cidade', max_length=100, blank=True)
    state = models.CharField('Estado', max_length=100, blank=True)
    country = models.CharField('País', max_length=100, blank=True)
    
    class Meta:
        ordering = ['company_name', 'name']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(customer_type='PF', name__isnull=False, cpf__isnull=False) |
                    models.Q(customer_type='PJ', company_name__isnull=False, cnpj__isnull=False)
                ),
                name='check_customer_type',
            ),
        ]
                

    def __str__(self):
        if self.customer_type == 'PJ' and self.company_name:
            return self.company_name
        elif self.name:
            return self.name
        return self.email


class Contact(BaseModel):
    """
    Representa pessoas relacionadas a um Cliente.
    """
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.PROTECT, 
        related_name='contacts'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    position = models.CharField(max_length=100, blank=True, help_text="Job title or relationship")
    is_primary = models.BooleanField(default=False, help_text="Main point of contact")
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f"{self.name} ({self.customer})"
