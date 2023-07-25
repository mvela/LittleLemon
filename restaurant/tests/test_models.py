from django.test import TestCase
from ..models import Menu
from decimal import Decimal

class MenuTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="Gelato", price=4.99, inventory=64)
        Menu.objects.create(name="Pizza Slice", price=5.99, inventory=44)
        Menu.objects.create(name="Soda", price=1.59, inventory=33)

    def test_getall(self):
        item = Menu.objects.get(name="Gelato")
        self.assertEqual(float(item.price), 4.99)
        self.assertEqual(float(item.inventory), 64)

        item = Menu.objects.get(name="Pizza Slice")
        self.assertEqual(float(item.price), 5.99)
        self.assertEqual(float(item.inventory), 44)

        item = Menu.objects.get(name="Soda")
        self.assertEqual(float(item.price), 1.59)
        self.assertEqual(float(item.inventory), 33)