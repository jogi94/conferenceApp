from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *
from .availability import check_availabilty

# Create your views here.

def roomList(request):
	roomList = Room.objects.all()
	return render(request, 'roomList.html',{'roomList':roomList})

def bookingList(request):
	bookingList = Booking.objects.all()
	return render(request, 'bookingList.html',{'bookingList':bookingList})

def booking(request):
	form = AvailabilityForm()
	return render(request, 'booking.html', {'form':form})

def bookingSubmit(request):
	if request.method == "POST":
		form = AvailabilityForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			room_list = Room.objects.filter(category=data['room'])
			available_room = []
			for room in room_list:
				if check_availabilty(room, data['check_in'],data['check_out']):
					available_room.append(room)
			if len(available_room)>0:
				room = available_room[0]
				booking = Booking.objects.create(
					user = request.user,
					room = room,
					check_in = data['check_in'],
					check_out = data['check_out']
				)
				booking.save()
				return HttpResponse(booking)
			else:
				return HttpResponse('This category of rooms are booked!!')
