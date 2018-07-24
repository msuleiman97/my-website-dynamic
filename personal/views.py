from django.shortcuts import render

def index(request):
    return render(request,'personal/home.html')

def about(request):
    return render(request,'personal/about.html')


def services(request):
    return render(request,'personal/services.html')
def portfolio(request):
    return render(request,'personal/portfolio.html')

def contact(request):
    return render(request,'personal/contact.html')
