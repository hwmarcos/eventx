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

class ContactManagerTest(TestCase):

    def setUp(self):
        s = Speaker.objects.create(
            name = 'Helder',
            slug = 'helder',
            photo = 'http://hbn.link/helder-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='helder@gmail.com')
        s.contact_set.create(kind=Contact.PHONE, value='11-998070000')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['helder@gmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['11-998070000']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

