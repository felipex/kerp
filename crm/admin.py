from django.contrib import admin
from crm.models import Customer, Contact

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer_type', 'email', 'phone')
    list_filter = ('customer_type',)
    search_fields = ('name', 'email', 'phone')
    ordering = ('name',)
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    ordering = ('name',)
    

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Contact, ContactAdmin)
    