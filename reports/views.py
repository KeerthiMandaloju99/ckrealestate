from itertools import count

from django.db.models import Count, Q
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from reports.models import Propery_Search_Log
from .models import Neighborhood, Home_Type, PriceRange

from django.utils import timezone


def generate_report(request):
    template = loader.get_template('reports/reports.html')
    context = {
        'homeTypeList': getHomeTypeData(),
        'NeighborhoodTypeList': getNeighborhoodTypeData(),
        'PriceRangeList': getPriceRangeTypeData(),
    }
    return HttpResponse(template.render(context, request))


def getNeighborhoodTypeData():
    today = timezone.now().date()  # Get today's date
    # Calculate the date 30 days ago
    past_30_days = today - timezone.timedelta(days=30)

    NeighborhoodTypeCounts = (Propery_Search_Log.objects.values('Neighborhood_ID').annotate(
        count=Count('Neighborhood_ID')).filter(Visitor_Search_Date__gte=past_30_days,
                                               Visitor_Search_Date__lte=today)
                              .filter(~Q(Neighborhood_ID__isnull=True)))

    neighborhoodTypeList = []
    total_count = sum(item['count'] for item in NeighborhoodTypeCounts)

    for obj in NeighborhoodTypeCounts:
        data = {"NeighborhoodType": Neighborhood.objects.get(pk=obj['Neighborhood_ID']).Neighborhood_Name,
                "Percentage": round((obj['count'] / total_count) * 100, 2)}
        neighborhoodTypeList.append(data)
    return neighborhoodTypeList


def getHomeTypeData():
    today = timezone.now().date()  # Get today's date
    # Calculate the date 30 days ago
    past_30_days = today - timezone.timedelta(days=30)

    homeTypeCounts = (Propery_Search_Log.objects.values('Home_Type_Id').annotate(
        count=Count('Home_Type_Id')).filter(Visitor_Search_Date__gte=past_30_days,
                                            Visitor_Search_Date__lte=today)
                      .filter(~Q(Home_Type_Id__isnull=True)))

    homeTypeList = []
    total_count = sum(item['count'] for item in homeTypeCounts)

    for obj in homeTypeCounts:
        data = {"HomeType": Home_Type.objects.get(pk=obj['Home_Type_Id']).Home_Type_Name,
                "Percentage": round((obj['count'] / total_count) * 100, 2)}
        homeTypeList.append(data)
    return homeTypeList


def getPriceRangeTypeData():
    today = timezone.now().date()  # Get today's date
    # Calculate the date 30 days ago
    past_30_days = today - timezone.timedelta(days=30)

    priceRangeTypeCounts = (Propery_Search_Log.objects.values('Price_Range_ID').annotate(
        count=Count('Price_Range_ID')).filter(Visitor_Search_Date__gte=past_30_days,
                                              Visitor_Search_Date__lte=today)
                            .filter(~Q(Price_Range_ID__isnull=True)))

    PriceRangeTypeList = []
    total_count = sum(item['count'] for item in priceRangeTypeCounts)

    for obj in priceRangeTypeCounts:
        data = {"PriceRangeType": PriceRange.objects.get(pk=obj['Price_Range_ID']).Price_Range,
                "Percentage": round((obj['count'] / total_count) * 100, 2)}
        PriceRangeTypeList.append(data)
    return PriceRangeTypeList
