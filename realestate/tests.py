from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Neighborhood, Home_Type, PropertyListing, PropertyImage

class TestHomeTypeModel(TestCase):
    def test_Home_type(self):
        hometype = Home_Type.objects.create(Home_Type_Name='2 Story')

        self.assertEqual(str(hometype),'2 Story' )
        self.assertTrue(isinstance(hometype, Home_Type))

class TestNeighborhoodModel(TestCase):
    def test_Neighborhood(self):
        neighborhood = Neighborhood.objects.create(Neighborhood_Name='Test Neighborhood')

        self.assertEqual(str(neighborhood),'Test Neighborhood' )
        self.assertTrue(isinstance(neighborhood, Neighborhood))

class TestPropertyListingModel(TestCase):
    def test_PropertyListing(self):
        neighborhood = Neighborhood.objects.create(Neighborhood_Name='Test Neighborhood')
        hometype = Home_Type.objects.create(Home_Type_Name='2 Story')
        property_listing = PropertyListing.objects.create(
            Listing_Name='Test House', Beds ='4',
            Bath = '2.5',
            Listing_Neighborhood = neighborhood,
            Listing_Home_Type = hometype
            )

        self.assertEqual(str(property_listing),'Test House' )

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        #urls
        self.realestate_url = reverse('realestate')

    def test_login_user_GET(self):
        # mock the response
        response = self.client.get(self.realestate_url)

        # write assertions
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'realestate/index.html')
        self.assertTemplateUsed(response, 'navbar.html')

