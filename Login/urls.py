from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    
    path("employee_login/", views.employee_login, name = "employee_login"),
    
    path("patient_login/", views.patient_login, name ="patient_login")]


