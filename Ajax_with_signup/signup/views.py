
from django.http import request
from django.shortcuts import render
from .models import User
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def signup(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email']) 
            msg = "Email Already Register"
            return render(request,'index.html',{'msg':msg})
        except:
            User.objects.create(
                fname=request.POST['fname'],
                lname=request.POST['lname'],
                email=request.POST['email'],
                mobile=request.POST['mobile'],
                address=request.POST['address'],

            )
            msg="sign up suucessfully"
            return render(request,'index.html',{'msg':msg})
    else:
        return render(request,'index.html ')        

def validate_email(request):
    email=request.GET.get('email',None)
    data={
        'is_taken':User.objects.filter(email__iexact=email).exists()
    }
    return  JsonResponse(data)
