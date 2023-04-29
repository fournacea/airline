from django.shortcuts import render
from .models import Flight


# Create your views here.

#Render Index page, displaying list of flights + information about those flights
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


#Take the flight id and render page with flight info + passengers onbaord flight
def flight(request, flight_id):
    
    #Get the first flight matching the flight id
    flight = Flight.objects.get(pk=flight_id)
    
    #Render page 
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all()
    })