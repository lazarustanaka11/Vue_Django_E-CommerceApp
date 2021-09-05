from django.test import SimpleTestCase
from django.urls import reverse, resolve
from order.views import checkout, OrdersList

class TestUrls(SimpleTestCase):

    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_checkout_orders_is_resolved(self):
        url = reverse('orders')
        self.assertEquals(resolve(url).func, OrdersList)
