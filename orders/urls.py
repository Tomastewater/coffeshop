from django.urls import path
from .views import MyOrderView, CreateOrderProductView, OrderListAPI

urlpatterns = [
    path('mi-orden/', MyOrderView.as_view(), name= "my_order"),
    path('agregar-orden', CreateOrderProductView.as_view(), name='add_product'),
    path('api/', OrderListAPI.as_view(), name='order_list_api'),
]