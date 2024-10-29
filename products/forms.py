from django import forms
from .models import Product

# Estos formularios me permiten ejecutar acciones cuando el usuario haga SUBMIT, podemos
# crear un metodo que se llame save() para guardar esto en el modelo

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label='Nombre')
    description = forms.CharField(max_length=300, label='Descripcion')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')
    available = forms.BooleanField(initial=True, label='Disponibilidad', required=False)
    photo = forms.ImageField(label='Foto', required=False)


    # cleaned_data[] es un diccionario que nos permite traer la informacion limpia del formulario
    # cuando el usuario hace el request.
       
    def save(self):
        # Crea un registra en la base de datos
        Product.objects.create(
            name = self.cleaned_data['name'],
            description = self.cleaned_data['description'],
            price = self.cleaned_data['price'],
            available = self.cleaned_data['available'],
            photo = self.cleaned_data['photo'],
        )
