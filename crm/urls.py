from django.urls import path
from crm.views import CustomerListView, CustomerCreateView

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
]

