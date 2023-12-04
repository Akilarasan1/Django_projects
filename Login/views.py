from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def employee_login(request):
    return render(request, 'base/employee_login.html')

def patient_login(request):
    return render(request, 'base/patient_login.html')
