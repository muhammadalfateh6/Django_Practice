from django.test import TestCase
from .models import Menu_lemon
from datetime import datetime

# Create your tests here.

class TestMenu(TestCase):

    @classmethod
    def setUp(self):
        self.indata = Menu_lemon.objects.create(name='Daal', 
                                               price=160)

    def test_field(self):
        self.assertIsInstance(self.indata.name, str)
        self.assertIsInstance(self.indata.price, int)