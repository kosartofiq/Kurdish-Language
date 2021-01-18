from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Language


class LanguaeTests(TestCase):

    def setUp(self):
        # create user
        self.user = get_user_model().objects.create_user(
            username='user',
            email='user@email.com',
            password='pass1234')

        self.language = Language.objects.create(
            creator=self.user,
            name='English',
            native_name='Englizi',
            iso_639_1='en',
            iso_639_2='eng',
            description='English is a language.'
        )

    # model testing
    def test_language_model(self):
        self.assertEqual(f'{self.language.name}', 'English')
        self.assertEqual(f'{self.language.native_name}', 'Englizi')
        self.assertEqual(f'{self.language.iso_639_1}', 'en')
        self.assertEqual(f'{self.language.iso_639_2}', 'eng')
        self.assertEqual(f'{self.language.description}', 'English is a language.')

    # list view
    def test_language_list_view(self):
        response = self.client.get(reverse('language-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'English')
        self.assertContains(response, 'Englizi')
        self.assertTemplateUsed(response, 'language/language_list.html')

    def test_language_detail_view(self):
        response = self.client.get(self.language.get_absolute_url())
        no_response = self.client.get('/language/9876543210/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Kurdish')
        self.assertContains(response, 'ku')
        self.assertContains(response, 'kur')
        self.assertContains(response, 'kurdish is a language.')
        self.assertTemplateUsed(response, 'languages/language_detail.html')

