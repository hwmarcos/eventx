from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventx.subcriptions.models import Subscription


class SubscriptionDetailGet(TestCase):

    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Helder Willian',
            email='helder.midaspro@gmail.com',
            cpf='12345678910',
            phone='(11)99807-4900'
        )
        self.resp = self.client.get(r('subscriptions:detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.email, self.obj.cpf, self.obj.phone)
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)

class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('subscriptions:detail', 0))
        self.assertEqual(404, resp.status_code)