from datetime import datetime

from django.test import TestCase

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