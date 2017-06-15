from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Helder', cpf='12345678901', email='helder.midaspro@gmail.com', phone='11-99807-4999')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscrition_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscrition_email_from(self):
        expect = 'contato@eventx.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscrition_email_to(self):
        expect = ['contato@eventx.com.br', 'helder.midaspro@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscrition_email_body(self):
        contents = [
            'Helder',
            '12345678901',
            'helder.midaspro@gmail.com',
            '11-99807-4999'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)