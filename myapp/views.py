from django.shortcuts import render, redirect
from .models import Contact, order
from .forms import FormContact, formsOrder

def index(request):
    context = {
        'form1': FormContact(),
    }
    return render(request, 'index.html', context)

def send_contact(request):
    if request.POST:
        form1 = FormContact(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/#contact')
        return redirect('/#contact')   

def product(request):
    context = {
        'form2': formsOrder(),
    }
    return render(request, 'product.html', context)

def send_order(request):
    if request.POST:
        form2 = formsOrder(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('product')
        return redirect('product')
    