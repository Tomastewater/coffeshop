from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class MyOrderViewTests(TestCase):

    def test_no_logged_should_redirect(self):
        url = reverse('my_order')
        response = self.client.get(url)
        self.assertEqual(response.status_code,302) # 302 is the status code for redirection
        self.assertEqual(response.url,'/usuarios/login/?next=/ordenes/mi-orden/')

    def test_logged_should_redirect(self):
        url = reverse('my_order')
        user = get_user_model().objects.create_user(username='test')
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200) # 200 is the status code for success, 
        
