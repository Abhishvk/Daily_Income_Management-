from django.shortcuts import render,redirect
from .models import Expense,ExpenseForm
def add_expense(request):
    if request.method=='POST':
        return redirect('/')
    else:
        f=ExpenseForm
        context={'form':f}
        return render(request,'expense.html',context)