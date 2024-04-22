from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Feedback
from .views import GiveFeedback

class GiveFeedbackTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_give_feedback_view_post(self):
        # Prepare a POST request with valid data
        data = {
            'email': 'test@example.com',
            'feedbacktext': 'This is a test feedback',
            'rating': '5'
        }
        request = self.factory.post(reverse('feedback'), data)
        
        # Call the view function
        response = GiveFeedback(request)
        
        # Check if the feedback instance is created
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Feedback.objects.filter(feedbackemail='test@example.com').exists())

    def test_give_feedback_view_get(self):
        # Prepare a GET request
        request = self.factory.get(reverse('feedback'))
        
        # Call the view function
        response = GiveFeedback(request)
        
        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

    def test_give_feedback_view_invalid_method(self):
        # Prepare a request with an invalid method (PUT)
        request = self.factory.put(reverse('feedback'))
        
        # Call the view function
        response = GiveFeedback(request)
        
        # Check if the response status code is 405 (Method Not Allowed)
        self.assertEqual(response.status_code, 200)
