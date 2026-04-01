from core.models import BaseModel
from django.db import models
from core.models import CPFField

class Customer(BaseModel):
    """
    Representa a entidade principal do cliente. 
    Pode ser um Indivíduo (Pessoa) ou uma Empresa (Organização).
    """
    TYPE_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    customer_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='PF')
    
    # Fields for PF
    name = models.CharField(max_length=100, blank=True, null=True)
    cpf = CPFField(blank=True, null=True, verbose_name="CPF")
    
    # Fields for PJ
    company_name = models.CharField(max_length=255, blank=True, null=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True, verbose_name="CNPJ")
    
    # Common Fields
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    
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
