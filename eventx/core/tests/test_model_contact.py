from django.core.exceptions import ValidationError
from django.test import TestCase
from eventx.core.models import Speaker, Contact

class ContactModelTest(TestCase):

    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='helder',
            slug='helder-w',
            photo="helder-pc",
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker = self.speaker,
            kind=Contact.EMAIL,
            value='helder@gmail.com'
        )

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='11-99807-0000'
        )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='helder@gmail.com'
        )
        self.assertEqual('helder@gmail.com', str(contact))