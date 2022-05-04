from django.shortcuts import render
from django.views.generic import TemplateView, View
from travel.models import Bus, Train, Flight, Package, Employee, FlightBooking, TrainBooking, BusBooking, PackageBooking, \
    guide


class IndexView(TemplateView):
    template_name = 'employee/index.html'



class AddPackages(TemplateView):
    template_name = 'employee/add_packages.html'
    def get_context_data(self, **kwargs):
        context = super(AddPackages,self).get_context_data(**kwargs)
        Guide = guide.objects.all()
        context['Guide'] = Guide
        return context
    def post(self,request,*args,**kwargs):
        employee = Employee.objects.get(user=self.request.user)
        package = Package()
        package.type = request.POST['type']
        package.name= request.POST['name']
        package.day = request.POST['day']
        package.night = request.POST['night']
        package.image = request.FILES['image']
        package.inclusions= request.POST['inclusions']
        package.exclusions = request.POST['exclusions']
        package.amount = request.POST['amount']
        package.details = request.POST['details']
        package.food = request.POST['food']
        package.guides_id = request.POST['guides']
        package.employee = employee
        package.save()
        return render(request,'employee/index.html',{'message':"Package Added"})


class AddFlights(TemplateView):
    template_name = 'employee/add_flight.html'
    def post(self,request,*args,**kwargs):
        employee = Employee.objects.get(user=self.request.user)
        flight = Flight()
        flight.type = request.POST['type']
        flight.company= request.POST['company']
        flight.dep_place = request.POST['dep_place']
        flight.dest_place = request.POST['dest_place']
        flight.dep_time = request.POST['dep_time']
        flight.arrival_time = request.POST['arrival_time']
        flight.flight_class = request.POST['flight_class']
        flight.fare = request.POST['fare']
        flight.image= request.FILES['image']
        flight.seat_map= request.FILES['seat_map']
        flight.details = request.POST['details']
        flight.seats = request.POST['seats']
        flight.employee = employee
        flight.save()
        return render(request,'employee/index.html',{'message':"Flight Added"})


class AddBus(TemplateView):
    template_name = 'employee/add_bus.html'
    def post(self,request,*args,**kwargs):
        employee = Employee.objects.get(user=self.request.user)
        bus = Bus()
        bus.name = request.POST['name']
        bus.company= request.POST['company']
        bus.dept_place = request.POST['dep_place']
        bus.dest_place = request.POST['dest_place']
        bus.dep_time = request.POST['dep_time']
        bus.arrival_time = request.POST['arrival_time']
        bus.seats = request.POST['seats']
        bus.fare = request.POST['fare']
        bus.employee = employee
        bus.seat_map= request.FILES['seat_map']
        bus.save()
        return render(request,'employee/index.html',{'message':"Bus Added"})

class AddTrain(TemplateView):
    template_name = 'employee/add_train.html'
    def post(self,request,*args,**kwargs):
        employee = Employee.objects.get(user=self.request.user)
        train = Train()
        train.type = request.POST['type']
        train.name= request.POST['name']
        train.dep_place = request.POST['dep_place']
        train.dest_place = request.POST['dest_place']
        train.dep_time = request.POST['dep_time']
        train.arrival_time = request.POST['arrival_time']
        train.ac_fare = request.POST['ac_fare']
        train.sleeper_fare = request.POST['sleeper_fare']
        train.first_fare= request.POST['first_fare']
        train.second_fare = request.POST['second_fare']
        train.employee = employee
        train.save()
        return render(request,'employee/index.html',{'message':"Train Added"})

class ViewPackages(TemplateView):
    template_name = 'employee/view_packages.html'
    def get_context_data(self, **kwargs):
        context = super(ViewPackages,self).get_context_data(**kwargs)
        package = Package.objects.all()
        # context['users'] = user
        context['package'] = package
        return context



class ViewFlight(TemplateView):
    template_name = 'employee/view_flights.html'
    def get_context_data(self, **kwargs):
        context = super(ViewFlight,self).get_context_data(**kwargs)
        flight = Flight.objects.all()
        context['flight'] = flight
        return context

class ViewTrain(TemplateView):
    template_name = 'employee/view_trains.html'
    def get_context_data(self, **kwargs):
        context = super(ViewTrain,self).get_context_data(**kwargs)
        train = Train.objects.all()
        context['train'] = train
        return context

class ViewBus(TemplateView):
    template_name = 'employee/view_bus.html'
    def get_context_data(self, **kwargs):
        context = super(ViewBus,self).get_context_data(**kwargs)
        bus = Bus.objects.all()
        context['bus'] = bus
        return context


class MyFlightBookings(TemplateView):
    template_name = 'employee/my_flight_bookings.html'
    def get_context_data(self, **kwargs):
        context = super(MyFlightBookings,self).get_context_data(**kwargs)
        context['flight_booking'] = FlightBooking.objects.filter(flight__employee__user=self.request.user)
        return context

class MyTrainBookings(TemplateView):
    template_name = 'employee/my_train_booking.html'
    def get_context_data(self, **kwargs):
        context = super(MyTrainBookings,self).get_context_data(**kwargs)
        context['train_booking'] = TrainBooking.objects.filter(train__employee__user=self.request.user)
        return context

class MyBusBookings(TemplateView):
    template_name = 'employee/my_bus_booking.html'
    def get_context_data(self, **kwargs):
        context = super(MyBusBookings,self).get_context_data(**kwargs)
        context['bus_booking'] = BusBooking.objects.filter(bus__employee__user=self.request.user)
        return context

class MyPackageBookings(TemplateView):
    template_name = 'employee/my_package_booking.html'
    def get_context_data(self, **kwargs):
        context = super(MyPackageBookings,self).get_context_data(**kwargs)
        context['package_booking'] = PackageBooking.objects.filter(package__employee__user=self.request.user)
        return context

class RemoveFlight(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        flight = Flight.objects.get(pk=id)
        flight.delete()
        return render(request,'employee/index.html',{'message':"Flight Removed"})

class RemoveBus(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        flight = Bus.objects.get(pk=id)
        flight.delete()
        return render(request,'employee/index.html',{'message':"Bus Removed"})

class RemoveTrain(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        flight = Train.objects.get(pk=id)
        flight.delete()
        return render(request,'employee/index.html',{'message':"Train Removed"})

class RemovePackage(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        flight = Package.objects.get(pk=id)
        flight.delete()
        return render(request,'employee/index.html',{'message':"Package Removed"})

class view_package_details(TemplateView):
    template_name = 'employee/view_packagedetails.html'
    def get_context_data(self, **kwargs):
        context = super(view_package_details,self).get_context_data(**kwargs)
        id =self.request.GET['id']
        package = Package.objects.filter(id=id)
        context['package'] = package
        return context