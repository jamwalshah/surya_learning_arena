from django.shortcuts import render
from passengerApp.models import PassengerPatal

# Create your views here.
def view_passengerData(request):
    passengers = PassengerPatal.objects.all()
    passengersDict = {'passengers':passengers}
    return render(request=request, template_name='passengers.html', context=passengersDict)
