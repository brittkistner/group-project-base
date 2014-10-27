from datetime import *
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.test import TestCase
import factory
from slides.forms import UserForm
from slides.models import User, Comment, Attachment


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda i: 'User%d' % i)
    email = factory.lazy_attribute(lambda o: '%s@gmail.com' % o.username)
    password = factory.PostGenerationMethodCall("set_password", "password")
    #how to create an image file?

class ViewTestCase(TestCase):
    # def test_register_page(self):
    #     username = 'new-user'
    #     data = {
    #         'username': username,
    #         'email': 'test@test.com',
    #         'password1': 'test',
    #         'password2': 'test',
    #         # 'image': how to test?
    #     }
    #
    #     response = self.client.post(reverse('register'), data)
    #
    #     print response
    #
    #     # Check this user was created in the database
    #     self.assertTrue(User.objects.filter(username=username).exists())
    #
    #     # Check it's a redirect to the slides index page
    #     self.assertIsInstance(response, HttpResponseRedirect)
    #
    #     # self.assertTrue(response.get('location').endswith(reverse('slides_home')))


    def test_login_page(self):
        user = UserFactory.create_batch(1)[0]

        data = {
            'username': user.username,
            'password': user.password
        }
        self.client.post(reverse('login'), data)

    def create_attachemnt(self):
        pass

    def create_comment(self):
        pass

class FormTestCase(TestCase):
    pass
    # def test_clean_username_exception(self):
    #     # Create a player so that this username we're testing is already taken
    #     User.objects.create_user(username='test-user')
    #
    #     form = UserForm()
    #     form.cleaned_data = {'username': 'test-user'}
    #
    #     with self.assertRaises(ValidationError):
    #         form.clean_username()

class ModelTestCase(TestCase):
    def setup(self):
        self.user1 = User.objects.create(
            image='',
            name='user1',
            username='user1',
            email='u1@test.com',
            first_name='u',
            last_name='1',
            password='1',
        )
        self.comment = Comment.objects.create(
            text='hello',
            user=self.user1,
            date=datetime.now(),
            week_number='1',
            day='5_am',
            slide_set='2',
            slide_number='1',
        )
        # self.attachment = Attachment.objects.create()

    def test_user_uicode(self):
        self.assertEqual(self.user1.__unicode__(), 'user1')

    def test_comment_uicode(self):
        self.assertEqual(self.comment.__unicode__(), 'slide from week1/5_am/#/2/1')