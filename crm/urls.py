from django.urls import path
from crm.views import (
    IndexView, 
    CustomerListView, 
    CustomerCreateView, 
    CustomerUpdateView,
    ContactListView,
    ContactCreateView,
    ContactUpdateView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<uuid:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('contacts/', ContactListView.as_view(), name='contact_list'),
    path('contacts/create/', ContactCreateView.as_view(), name='contact_create'),
    path('contacts/<uuid:pk>/update/', ContactUpdateView.as_view(), name='contact_update'),
]
