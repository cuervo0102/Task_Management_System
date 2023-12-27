from django.test import TestCase, Client
from django.urls import reverse
import json



class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.register = reverse('register_request')
        self.login = reverse('login_request')


        
    def test_register_GET(self):
        response = self.client.get(self.register)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_templates/register.html')


    def test_login_GET(self):
        response = self.client.get(self.login)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_templates/login.html')
