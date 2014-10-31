from datetime import *
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.test import TestCase
import factory
from slides.forms import UserForm
from slides.models import User, Comment, Attachment, Slide


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda i: 'User%d' % i)
    email = factory.lazy_attribute(lambda o: '%s@gmail.com' % o.username)
    password = factory.PostGenerationMethodCall("set_password", "password")

class ViewTestCase(TestCase):
    def test_register_page(self):
        username = 'new-user'
        data = {
            'username': username,
            'email': 'test@test.com',
            'name': 'new-user',
            'password1': 'test',
            'password2': 'test',
            'image': ''
        }

        response = self.client.post(reverse('register'), data)

        # Check this user was created in the database
        self.assertTrue(User.objects.filter(username=username).exists())

        # Check it's a redirect to the slides index page
        self.assertIsInstance(response, HttpResponseRedirect)

        self.assertTrue(response.get('location').endswith(reverse('slides_home')))




    def test_login_page(self):
        user = UserFactory.create_batch(1)[0]

        data = {
            'username': user.username,
            'password': user.password
        }
        self.client.post(reverse('login'), data)

    def test_edit_account_page(self):
        name = 'new-user'
        data_create = {
            'email': 'test@test.com',
            'name': name,
        }

        response = self.client.post(reverse('edit_profile'), data_create)

        # Check this user was created in the database
        self.assertTrue(User.objects.filter(name=name).exists())

        data_edit = {
            'name':'test'
        }

        response = self.client.post(reverse('edit_profile'), data_edit)

        # Check the changes were made in the database
        self.assertTrue(User.objects.filter(username='test').exists())

        # Check it's a redirect to the profile page
        # self.assertIsInstance(response, HttpResponseRedirect)
        # self.assertTrue(response.get('location').endswith(reverse('profile')))


    def test_create_comment(self):
        pass
    #TODO

    def test_profile_page(self):
        user = UserFactory.create_batch(1)[0]
        user.name = 'test'
        user.save()
        response = self.client.get(reverse('profile'))
        # self.assertInHTML('<p id="editAccount">Welcome, {}</p>'.format(user.name), response.content)
        self.assertInHTML('<p id="lectures">Registration and Profile</p>', response.content)


class FormTestCase(TestCase):
    def test_clean_username_exception(self):
        # Create a player so that this username we're testing is already taken
        User.objects.create_user(username='test-user')

        form = UserForm()
        form.cleaned_data = {'username': 'test-user'}

        with self.assertRaises(ValidationError):
            form.clean_username()

    def test_commentform(self):
        pass
    #TODO

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            image='',
            name='user1',
            username='user1',
            email='u1@test.com',
            first_name='u',
            last_name='1',
            password='1',
        )
        self.slide = Slide.objects.create(
            week_number = 1,
            day = '2_am',
            slide_set = 2,
            slide_number = 1,
            slide_header = 'hello world',
            url = '/week1/1'
        )
        self.comment = Comment.objects.create(
            text='hello',
            user=self.user,
            date=datetime.now(),
            slide = self.slide,
            slide_set= 2,
            slide_number=1,
        )
        self.attachment = Attachment.objects.create(
            file='media/comment_attachment/hello_world.jpg',
            uuid='abcd',
            comment=self.comment,
        )

    def test_user_unicode(self):
        self.assertEqual(self.user.__unicode__(), 'user1')


