from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from crm.forms import CustomerForm, SearchCustomerForm
from crm.models import Customer


class CustomerListView(ListView):
    model = Customer
    form_class = SearchCustomerForm
    template_name = 'crm/customers/customer_list.html'
    context_object_name = 'customers'           
        
    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = Customer.objects.all()
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(company_name__icontains=search) |
                Q(email__icontains=search) |
                Q(phone__icontains=search) |
                Q(cpf__icontains=search) |
                Q(cnpj__icontains=search)
            )

        # 1. Pega o parâmetro de ordenação da URL
        order_by = self.request.GET.get('order_by', 'name') # 'nome' é o padrão

        # 2. Ordena o queryset
        queryset = queryset.order_by(order_by)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['current_order'] = self.request.GET.get('order_by', 'name')
        context['view_type'] = self.request.GET.get('view_type', 'table')
        return context



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

