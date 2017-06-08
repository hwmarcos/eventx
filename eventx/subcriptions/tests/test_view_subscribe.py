from django.core import mail
from django.test import TestCase
from eventx.subcriptions.forms import SubscriptionForm
from eventx.subcriptions.models import Subscription


class SubscribeGet(TestCase):

    def setUp(self):
        self.resp = self.client.get('/inscricao/')


    def test_get(self):
        self.assertEqual(200, self.resp.status_code)


    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):

        tags = (
            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Helder', cpf='12345678901', email='helder.midaspro@gmail.com', phone='11-99807-4999')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscribePostInvalid(TestCase):

    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())

class SubscribeSuccessMessage(TestCase):

    def test_message(self):
        data = dict(name='Helder', cpf='12345678901', email='helder.midaspro@gmail.com', phone='11-99807-4999')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')