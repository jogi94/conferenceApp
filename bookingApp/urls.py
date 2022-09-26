from django.urls import path
from . import views
from django.views.i18n import JavaScriptCatalog

app_name='bookingApp'

urlpatterns = [
	path('',views.booking,name='bookingUrl'),
	path('booking-submit',views.bookingSubmit,name='bookingSubmit'),
	path('roomList',views.roomList,name='roomListUrl'),
	path('bookingList',views.bookingList,name='bookingListUrl'),
	path('jsi18n', JavaScriptCatalog.as_view(), name='js_catlog'),
]
