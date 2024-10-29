from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import authenticate, login as auth_login , logout as lg
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from .forms import *

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    # usr = get_list_or_404(User)
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Both E-mail and Password are required')
            return redirect('/login/')
            
        usr=authenticate(request, username=username, password=password)
        print(usr)

        if usr is None:
            messages.error(request, 'Wrong credentials')
            return redirect('/login/')
        else:
            auth_login(request, usr)
            return redirect('/')
    return render(request, 'login.html')
            

def register(request):
    if request.method == 'POST':
        nm = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        r_password = request.POST.get('r_password')
        if User.objects.filter(username=nm).exists():
            messages.error(request, 'Username is taken.')
            return redirect('/register/')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is taken.')
            return redirect('/register/')
        if password != r_password:
            messages.error(request, 'Passwords do not match.')
        else:
            print(password)
            regi = User.objects.create_user(username=nm, email=email, password=password)
            regi.save()
            messages.success(request, 'Registration successful.')
            return redirect('/login/')
        
    return render(request, 'register.html')

def Logout(request):
    lg(request)
    return redirect('/')

# def loan_app(request,id):
#     if request.method == 'POST':
#         fm = LoanForm(request.POST)
#         taken_from = fm.cleaned_data['taken_from']
#         amount = fm.cleaned_data['amount']
#         requested_by = get_list_or_404(User, id=id)

#     else:
#         fm = LoanForm()
#     return render(request, 'loan.html',{'form':fm})
