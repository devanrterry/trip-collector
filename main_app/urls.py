from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trips/', views.trips_index, name='index'),
    path('trips/<int:trip_id>/', views.trips_detail, name='detail'),
    path('trips/create/', views.TripCreate.as_view(), name='trips_create'),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trips_update'),
    path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trips_delete'),
    path('trips/<int:trip_id>/add_sight/', views.add_sight, name='add_sight'),
    path('trips/<int:trip_id>/assoc_visitor/<int:visitor_id>/', views.assoc_visitor, name='assoc_visitor'),
    path('visitors/', views.VisitorList.as_view(), name='visitors_index'),
    path('visitors/<int:pk>/', views.VisitorDetail.as_view(), name='visitors_detail'),
    path('visitors/create/', views.VisitorCreate.as_view(), name='visitors_create'),
    path('visitors/<int:pk>/update/', views.VisitorUpdate.as_view(), name='visitors_update'),
    path('visitors/<int:pk>/delete/', views.VisitorDelete.as_view(), name='visitors_delete'),
]