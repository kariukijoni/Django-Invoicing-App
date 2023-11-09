from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import *
from .models import *
from django.http import HttpResponse

from django.contrib.auth.models import User, auth
from random import randint
from uuid import uuid4

#Anonymous required
def anonymous_required(function=None, redirect_url=None):
   if not redirect_url:
       redirect_url = 'dashboard'

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous,
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator


def index(request):
    context = {}
    return render(request, 'invoices/index.html', context)

# @anonymous_required
def login(request):
    context = {}
    if request.method == 'GET':
        form = UserLoginForm()
        context['form'] = form
        return render(request, 'invoices/login.html', context)

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            return redirect('dashboard')
        else:
            context['form'] = form
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'invoices/login.html', context)


@login_required
def dashboard(request):
    context = {}
    return render(request, 'invoices/dashboard.html', context)

@login_required
def invoices(request):
    context = {}
    return render(request, 'invoices/invoices.html', context)

@login_required
def products(request):
    context = {}
    return render(request, 'invoices/products.html', context)

@login_required
def clients(request):
    context = {}
    clients = Client.objects.all()
    context['clients'] = clients

    if request.method == 'GET':
        form = ClientForm()
        context['form'] = form
        return render(request, 'invoices/clients.html', context)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, 'New Client Added')
            return redirect('clients')
        else:
            messages.error(request, 'Problem processing your request')
            return redirect('clients')

    return render(request, 'invoices/clients.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required
def create_invoice(request):
    # create a blank invoice
    number='INV-'+str(uuid4()).split('-')[1]
    new_invoice=Invoice.objects.create(number=number)
    new_invoice.save()

    invoice=Invoice.objects.get(number=number)

    return redirect('create-build-invoice',slug=invoice.slug)  



@login_required
def create_build_invoice(request,slug):

    # fetch invoice
    try:
        invoice=Invoice.objects.get(slug=slug)
        pass
    except:
        messages.error(request,'Something went wrong')
        return redirect('invoices')

    # fetch all products related to invoice
    products=Product.objects.filter(product_invoice=invoice)

    context={
        'invoice':invoice,
        'products':products
    }

    if request.method=='GET':
        prod_form=ProductForm()
        inv_form=InvoiceForm(instance=invoice)

        context={
            'prod_form':prod_form,
            'inv_form':inv_form
        }

        return render(request,'invoices/create-invoice.html',context)

    return render(request,'invoices/create-invoice.html',context)

