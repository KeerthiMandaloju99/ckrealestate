from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from .models import PropertyListing, Neighborhood, Home_Type, PriceRange

from reports.models import Propery_Search_Log
from datetime import date

from django.db.models import Q


def index(request):
    myProperties = PropertyListing.objects.filter(Is_Featured_Property=False)
    featuredProperty = PropertyListing.objects.filter(Is_Featured_Property=True)
    context = {
        'myProperties': myProperties,
        'featuredProperty': featuredProperty
    }
    template = loader.get_template('realestate/index.html')
    return HttpResponse(template.render(context, request))


def create(request):
    template = loader.get_template('realestate/createListing.html')
    return HttpResponse(template.render({}, request))


def createListing(request):
    data1 = request.POST['Name']
    data2 = request.POST['Desc']
    newProperty = PropertyListing(Name=data1, Desc=data2)
    newProperty.save()
    return HttpResponseRedirect(reverse('realestate'))


def delete(request, id):
    deleteProperty = PropertyListing.objects.get(id=id)
    deleteProperty.delete()
    return HttpResponseRedirect(reverse('realestate'))


def update(request, id):
    updateProperty = PropertyListing.objects.get(id=id)
    context = {
        'property': updateProperty
    }
    template = loader.get_template('realestate/updateListing.html')
    return HttpResponse(template.render(context, request))


def updateListing(request, id):
    name = request.POST['Name']
    desc = request.POST['Desc']
    updateProperty = PropertyListing.objects.get(id=id)
    updateProperty.Name = name
    updateProperty.Desc = desc
    updateProperty.save()
    return HttpResponseRedirect(reverse('realestate'))


class Listing:
    def __init__(self, listingID, listingName, listingDesc, listingAddress, beds, bath, price, neighborhood, homeType,
                 image):
        self.listingID = listingID
        self.listingName = listingName
        self.listingDesc = listingDesc
        self.listingAddress = listingAddress
        self.beds = beds
        self.bath = bath
        self.price = price
        self.neighborhood = neighborhood
        self.homeType = homeType
        self.image = image

    def __str__(self) -> str:
        return f"{self.Listing_Name}"


def all_listings(request):
    template = loader.get_template('realestate/listings.html')
    listings = PropertyListing.objects.all().order_by('-Is_Featured_Property')
    context = {
        'listings': listings,
        'neighborhoods': Neighborhood.objects.all(),
        'homeTypes': Home_Type.objects.all(),
        'priceRanges': PriceRange.objects.all()
    }
    return HttpResponse(template.render(context, request))


def logSearchLog(homeTypeOption, priceRangeOption, neighborhoodOption):
    searchAll = False
    if neighborhoodOption == 'Any' and homeTypeOption == 'Any' and priceRangeOption == 'Any':
        searchAll = True

    search_log = Propery_Search_Log(
        Home_Type_Id=None if homeTypeOption == 'Any' else Home_Type.objects.all().get(Home_Type_ID=homeTypeOption),
        Price_Range_ID=None if priceRangeOption == 'Any' else PriceRange.objects.all().get(
            Price_Range_ID=priceRangeOption),
        Neighborhood_ID=None if neighborhoodOption == 'Any' else Neighborhood.objects.all().get(
            Neighborhood_ID=neighborhoodOption),
        Visitor_Search_Date=date.today())

    if not searchAll:
        search_log.save()


def search_listings(request):
    neighborhoodOption = request.GET.get('neighborhoodOption')
    homeTypeOption = request.GET.get('homeTypeOption')
    priceRangeOption = request.GET.get('priceRangeOption')
    listings = PropertyListing.objects.all().order_by('-Is_Featured_Property')

    if neighborhoodOption != 'Any':
        listings = listings.filter(Listing_Neighborhood=neighborhoodOption)

    if homeTypeOption != 'Any':
        listings = listings.filter(Listing_Home_Type=homeTypeOption)

    if priceRangeOption != 'Any':
        priceRange = PriceRange.objects.get(pk=priceRangeOption).Price_Range
        if priceRangeOption != 'Any':
            listings = listings.filter(Q(Price__gt=priceRange.split("-")[0]) & Q(Price__lt=priceRange.split("-")[1]))

    logSearchLog(homeTypeOption, priceRangeOption, neighborhoodOption)

    template = loader.get_template('realestate/listings.html')
    context = {
        'listings': listings,
        'neighborhoods': Neighborhood.objects.all(),
        'homeTypes': Home_Type.objects.all(),
        'priceRanges': PriceRange.objects.all()
    }
    return HttpResponse(template.render(context, request))

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import PropertyListing

def create_property(request):
    if request.method == 'POST':
        data1 = request.POST.get('Name', '')
        data2 = request.POST.get('Desc', '')
        new_property = PropertyListing(Name=data1, Desc=data2)
        new_property.save()
        return HttpResponseRedirect(reverse('realestate:index'))
    return render(request, 'realestate/propertyCreation.html')



def detail_listings(request):
    id = request.GET.get('id')
    print('id', id)
    listing = PropertyListing.objects.get(pk=id)

    template = loader.get_template('realestate/detail.html')
    context = {
        'listing': listing
    }
    return HttpResponse(template.render(context, request))
