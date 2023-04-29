from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger




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
    
    #Render page, provide variables to template
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


#Create view to book a flight
def book(request, flight_id):

    #Check if method=post
    if request.method == "POST":
        
        #Get all flight objects
        flight_obj = Flight.objects.get(pk=flight_id)

        #Get all passenger objects
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))

        #Add passenger to flight
        passenger.flights.add(flight_obj)

        #Redirect back to flight template
        return HttpResponseRedirect(reverse("flight", args=(flight_obj.id,)))
