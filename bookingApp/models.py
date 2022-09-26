from django.db import models
from django.utils import timezone
from django.conf import settings
import datetime
# Create your models here.


roomCategory = (
		('Contact','Contact'),
		('Sharing','Sharing'),
		('Team','Team'),
)

class Room(models.Model):
	category = models.CharField(max_length=10,choices=roomCategory,null=True,blank=True)
	capacity = models.IntegerField(null=True,blank=True)
	publish = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.category

	class Meta:
		verbose_name_plural = 'Rooms'


class Booking(models.Model):
	user = models.ForeignKey(on_delete=models.CASCADE,default=datetime.datetime(2016,1,1,7,15,12,655838),to=settings.AUTH_USER_MODEL)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	day = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	check_in = models.TimeField(auto_now=False,null=True)
	check_out = models.TimeField(auto_now=False,null=True)
	publish = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.user} has booked {self.room} ,check in time : {self.check_in} & check out time : {self.check_out}'

	class Meta:
		verbose_name_plural = 'Booking'