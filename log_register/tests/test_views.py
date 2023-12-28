import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User



class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.register = reverse('register_request')
        self.login = reverse('login_request')
        self.test = reverse('test')


        
    def test_register_GET(self):
        response = self.client.get(self.register)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_templates/register.html')


    def test_register_POST(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        response = self.client.post(self.register, data=user_data)
        print(response)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login_GET(self):
        response = self.client.get(self.login)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_templates/login.html')


    # def test_login_POST(self):
    #     login_data = {
    #         'username': 'testuser',
    #         'password': 'testpassword123',
    #     }

    #     response = self.client.post(self.login, data=login_data, follow=True)


    #     print(f"Response content: {response.content}")
    #     print(f"User authenticated: {response.wsgi_request.user.is_authenticated}")

    #     self.assertEqual(response.status_code, 200)
    #     self.assertRedirects(response, self.test)



