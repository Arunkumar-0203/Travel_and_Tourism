"""Travel_and_Tourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from Travel_and_Tourism import settings
from travel import admin_urls,employee_urls,user_urls
from travel.views import IndexView,LoginView,RegisterView

urlpatterns = [
    path('', IndexView.as_view()),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('admin/', admin_urls.urls()),
    path('employee/', employee_urls.urls()),
    path('user/', user_urls.urls(),name='user/'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
