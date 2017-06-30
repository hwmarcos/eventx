from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventx.core.models import Talk, Speaker, Course


class TalkListTest(TestCase):

    def setUp(self):

        t1 = Talk.objects.create(title='Título da Palestra', start='10:00', description='Descrição da palestra')
        t2 = Talk.objects.create(title='Título da Palestra', start='13:00', description='Descrição da palestra')

        c1 = Course.objects.create(title='Título da curso', start='09:00', description='Descrição da curso', slots=20)

        speaker = Speaker.objects.create(
            name='Helder Willian',
            slug='helder-willian',
            website='http://helder.com.br'
        )

        t1.speakers.add(speaker)
        t2.speakers.add(speaker)

        c1.speakers.add(speaker)

        self.resp = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (2, 'Título da Palestra'),
            (1, '10:00'),
            (1, '13:00'),
            (3, '/palestrantes/helder-w/'),
            (3, 'Helder Willian'),
            (2, 'Descrição da palestra'),
            (1, 'Título curso'),
            (1, '09:00'),
            (1, 'Descrição curso'),
        ]

        for count, expected in contents:
                with self.subTest():
                    self.assertContains(self.resp, expected, count)

    def test_context(self):
        variables = ['talk_list']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.resp.context)

class TalkListTest(TestCase):
    def test_get_empty(self):
        response = self.client.get(r('talk_list'))
        self.assertContains(response, 'Ainda não existem palestras de manhã.')
        self.assertContains(response, 'Ainda não existem palestras de tarde.')