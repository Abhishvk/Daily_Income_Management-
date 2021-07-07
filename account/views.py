from django.shortcuts import render,redirect,HttpResponse
from .models import UserInfoForm
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        f=UserInfoForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserInfoForm
        context={'form':f}
        return render(request,'register.html',context)

from django.contrib.auth import login,logout,authenticate
def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("<h1> InValid UserName and Password</h1>")
    else:
        return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')