from django.urls import path

from travel.admin_views import IndexView,AddEmployeeView,ViewEmployees, add_guide, Viewguide, view_feedback, \
    view_copmlaint, reject, reject2

urlpatterns = [
    path('',IndexView.as_view()),
    path('addemployee',AddEmployeeView.as_view()),
    path('view_employees',ViewEmployees.as_view()),
    path('add_guide',add_guide.as_view()),
    path('Viewguide',Viewguide.as_view()),
    path('view_feedback',view_feedback.as_view()),
    path('view_complaint',view_copmlaint.as_view()),
    path('reject',reject.as_view()),
    path('reject2',reject2.as_view()),


]

def urls():
    return urlpatterns,'admin','admin'