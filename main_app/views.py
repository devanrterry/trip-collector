from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Trip, Visitor
from .forms import SightForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def trips_index(request):
  trips = Trip.objects.all()
  return render(request, 'trips/index.html', { 'trips': trips })

def trips_detail(request, trip_id):
  trip = Trip.objects.get(id=trip_id)
  sight_form = SightForm()
  return render(request, 'trips/detail.html', { 'trip': trip, 'sight_form': sight_form })

def add_sight(request, trip_id):
  form = SightForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_sight = form.save(commit=False)
    new_sight.trip_id = trip_id
    new_sight.save()
  return redirect('detail', trip_id=trip_id)

class TripCreate(CreateView):
  model = Trip
  fields = '__all__'
  success_url = '/trips/'

class TripUpdate(UpdateView):
  model = Trip
  fields = ['city', 'country', 'description', 'duration']

class TripDelete(DeleteView):
  model = Trip
  success_url = '/trips/'

class VisitorList(ListView):
  model = Visitor

class VisitorDetail(DetailView):
  model = Visitor

class VisitorCreate(CreateView):
  model = Visitor
  fields = '__all__'

class VisitorUpdate(UpdateView):
  model = Visitor
  fields = ['name', 'age']

class VisitorDelete(DeleteView):
  model = Visitor
  success_url = '/visitors/'