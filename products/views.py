from django.views import generic
from .forms import ProductForm
from django.urls import reverse_lazy

class ProductFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product') 
    # Este atributo funciona como una redireccion cuando el submit sea exitoso

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) # Este método generalmente redirige al usuario a la success_url
    

