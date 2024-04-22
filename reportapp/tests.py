from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from reportapp.models import Article

class ReportAppViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_report_lost_item_view(self):
        # Test POST request to report a lost item
        data = {
            'name': 'Test Item',
            'brand': 'Test Brand',
            'category': 'Test Category',
            'lostlocation': 'Test Location',
            'lostdate': '2024-04-22',
            'description': 'Test Description',
        }
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('report'), data)
        self.assertEqual(response.status_code, 200)  # Assuming the view returns 200 on success

        # Check if the item is created in the database
        self.assertTrue(Article.objects.filter(name='Test Item').exists())

    def test_report_found_item_view(self):
        # Test POST request to report a found item
        data = {
            'name': 'Test Item',
            'brand': 'Test Brand',
            'category': 'Test Category',
            'foundlocation': 'Test Location',
            'founddate': '2024-04-22',
            'description': 'Test Description',
        }
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('reportfound'), data)
        self.assertEqual(response.status_code, 200)  # Assuming the view returns 200 on success

        # Check if the item is created in the database
        self.assertTrue(Article.objects.filter(name='Test Item').exists())

    def test_view_items_view(self):
        # Test GET request to view items
        response = self.client.get(reverse('viewitems'))
        self.assertEqual(response.status_code, 200)  # Assuming the view returns 200 on success

  
