from django.shortcuts import render
from django.http import HttpResponse
from .forms import Customer_Form 
from .models import Menu_lemon

def check():
    return HttpResponse("Hello World")


def home_1(request):
    return render(request, 'home_1.html')

def about_1(request):
    return render(request, 'about_1.html')

def menu_1(request):
    return render(request, 'menu_1.html')

# def book_1(request):
#     return render(request)

# def form_view(request):
#     form = DemoForm()

#     context = {'form': form}
#     return render(request, 'home.html', context)

def get_cm_info(request):
    form = Customer_Form()
    if request.method == 'POST':
        form = Customer_Form(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'home.html',  context)


def about_littlelemon(request): 
    context = {'about' : ' This resturant is focus in seafood and mainly fresh seafood with no harm to human life and bectriea'}
    return render(request, 'about.html' , context)


def index(request):
    context = {'name':'Muhammad Alfateh'}
    return render(request, 'index.html', context)

def menu(request):
    menu_dic = {'menu': [
        {'name':'Biryni', 'price':'80'},
        {'name':'Tikka', 'price':'270'},
        {'name':'Zinger', 'price':'200'},
        {'name':'Fries', 'price':'50'},
        {'name':'Chicken', 'price':'720'}
    ]}
    return render(request, 'menu.html', menu_dic)


def menu_byid(request):
    all_menu = Menu_lemon.objects.all()
    context = {'menu': all_menu}
    return render(request, 'menu_id.html', context)

