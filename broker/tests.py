from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        #urls
        self.login_url = reverse('login')

    def test_login_user_GET(self):
        # mock the response
        response = self.client.get(self.login_url)

        #Assertions on login url working
        self.assertEqual(response.status_code, 200)
        #Assertions on templates, just making sure navbar is on every page....
        self.assertTemplateUsed(response, 'navbar.html')

    def test_bad_login(self):
        response = self.client.post(self.login_url, {"username": "john", "password": "smith"})
        self.assertNotEqual(response.status_code, 200)

    def test_create_user(self):
        # This one does not actually test user, I need to fix to work past redirect
        self.user = User.objects.create_user(username='testuser', password='12345')
        response = self.client.post(self.login_url, {"username": 'testuser', "password": '12345'})
        self.assertEqual(response.status_code, 302)
        #response = self.client.post(self.login_url,{"username": 'testuser', "password": '12345'}, follow=True)
        #print(response.redirect_chain)
               
