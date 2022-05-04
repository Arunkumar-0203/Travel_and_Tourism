from django.urls import path

from travel.employee_views import IndexView, AddPackages, AddFlights, AddBus, AddTrain, ViewPackages, ViewFlight, \
    ViewTrain, ViewBus, MyFlightBookings, MyTrainBookings, MyBusBookings, MyPackageBookings, RemoveFlight, RemoveBus, \
    RemoveTrain, RemovePackage, view_package_details

urlpatterns = [
    path('',IndexView.as_view()),
    path('add_packages',AddPackages.as_view()),
    path('add_flights',AddFlights.as_view()),
    path('add_bus',AddBus.as_view()),
    path('add__train',AddTrain.as_view()),
    path('view_packages',ViewPackages.as_view()),
    path('view_flights',ViewFlight.as_view()),
    path('view_trains',ViewTrain.as_view()),
    path('view_bus',ViewBus.as_view()),
    path('my_flight_bookings', MyFlightBookings.as_view()),
    path('my_train_bookings', MyTrainBookings.as_view()),
    path('my_bus_bookings', MyBusBookings.as_view()),
    path('my_package_bookings', MyPackageBookings.as_view()),
    path('remove_flight', RemoveFlight.as_view()),
    path('remove_bus', RemoveBus.as_view()),
    path('remove_train', RemoveTrain.as_view()),
    path('remove_package', RemovePackage.as_view()),
    path('view_package_details',view_package_details.as_view())
]

def urls():
    return urlpatterns,'employee','employee'