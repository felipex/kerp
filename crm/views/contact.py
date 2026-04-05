from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from crm.forms import ContactForm, SearchContactForm
from crm.models import Contact


class ContactListView(ListView):
    model = Contact
    form_class = SearchContactForm
    template_name = 'crm/contacts/contact_list.html'
    context_object_name = 'contacts'
        
    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = Contact.objects.all()
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(email__icontains=search) |
                Q(phone__icontains=search) |
                Q(position__icontains=search)
            )

        # Ordering support
        order_by = self.request.GET.get('order_by', 'name')
        queryset = queryset.order_by(order_by)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['current_order'] = self.request.GET.get('order_by', 'name')
        context['view_type'] = self.request.GET.get('view_type', 'table')
        return context


class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'crm/contacts/create_contact.html'
    success_url = reverse_lazy('contact_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'crm/contacts/update_contact.html'
    success_url = reverse_lazy('contact_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
