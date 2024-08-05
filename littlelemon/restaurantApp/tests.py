# tests/test_models.py

from django.test import TestCase
from django.utils import timezone
from datetime import time, date
from .models import *

class BookingModelTest(TestCase):

    def setUp(self):
        self.booking = Booking.objects.create(
            first_name='John Doe',
            date=date.today(),
            time=time(12, 30)
        )

    def test_booking_creation(self):
        self.assertIsInstance(self.booking, Booking)
        self.assertEqual(self.booking.first_name, 'John Doe')
        self.assertEqual(self.booking.date, date.today())
        self.assertEqual(self.booking.time, time(12, 30))

    def test_string_representation(self):
        self.assertEqual(str(self.booking), 'John Doe')

class MenuModelTest(TestCase):

    def setUp(self):
        self.menu = Menu.objects.create(
            name = 'milk',
            price = 13,
            menu_item_description = 'medimu bottle of organic milk'
        )

    def test_booking_creation(self):
        self.assertIsInstance(self.menu, Menu)
        self.assertEqual(self.menu.name, 'milk')
        self.assertEqual(self.menu.price, 13)
        self.assertEqual(self.menu.menu_item_description, 'medimu bottle of organic milk')

    def test_string_representation(self):
        self.assertEqual(str(self.menu), 'milk')