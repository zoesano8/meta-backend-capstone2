from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Menu, MenuItem, Booking
from .serializers import MenuSerializer, MenuItemSerializer, BookingSerializer

class MenuViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.menu = Menu.objects.create(name='Lunch Special', price=20, menu_item_description='Special lunch menu')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def test_get_menu(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

class MenuItemViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.menu_item = MenuItem.objects.create(title='Pasta', price=12.50, inventory=50)
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def test_get_menu_item(self):
        response = self.client.get(reverse('menuitem-list'))
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

class BookingViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.booking = Booking.objects.create(first_name='John Doe', reservation_date='2024-07-04', reservation_slot=12)
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def test_get_booking(self):
        response = self.client.get(reverse('booking-list'))
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

class ProtectedMessageViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def test_protected_message(self):
        response = self.client.get(reverse('message'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "This view is protected"})
