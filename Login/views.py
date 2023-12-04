from django.shortcuts import render, redirect

# HOME PAGE
def home(request):
    return render(request, 'base/home.html')


# EMPLOYEE LOGIN
def employee_login(request):
    return render(request, 'base/employee_login.html')


def employee_logout(request):
    return redirect('home')


#PATIENT LOGIN
def patient_login(request):
    return render(request, 'base/patient_login.html')

def patient_logout(request):
    return redirect('home')