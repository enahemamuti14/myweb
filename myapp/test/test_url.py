from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import index, send_contact,send_order, product

class TestUrls(SimpleTestCase):

    def test_urls(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)