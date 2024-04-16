from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Products
from products.forms import ProductForm
# Create your views here.



def get_all_products(request):
    all_products = Products.objects.all()
    return render(request,'home.html',{'message':'django crud home page',"all_products":all_products})
    # return redirect('index')

    # return HttpResponse('this is our view function ')

def get_one_product(request,id):
    product = Products.objects.get(pk=id)
    return render(request,'home.html',{'message':'django single record fetch','all_products':[product]})
    # return HttpResponse('this is our get one  view function ')


def create_product(request):
    p_form = ProductForm(request.POST)
    if request.method == 'POST':
        # print(request.POST)
        if p_form.is_valid():
            p_form.save()
            return redirect('index')

    return render(request,'add.html',{'form':p_form,'message':'create product'})

    # return HttpResponse('this is our create product view function ')

def edit_products(request,id):
    prod = Products.objects.get(pk=id)
    print('****', prod)
    if prod:
        p_form = ProductForm(instance=prod)
        return render(request, 'edit.html',{'form':p_form,'message':'edit mode','pid':prod.id})
    return render(request,'home.html',{'message':'product not found', 'all_products':Products.object.all()})

def update_product(request,id):
    prod = Products.objects.get(pk=id)
    if prod:
        p_form = ProductForm(request.POST, instance=prod)
        p_form.save()
        return redirect('index')




    # return HttpResponse('this is our  edit view function ')

def delete_products(request,id):
    product = Products.objects.get(pk=id)
    product.delete()
    return redirect('index')
    # return HttpResponse('this is our delete view function ')