from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .form import OrderProductForm
from .models import Order
from rest_framework.views import APIView
from .serializers import OrderSerializer
from rest_framework.response import Response

class MyOrderView(LoginRequiredMixin, DetailView): # Esta vista funciona con un ID que se le ingresara para que pueda buscar la orden 
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = 'order' # con este atributo le decimos con que contexto queremos acceder a nuestros datos

    def get_object(self, queryset=None):   # Sobreescribimos el metodo para obtener solo los pk/id de las ordenes activas
        return Order.objects.filter(is_active=True, user=self.request.user).first()    # Usamos first() porque sino devolveria una lista de objetos y solo queremos un solo objeto
    
class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = 'orders/create_order_product.html'
    form_class = OrderProductForm
    success_url = reverse_lazy('my_order')

    # Debemos sobreescribir el metodo form_valid para agregarle la logica que queremos antes de que la instancia sea creada y guardada

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            # El producto que se va a agregar ira a una orden existente o se creara una nueva orden por lo tanto usamos el metodo get_or_create() donde decimos que debe estar activa y debe ser del usuario logueado
            is_active = True,
            user = self.request.user
        )
        # ahora debemos asignar la orden a la instancia del formulario y agregar el resto de los atributos del modelo
        form.instance.order = order
        form.instance.quanty = 1
        form.save()
        return super().form_valid(form)
    
class OrderListAPI(APIView):

    authentication_classes = []
    permission_classes = []
    
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)