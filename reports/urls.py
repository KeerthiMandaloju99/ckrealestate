from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.generate_report, name='reports'),
]
