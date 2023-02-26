from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Signup
# Create your views here.

def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is homepage")
    
def about(request):
    return HttpResponse("this is aboutpage")
    
    
def services(request):
    return HttpResponse("this is servicepage")

def signup(request):
    if request.method== "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        signup  = Signup(name=name,email=email,password=password)
        signup.save()
        # messages.success(request, 'Successfully SignedUp')
    return render(request,'signin.html')

def login(request):
    return render(request,'login.html')




