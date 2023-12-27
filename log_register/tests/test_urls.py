from django.test import SimpleTestCase
from django.urls import reverse, resolve
from log_register.views import register_request, login_request, logout_request, test

class TestUrls(SimpleTestCase):
    def test_register_urls_is_resolved(self):
        url = reverse('register_request')
        print(resolve(url))
        self.assertEqual(resolve(url).func, register_request)

    def test_login_urls_is_resolved(self):
        url = reverse('login_request')
        print(resolve(url))
        self.assertEqual(resolve(url).func, login_request)

    def test_logout_urls_is_resolved(self):
        url = reverse('logout_request')
        print(resolve(url))
        self.assertEqual(resolve(url).func, logout_request)

    


#if theres  a class based views
#func.view_class