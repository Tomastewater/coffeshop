from django.test import TestCase
from django.urls import reverse
from .models import Product
from django.contrib.auth import get_user_model

# Crear clases de prueba para los modelos de la aplicacion

class ProductListViewTests(TestCase): #TestCase contiene varias funciones que nos permiten hacer pruebas unitarias
    
    def test_should_return_200(self):
        url = reverse('list_product')
        response = self.client.get(url) #response es un objeto que contiene la respuesta del servidor y client es un atributo que nos permite hacer peticiones al servidor
        # breakpoint() # breakpoint es una funcion que nos permite detener la ejecucion del programa y nos permite inspeccionar el codigo
        self.assertEqual(response.status_code, 200) # assertEqual es una funcion que compara dos valores y si son iguales la prueba pasa, status_code es un atributo que contiene el codigo de estado de la respuesta

    def test_should_return_200_with_products(self):
        url = reverse('list_product')
        Product.objects.create(
            name ="test",
            description="test description",
            price="5",
            available=True
        )
        response = self.client.get(url) 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), 1) # context es un atributo que contiene el contexto de la respuesta, en este caso el contexto es un diccionario que contiene la lista de productos

    def test_should_return_200_with_no_products(self):
        url = reverse('list_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), 0)

