from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.shortcuts import render, redirect
from .models import Confirm, Deposit, User
from django.contrib import messages

# Create your views here.
def home(request):
    print(request.user.username)
    return render(request, "home.html")

def signup(request):
    print(request.user)
    if request.method == 'POST':
        # form = SignUpForm(request.POST)
        # if form.is_valid():
        #     form.save()
            username = request.POST.get('username')
            full_name = request.POST.get('fullname')
            email = request.POST.get('email')
            raw_password = request.POST.get('password')
            user = User.objects.create(username=username, password=raw_password, full_name=full_name, email=email)
            user.set_password(raw_password)
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("main:profile")
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'succesfully logged in as {request.user}')
            return redirect("main:profile")
        else:
            messages.warning(request, "invalid login details, login again!")
            return redirect("main:sign_up")
    return render(request, "login.html")

def profile(request):
    user = request.user
    context = {
        "user": user
    }
    return render(request, "dashboard.html", context)

def edit(request):
    user = request.user
    context = {
        "user": user
    }
    return render(request, "edit_account.html", context)

def deposit2(request):
    user = request.user
    context = {
        "user": user
    }
    if request.method == 'POST':
        name = request.POST.get('fields[1]')
        confirm = Confirm.objects.create(name=name)
        confirm.save()
        return redirect("main:profile")
    return render(request, "deposit2.html", context)

def deposit(request):
    user = request.user
    context = {
        "user": user
    }
    if request.method == 'POST':
        amount = request.POST.get('amount')
        user = request.user
        new_deposit = Deposit.objects.create(user=user, amount=amount)
        new_deposit.save()
        return render(request, "deposit2.html", {"amount":amount})
    return render(request, "deposit.html", context)

def withdraw(request):
    user = request.user
    context = {
        "user": user
    }
    return render(request, "withdraw.html", context)

def history(request):
    user = request.user
    context = {
        "user": user
    }
    return render(request, "account-history.html", context)

def faq(request):
    user = request.user
    context = {
        "user": user
    }
    return render(request, "faq.html", context)

def support(request):
    user = request.user
    context = {
        "user": user
    }
    return render(request, "support.html", context)

def logout_view(request):
        logout(request)
        return redirect("main:home")

def active(request):
    return render(request, "active-depo.html")
