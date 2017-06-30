from datetime import datetime
from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventx.subcriptions.models import Subscription


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name='Helder',
            cpf='12345678910',
            email='helder.midaspro@gmail.com',
            phone='11-9807-4900'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_paid_default_to_false(self):
        self.assertEquals(False, self.obj.paid)

    def test_get_absolute_url(self):
        url = r('subscriptions:detail', self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())