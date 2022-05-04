from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from travel.models import Flight, Train, Bus, Package, FlightBooking, UserInfo, BusBooking, TrainBooking, PackageBooking, \
    feedbacks, complaints


class IndexView(TemplateView):
    template_name = 'user/index.html'


class FlightView(TemplateView):
    template_name = 'user/flight.html'
    def get_context_data(self, **kwargs):
        context = super(FlightView,self).get_context_data(**kwargs)
        flight = Flight.objects.all()
        context['flight'] = flight
        return context

    def post(self, request, *args, **kwargs):
        template = loader.get_template('user/flight.html')
        start = self.request.POST['start_point']
        dest= self.request.POST['dest']
        print(start,dest)
        flight = Flight.objects.filter(dep_place=start,dest_place=dest)
        # return HttpResponse(template.render({"flight": flight}))
        return render(request,'user/flight.html',{'flight': flight})

class TrainView(TemplateView):
    template_name = 'user/train.html'
    def get_context_data(self, **kwargs):
        context = super(TrainView,self).get_context_data(**kwargs)
        train = Train.objects.all()
        context['train'] = train
        return context

    def post(self, request, *args, **kwargs):
        template = loader.get_template('user/train.html')
        start = self.request.POST['start_point']
        dest= self.request.POST['dest']
        print(start,dest)
        train = Train.objects.filter(dep_place=start,dest_place=dest)
        # return HttpResponse(template.render({"train": train}))
        return render(request,'user/train.html',{'train':train})
class BusView(TemplateView):
    template_name = 'user/bus.html'
    def get_context_data(self, **kwargs):
        context = super(BusView,self).get_context_data(**kwargs)
        bus = Bus.objects.all()
        context['bus'] = bus
        return context

    def post(self, request, *args, **kwargs):
        template = loader.get_template('user/bus.html')
        start = self.request.POST['start_point']
        dest= self.request.POST['dest']
        print(start,dest)
        bus = Bus.objects.filter(dept_place=start,dest_place=dest)
        # return HttpResponse(template.render({"bus": bus}))
        return render(request,'user/bus.html',{'bus':bus})


class ToursView(TemplateView):
    template_name = 'user/tours.html'
    def get_context_data(self, **kwargs):
        context = super(ToursView,self).get_context_data(**kwargs)
        package = Package.objects.all()
        # context['users'] = user
        context['package'] = package
        return context


class BookFlightsView(TemplateView):
    template_name = 'user/book_flights.html'
    def get_context_data(self, **kwargs):
        context = super(BookFlightsView,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        flight = Flight.objects.get(pk=id)
        context['flight'] = flight
        return context
    def post(self,request,*args,**kwargs):
        id = request.POST['id']
        date = request.POST['date']
        seat = request.POST['seat']
        flight = Flight.objects.get(pk=id)
        user = UserInfo.objects.get(user=self.request.user)
        f_book = FlightBooking.objects.get(flight=flight,date=date,seat=seat)
        if f_book:
            return render(request,'user/flight.html',{'message':"Seat Already Booked"})
        else:
            flight_book = FlightBooking()
            flight_book.date = date
            flight_book.seat = seat
            flight_book.flight = flight
            flight_book.user = user
            flight_book.save()
            return redirect('/user/payment?fare='+str(flight.fare))

class BookBusView(TemplateView):
    template_name = 'user/book_bus.html'
    def get_context_data(self, **kwargs):
        context = super(BookBusView,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        bus = Bus.objects.get(pk=id)
        context['bus'] = bus
        return context
    def post(self,request,*args,**kwargs):
        id = request.POST['id']
        date = request.POST['date']
        seat = request.POST['seat']
        bus = Bus.objects.get(pk=id)
        user = UserInfo.objects.get(user=self.request.user)
        try:
            b_book = BusBooking.objects.get(bus=bus,date=date,seat=seat)
        except:
            bus_book = BusBooking()
            bus_book.date = date
            bus_book.seat = seat
            bus_book.bus = bus
            bus_book.user = user
            bus_book.save()
            return redirect('/user/payment?fare='+str(bus.fare))
        if b_book:
            return render(request,'user/bus.html',{'message':"Seat Already Booked"})


class BookTrainView(TemplateView):
    template_name = 'user/book_trains.html'
    def get_context_data(self, **kwargs):
        context = super(BookTrainView,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        train = Train.objects.get(pk=id)
        context['train'] = train
        return context
    def post(self,request,*args,**kwargs):
        id = request.POST['id']
        date = request.POST['date']
        seats = request.POST['seats']
        train_class = request.POST['class']
        train = Train.objects.get(pk=id)
        user = UserInfo.objects.get(user=self.request.user)
        train_book = TrainBooking()
        train_book.date = date
        train_book.seats = seats
        train_book.train_class = train_class
        train_book.train = train
        train_book.user = user
        train_book.save()
        if train_class =="A/C Class":
            fare = train.ac_fare
        elif train_class == "First Class:":
            fare = train.first_fare
        elif train_class == "Second Class":
            fare = train.second_fare
        else:
            fare = train.sleeper_fare
        amount = int(seats)*int(fare)
        return redirect('/user/payment?fare='+str(amount))


class BookPackagesView(TemplateView):
    template_name = 'user/book_packages.html'
    def get_context_data(self, **kwargs):
        context = super(BookPackagesView,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        package = Package.objects.get(pk=id)
        context['package'] = package
        return context
    def post(self,request,*args,**kwargs):
        id = request.POST['id']
        date = request.POST['date']
        people = request.POST['people']
        package =Package.objects.get(pk=id)
        user = UserInfo.objects.get(user=self.request.user)
        package_book = PackageBooking()
        package_book.date = date
        package_book.people = people
        package_book.package = package
        package_book.user = user
        package_book.save()
        amount = int(package.amount)* int(people)
        return redirect('/user/payment?fare='+str(amount))


class MyFlightBookings(TemplateView):
    template_name = 'user/my_flight_bookings.html'
    def get_context_data(self, **kwargs):
        context = super(MyFlightBookings,self).get_context_data(**kwargs)
        context['flight_booking'] = FlightBooking.objects.filter(user__user=self.request.user)
        return context

class MyTrainBookings(TemplateView):
    template_name = 'user/my_train_booking.html'
    def get_context_data(self, **kwargs):
        context = super(MyTrainBookings,self).get_context_data(**kwargs)
        context['train_booking'] = TrainBooking.objects.filter(user__user=self.request.user)
        return context

class MyBusBookings(TemplateView):
    template_name = 'user/my_bus_booking.html'
    def get_context_data(self, **kwargs):
        context = super(MyBusBookings,self).get_context_data(**kwargs)
        context['bus_booking'] = BusBooking.objects.filter(user__user=self.request.user)
        return context

class MyPackageBookings(TemplateView):
    template_name = 'user/my_package_booking.html'
    def get_context_data(self, **kwargs):
        context = super(MyPackageBookings,self).get_context_data(**kwargs)
        context['package_booking'] = PackageBooking.objects.filter(user__user=self.request.user)
        return context


class PaymentView(TemplateView):
    template_name = 'user/payment.html'
    def get_context_data(self, **kwargs):
        context = super(PaymentView,self).get_context_data(**kwargs)
        fare = self.request.GET['fare']
        context['fare'] = fare
        return context
    def post(self,request,*args,**kwargs):
        return render(request,'user/index.html',{'message':"Payment Successfull"})

class view_package_details(TemplateView):
    template_name = 'user/view_packagedetails.html'
    def get_context_data(self, **kwargs):
        context = super(view_package_details,self).get_context_data(**kwargs)
        id =self.request.GET['id']
        package = Package.objects.filter(id=id)
        context['package'] = package
        return context

class add_feedback(TemplateView):
    template_name = 'user/feedbacks.html'
    def get_context_data(self, **kwargs):
        context = super(add_feedback,self).get_context_data(**kwargs)
        id=self.request.user.id
        users = UserInfo.objects.get(user_id=id)
        feed = feedbacks.objects.filter(user_id=users.id)
        context['feed'] = feed
        return context
    def post(self,request,*args,**kwargs):
        id=self.request.user.id
        users = UserInfo.objects.get(user_id=id)
        feed = request.POST['feedback']
        f=feedbacks()
        f.user_id=users.id
        f.feedback = feed
        f.save()
        return redirect(request.META['HTTP_REFERER'])

class add_complaint(TemplateView):
    template_name = 'user/complaints.html'
    def get_context_data(self, **kwargs):
        context = super(add_complaint,self).get_context_data(**kwargs)
        id=self.request.user.id
        users = UserInfo.objects.get(user_id=id)
        com = complaints.objects.filter(user_id=users.id)
        context['feed'] = com
        return context
    def post(self,request,*args,**kwargs):
        id=self.request.user.id
        users = UserInfo.objects.get(user_id=id)
        comp = request.POST['complaint']
        f=complaints()
        f.user_id=users.id
        f.complaint = comp
        f.save()
        return redirect(request.META['HTTP_REFERER'])

class remove_feedback(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        feedbacks.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class remove_complaint(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        complaints.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])
