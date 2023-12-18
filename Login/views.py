from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# HOME PAGE
def home(request):
    return render(request, 'base/home.html')


# EMPLOYEE LOGIN
def employee_login(request):
    
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email = email)
        except:
            messages.error(request, "Username does not exist")
    return render(request, 'base/employee_login.html')


def employee_logout(request):
    return redirect('base/home.html')


def register_EmpFrm(request):
    
    if request.method == "POST":
        form = MyUserCreation(request.POST)
        if request.method == "POST":
            form = MyUserCreation(request.POST)
            if form.is_valid():
                user = form.save(commit = False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
    return redirect('base/home.html')

#PATIENT LOGIN
def patient_login(request):
    return render(request, 'base/patient_login.html')

def patient_logout(request):
    return redirect('base/home.html')