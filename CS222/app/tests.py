from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your tests here.

class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user = {
            'username' : "testusername",
            'password' : "testpassword",
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

        self.login_user = {
            'username' : "jaden123",
            'email' : "jalen.xing@gmail.com",
            'password' : "mynameisjalen12",
            'password2' : "mynameisjalen12"
        }

        self.invalid_email = {
            "username" : "jaden230494",
            'password' : "mynameisjalen123" 

        }

        self.null_password= {
            'username' : "jaden12345",
            'password' : "",
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
    
class LoginTest(BaseTest):
    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/login.html')
    
    def test_login_success(self):
        User.objects.create_user(**self.user)
        response = self.client.post('/login/', self.user, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_unverified_user_name(self):
        User.objects.create_user(**self.invalid_email)
        response = self.client.post('/login/', self.invalid_email, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_null_username(self):
        User.objects.create_user(**self.invalid_email)
        response = self.client.post('/login/', self.invalid_email, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_null_password(self):
        User.objects.create_user(**self.null_password)
        response= self.client.post(self.login_url, self.null_password,format='text/html')
        self.assertEqual(response.status_code,401)

