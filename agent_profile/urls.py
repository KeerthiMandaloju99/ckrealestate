from django.urls import path
from . import views

urlpatterns = [
    path('', views.agent_profile_view, name='agent_profile'),
    path('profile/', views.agent_profile_view, name='agent_profile'),
]




