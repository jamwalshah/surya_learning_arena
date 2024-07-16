from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict={
        'product1':'Mac',
        'product2':'iPhone',
        'product3':'Dell',
        'heading':'Electronics Aisle',
        'logo':'Electronics.jpg'
    }
    return render(request=request, template_name='productApp/products.html', context=product_dict)

def toys(request):
    product_dict={
        'product1':'Remote Car',
        'product2':'Drone',
        'product3':'Rocket Launcher',
        'heading':'Toys Aisle',
        'logo':'Toys.jpg'
    }
    return render(request=request, template_name='productApp/products.html', context=product_dict)

def shoes(request):
    product_dict={
        'product1':'Nike',
        'product2':'Adidas',
        'product3':'Reebok',
        'heading':'Shoes Aisle',
        'logo':'Shoes.jpg'
    }
    return render(request=request, template_name='productApp/products.html', context=product_dict)

def index(request):
    return render(request=request, template_name='productApp/index.html')