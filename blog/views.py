from django.shortcuts import render, HttpResponseRedirect

# Home
def home(request):
    return render(request, 'blog/home.html')

# About
def about(request):
    return render(request, 'blog/about.html')

# Contact
def contact(request):
    return render(request, 'blog/contact.html')

# Dashboard
def dashboard(request):
    return render(request, 'blog/dashboard.html')

# LogIn
def LogIn(request):
    return render(request, 'blog/login.html')

# SignUp
def SignUp(request):
    return render(request, 'blog/signup.html')

# LogOut
def user_logout(request):
    return HttpResponseRedirect('/')
