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
            name='a language',
            native_name='a native name language',
            iso_639_1='al',
            iso_639_2='alg',
            description='a language is a language.'
        )

    # model testing
    def test_language_model(self):
        self.assertEqual(f'{self.language.name}', 'a language')
        self.assertEqual(f'{self.language.native_name}', 'a native name language')
        self.assertEqual(f'{self.language.iso_639_1}', 'al')
        self.assertEqual(f'{self.language.iso_639_2}', 'alg')
        self.assertEqual(f'{self.language.description}', 'a language is a language.')

    # list view
    def test_language_list_view(self):
        response = self.client.get(reverse('language-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'a language')
        self.assertContains(response, 'a native name language')
        self.assertTemplateUsed(response, 'language/language_list.html')
    
    # detail view
    def test_language_detail_view(self):
        response = self.client.get(self.language.get_absolute_url())
        no_response = self.client.get('/language/9876543210/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'a language')
        self.assertContains(response, 'a native name language')
        self.assertContains(response, 'al')
        self.assertContains(response, 'alg')
        self.assertContains(response, 'a language is a language.')
        self.assertTemplateUsed(response, 'languages/language_detail.html')

