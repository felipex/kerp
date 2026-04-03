from django.urls import path
from crm.views import IndexView, CustomerListView, CustomerCreateView, CustomerUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<uuid:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
]

