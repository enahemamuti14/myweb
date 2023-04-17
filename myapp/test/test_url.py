from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import index, send_contact,send_order, product

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_send_contact_url_is_resolved(self):
        url = reverse('send_contact')
        self.assertEquals(resolve(url).func, send_contact)

    def test_send_order_url_is_resolved(self):
        url = reverse('send_order')
        self.assertEquals(resolve(url).func, send_order)

    def test_product_url_is_resolved(self):
        url = reverse('product')
        self.assertEquals(resolve(url).func, product)