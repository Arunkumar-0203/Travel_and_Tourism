from django.urls import path

from travel.user_views import IndexView,BusView,FlightView,ToursView,TrainView, BookFlightsView, PaymentView, \
    BookBusView, BookTrainView, BookPackagesView, MyFlightBookings, MyTrainBookings, MyBusBookings, MyPackageBookings, \
    view_package_details, add_feedback, add_complaint, remove_feedback, remove_complaint

urlpatterns = [
    path('', IndexView.as_view()),
    path('view_flight', FlightView.as_view()),
    path('view_train', TrainView.as_view()),
    path('view_bus', BusView.as_view()),
    path('view_tours', ToursView.as_view()),
    path('book_flights', BookFlightsView.as_view()),
    path('book_bus', BookBusView.as_view()),
    path('book_train', BookTrainView.as_view()),
    path('book_packages', BookPackagesView.as_view()),
    path('payment', PaymentView.as_view()),
    path('my_flight_bookings', MyFlightBookings.as_view()),
    path('my_train_bookings', MyTrainBookings.as_view()),
    path('my_bus_bookings', MyBusBookings.as_view()),
    path('my_package_bookings', MyPackageBookings.as_view()),
    path('view_package_details',view_package_details.as_view()),
    path('add_feedback',add_feedback.as_view()),
    path('add_complaint',add_complaint.as_view()),
    path('remove_feedback',remove_feedback.as_view()),
    path('remove_complaint',remove_complaint.as_view())
]

def urls():
    return urlpatterns,'user','user'
