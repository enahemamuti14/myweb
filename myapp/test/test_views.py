from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import Contact, order

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.Contact = Contact.objects.create(
           nama ="Mutiara",
        )
        self.order = order.objects.create(
           nama ="Mutiara Ratna Enahema",
        )
    def test_index_view(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, self.Contact.nama)
        self.assertContains(response, self.order.nama)