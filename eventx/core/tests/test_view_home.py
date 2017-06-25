from django.test import TestCase
from django.shortcuts import resolve_url as r

class HomeTest(TestCase):

    fixtures = ['keynotes.json']

    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)

    def test_speakers(self):
        contents = [
            'Grace Hopper',
            'http://hbn.link/hopper-pic',
            'Alan Turing',
            'http://hbn.link/turing-pic',
            'href="{}"'.format(r('speaker_detail', slug='grace-hopper')),
            'href="{}"'.format(r('speaker_detail', slug='alan-turing')),
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speaker_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)

    def test_talks_list(self):
        expected = 'href="{}"'.format(r('talk_list'))
        self.assertContains(self.response, expected)