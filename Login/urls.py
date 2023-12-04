from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    
    path("employee_login/", views.employee_login, name = "employee_login"),
    path("employee_logout/", views.employee_logout, name = "employee_logout"),
    
    path("patient_login/", views.patient_login, name ="patient_login"),
    path("patient_logout/", views.patient_logout, name ="patient_logout")
    ]


