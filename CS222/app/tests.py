from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# Create your tests here.

class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.user = {
            'username' : "testusername",
            'password' : "testpassword",
            'password2' : 'testpassword',
        }
        self.short_password = {
            'username' : "testusername",
            'password' : "short",
            'password2' : 'short',
        }
        self.same_user = {
            'username' : "testusername",
            'password' : "short",
            'password2' : 'short',
            'username' : "testusername",
            'password' : "short",
            'password2' : 'short',
        }
        self.diff_password = {
            'username' : "testusername",
            'password' : "short",
            'password2' : 'short2',
        }
        self.only_numbers = {
            'username' : "1234567989",
            'password' : "1234567989",
            'password2' : "1234567989",
        }
        self.common_password = {
            'username' : "jalenxing",
            'password' : "hello",
            'password2' : "hello",
        }
        self.null_values = {
            'username' : "",
            'password' : "",
            'password2' : "",
        }
        return super().setUp()

class RegisterTest(BaseTest):
    def test_can_view_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/register.html')

    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user, format = 'text/html')
        self.assertEqual(response.status_code, 200)


    def test_short_password(self):
        form = UserCreationForm(self.short_password)
        self.assertFalse(form.is_valid())

    def test_same_username(self):
        form = UserCreationForm(self.same_user)
        self.assertFalse(form.is_valid())

    def test_diff_password(self):
        form = UserCreationForm(self.diff_password)
        self.assertFalse(form.is_valid())

    def test_only_number(self):
        form = UserCreationForm(self.only_numbers)
        self.assertFalse(form.is_valid())

    def test_only_number(self):
        form = UserCreationForm(self.common_password)
        self.assertFalse(form.is_valid())
    
    def test_null_values(self):
        form = UserCreationForm(self.null_values)
        self.assertFalse(form.is_valid())