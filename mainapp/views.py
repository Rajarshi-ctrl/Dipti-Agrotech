from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')

def detail(request):
    return render(request, 'detail.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        messages.success(request, 'Thanks for your message. We will get in touch soon.')

    return render(request, 'contact.html')

def userlogin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are successfully Logged In.')
        else:
            messages.warning(request, "Your credentials doesn't match with our database.")

    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']

            if password == password2:
                myuser = User.objects.create_user(name, email, password)
                myuser.save()

                messages.success(request, 'You are successfully Registered...')
            else:
                messages.warning(request, 'Password is not same. Please check It.')
        except:
            messages.error(request, 'Username is already taken. Please use something else.')

    return render(request, "login.html")

def userlogout(request):
    logout(request)
    messages.success(request, 'You are successfully Logged Out...')
    return render(request, "index.html")
