from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from app1.views import SignupPage

class SignupPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_with_valid_data(self):
        # Prepare valid form data
        data = {
            'username': 'test_user',
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'test@example.com',
            'password1': 'test_password',
            'password2': 'test_password'
        }

        # Submit the signup form
        response = self.client.post(reverse('signup'), data)

        # Check if the user is redirected to the login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

        # Check if the user is created in the database
        self.assertTrue(User.objects.filter(username='test_user').exists())

    def test_signup_with_password_mismatch(self):
        # Prepare form data with mismatched passwords
        data = {
            'username': 'test_user',
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'test@example.com',
            'password1': 'test_password',
            'password2': 'mismatched_password'
        }

        # Submit the signup form
        response = self.client.post(reverse('signup'), data)

        # Check if the user is redirected back to the signup page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

        # Check if the error message is displayed
        self.assertContains(response, 'Your Passwords donot match')

    def test_signup_with_empty_username(self):
        # Prepare form data with an empty username
        data = {
            'username': '',
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'test@example.com',
            'password1': 'test_password',
            'password2': 'test_password'
        }

        # Submit the signup form
        response = self.client.post(reverse('signup'), data)

        # Check if the user is redirected back to the signup page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

        # Check if the error message is displayed
        self.assertContains(response, 'Please enter a username')
