from django.shortcuts import render,redirect,HttpResponse
from .models import IncomeForm,Income

def add_income(request):
    if request.method=="POST":
        f=IncomeForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=IncomeForm
        context={'form':f}
        return render(request,'income.html',context)
