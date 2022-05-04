from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from travel.models import Employee, Package, Flight, Train, Bus, guide, complaints, feedbacks, UserInfo


class IndexView(TemplateView):
    template_name = 'admin/' \
                    'index.html'

class AddEmployeeView(TemplateView):
    template_name = 'admin/add_employee.html'
    def post(self , request,*args,**kwargs):
        try:
            name = request.POST['name']
            email= request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            contact = request.POST['contact']
            company = request.POST['company']
            user = User.objects._create_user(username=username,password=password,email=email,first_name=name,is_staff='1',)
            user.save()
            employee = Employee()
            employee.user = user
            employee.contact = contact
            employee.company = company
            employee.save()
            return redirect('/admin')
        except:
            messages = "Enter Another Username"
            return render(request,'admin/index.html',{'messages':messages})


class ViewEmployees(TemplateView):
    template_name = 'admin/view_employees.html'
    def get_context_data(self, **kwargs):
        context = super(ViewEmployees,self).get_context_data(**kwargs)
        employee = Employee.objects.filter(user__is_active='1')
        context['employee'] = employee
        return context

class Viewguide(TemplateView):
    template_name = 'admin/view_guide.html'
    def get_context_data(self, **kwargs):
        context = super(Viewguide,self).get_context_data(**kwargs)
        employee = guide.objects.filter(user__is_active='1')
        context['employee'] = employee
        return context

class add_guide(TemplateView):
    template_name = 'admin/add_guide.html'
    def post(self , request,*args,**kwargs):
        try:
            name = request.POST['name']
            email= request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            contact = request.POST['contact']
            company = request.POST['company']
            user = User.objects._create_user(username=username,password=password,email=email,first_name=name)
            user.save()
            employee = guide()
            employee.user = user
            employee.contact = contact
            employee.company = company
            employee.save()
            return redirect('/admin')
        except:
            messages = "Enter Another Username"
            return render(request,'admin/index.html',{'messages':messages})


class view_feedback(TemplateView):
    template_name = 'admin/view_feedback.html'
    def get_context_data(self, **kwargs):
        context = super(view_feedback,self).get_context_data(**kwargs)
        feed = feedbacks.objects.all()
        context['feed'] = feed
        return context

class view_copmlaint(TemplateView):
    template_name = 'admin/view_complaint.html'
    def get_context_data(self, **kwargs):
        context = super(view_copmlaint,self).get_context_data(**kwargs)
        com = complaints.objects.all()
        context['feed'] = com
        return context

class reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        UserInfo.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class reject2(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        Employee.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])
