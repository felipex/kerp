from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from crm.forms import CustomerForm
from crm.models import Customer


class IndexView(TemplateView):
    template_name = 'crm/index.html'

class CustomerListView(ListView):
    model = Customer
    template_name = 'crm/customers/customer_list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        return Customer.objects.all()


class CustomerCreateView(CreateView):
    form_class = CustomerForm
    template_name = 'crm/customers/create_customer.html'
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'crm/customers/update_customer.html'
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form) 