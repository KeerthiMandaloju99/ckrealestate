from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Event

class TestEventModel(TestCase):
    def test_Event(self):
        event = Event.objects.create(Event_Name='Friday')

        self.assertEqual(str(event),'Friday' )
        self.assertTrue(isinstance(event, Event))
        
    #Event_Desc = models.TextField(null=False, blank=False)
    #Event_Image = models.ImageField(upload_to='event_images/',null=True, blank=True)
    #Event_Address = models.TextField(null=False, blank=False)
    #Activity_type = models.CharField( max_length=50)

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        #urls
        self.events_url = reverse('events')

    def test_login_user_GET(self):
        # mock the response
        response = self.client.get(self.events_url)

        # write assertions
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events.html')
        self.assertTemplateUsed(response, 'navbar.html')


