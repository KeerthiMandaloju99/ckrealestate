from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import context, loader
from .models import Event

# Create your views here.

def events_all(request):
    myEvents = Event.objects.all()
    template = loader.get_template('events/events.html')
    context = {
        'myEvents': myEvents,
    }
    return HttpResponse(template.render(context, request ) )

def sort_events(request, activityOption):
    #activityOption = request.GET.get('activityOption')
    #neighborhoodOption = request.GET.get('neighborhoodOption')
    #homeTypeOption = request.GET.get('homeTypeOption')
    #listings = PropertyListing.objects.filter(Listing_Neighborhood=neighborhoodOption).filter(Listing_Home_Type=homeTypeOption)
    myEvents = Event.objects.filter(Activity_type=activityOption)
    template = loader.get_template('events/events.html')
    context = {
        'myEvents': myEvents,
    }
    return HttpResponse(template.render(context, request ) )