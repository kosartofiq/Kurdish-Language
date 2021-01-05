from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView,AboutPageView


class HomepageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self): 
        self.assertTemplateUsed(self.response, 'home/home.html')

    def test_home_page_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_home_page_url_resolve_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

class AboutpageTest(SimpleTestCase):
    
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self): 
        self.assertTemplateUsed(self.response, 'home/about.html')

    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, 'About')
    
    def test_about_page_url_resolve_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )

"""
class HomePageViewTest(TestCase):  # new
    def setUp(self):
        Post.objects.create(text='this is another test')
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')


class BlogTests(TestCase):
    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )


self.post = Post.objects.create(
    title='A good title',
    body='Nice body content',
    author=self.user,
)


def test_string_representation(self):
    post = Post(title='A sample title')
    self.assertEqual(str(post), post.title)


Chapter
5: Blog
App
117


def test_post_content(self): self.assertEqual(f'{self.post.title}', 'A good title')


self.assertEqual(f'{self.post.author}', 'testuser')
self.assertEqual(f'{self.post.body}', 'Nice body content')


def test_post_list_view(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Nice body content')
    self.assertTemplateUsed(response, 'home.html')


def test_post_detail_view(self):
    response = self.client.get('/post/1/')


no_response = self.client.get('/post/100000/')
self.assertEqual(response.status_code, 200)
self.assertEqual(no_response.status_code, 404)
self.assertContains(response, 'A good title')
self.assertTemplateUsed(response, 'post_detail.html')




/////////

class BlogTests(TestCase):
    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )


self.post = Post.objects.create(
    title='A good title',
    body='Nice body content',
    author=self.user,
)


def test_string_representation(self):
    post = Post(title='A sample title')
    self.assertEqual(str(post), post.title)


def test_get_absolute_url(self):  # new


Chapter
6: Forms
143
self.assertEqual(self.post.get_absolute_url(), '/post/1/')


def test_post_content(self): self.assertEqual(f'{self.post.title}', 'A good title')


self.assertEqual(f'{self.post.author}', 'testuser')
self.assertEqual(f'{self.post.body}', 'Nice body content')


def test_post_list_view(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Nice body content')
    self.assertTemplateUsed(response, 'home.html')


def test_post_detail_view(self):
    response = self.client.get('/post/1/')


no_response = self.client.get('/post/100000/')
self.assertEqual(response.status_code, 200)
self.assertEqual(no_response.status_code, 404)
self.assertContains(response, 'A good title')
self.assertTemplateUsed(response, 'post_detail.html')


def test_post_create_view(self):  # new
    response = self.client.post(reverse('post_new'), {
        'title': 'New title',
        'body': 'New text',
        'author': self.user,
    })


self.assertEqual(response.status_code, 200)
self.assertContains(response, 'New title')

Chapter
6: Forms
144
self.assertContains(response, 'New text')


def test_post_update_view(self):  # new
    response = self.client.post(reverse('post_edit', args='1'), {
        'title': 'Updated title',
        'body': 'Updated text',
    })


self.assertEqual(response.status_code, 302)


def test_post_delete_view(self):  # new response = self.client.post(
    reverse('post_delete', args='1'))
    self.assertEqual(response.status_code, 302)

"""
