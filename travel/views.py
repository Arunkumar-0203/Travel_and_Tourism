from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView

from travel.models import UserInfo


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self,request,*args,**kwargs):
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            if user.is_superuser:
                return redirect('admin/')
            elif user.is_staff:
               return redirect('employee/')
            else:
               return redirect('user/')
        else:
            message = "Invalid Usename or Password"
            return render(request,'login.html',{'message':message},)

class RegisterView(TemplateView):
    template_name = 'register.html'

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        email= request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects._create_user(username=username,password=password,email=email,first_name=name,is_staff='0')
        user.save()
        userinfo = UserInfo()
        userinfo.user = user
        userinfo.address = address
        userinfo.contact = contact
        userinfo.save()
        return redirect('/')
