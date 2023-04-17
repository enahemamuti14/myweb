from django.test import TestCase
from myapp.models import Contact, order

class ContactTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Contact.objects.create(nama = "Mutiara Ratna Enahema")

    def test_nama(self):
        contact = Contact.objects.get(id=1)
        expected_nama = f'{contact.nama}'
        self.assertEquals(expected_nama, "Mutiara Ratna Enahema")