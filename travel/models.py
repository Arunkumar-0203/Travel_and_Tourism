
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    address= models.CharField(max_length=50)

class Employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    company = models.CharField(max_length=50)

class guide(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    company = models.CharField(max_length=50)

class Package(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    guides = models.ForeignKey(guide,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    night = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    inclusions = models.CharField(max_length=100)
    exclusions = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    food = models.CharField(max_length=200,null=True)


class Flight(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    dep_place = models.CharField(max_length=100)
    dest_place = models.CharField(max_length=100)
    dep_time = models.CharField(max_length=100)
    arrival_time = models.CharField(max_length=100)
    flight_class = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    seat_map = models.ImageField(upload_to='images/',null=True)
    fare = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    seats = models.CharField(max_length=100,null=True)


class Train(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    dep_place = models.CharField(max_length=100)
    dest_place = models.CharField(max_length=100)
    dep_time = models.CharField(max_length=100)
    arrival_time = models.CharField(max_length=100)
    ac_fare = models.CharField(max_length=100)
    sleeper_fare = models.CharField(max_length=100)
    first_fare = models.CharField(max_length=100)
    second_fare = models.CharField(max_length=100)

class Bus(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    dept_place = models.CharField(max_length=100)
    dest_place = models.CharField(max_length=100)
    dep_time = models.CharField(max_length=100)
    arrival_time = models.CharField(max_length=100)
    seats = models.CharField(max_length=100)
    fare = models.CharField(max_length=100)
    seat_map = models.ImageField(upload_to='images/',null=True)


class FlightBooking(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    seat = models.CharField(max_length=100)

class BusBooking(models.Model):
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    seat = models.CharField(max_length=100)

class TrainBooking(models.Model):
    train = models.ForeignKey(Train,on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    seats = models.CharField(max_length=100)
    train_class = models.CharField(max_length=100)

class PackageBooking(models.Model):
    package = models.ForeignKey(Package,on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    people = models.CharField(max_length=100)

class feedbacks(models.Model):
    user  =models.ForeignKey(UserInfo,on_delete=models.CASCADE,null=True)
    feedback = models.CharField(max_length=100,null=True)

class complaints(models.Model):
    user  =models.ForeignKey(UserInfo,on_delete=models.CASCADE,null=True)
    complaint = models.CharField(max_length=100,null=True)

