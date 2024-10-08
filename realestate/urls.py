from django.urls import path
from . import views

urlpatterns = [
    path('realestate/', views.index, name='realestate'),
    path('create/', views.create, name='create'),
    path('create/createListing/', views.createListing, name='createListing'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updateListing/<int:id>', views.updateListing, name='updateListing'),
    path('', views.all_listings, name='listings'),
    path('search_listings', views.search_listings, name='search_listings'),
    path('createProperty/', views.create_property, name='createProperty'),
    path('detail_listings', views.detail_listings, name='detail_listings'),
]
