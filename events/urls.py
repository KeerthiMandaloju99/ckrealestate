from django.urls import path
from . import views

urlpatterns = [
    path('',views.events_all, name='events'),
    path('events_all', views.events_all, name='events'),
    path('sort_events/<str:activityOption>', views.sort_events, name='sort_events'),
]
