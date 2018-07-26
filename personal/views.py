from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
from tkinter import messagebox

def index(request):
    return render(request,'personal/home.html')

def about(request):
    return render(request,'personal/about.html')


def services(request):
    return render(request,'personal/services.html')
def portfolio(request):
    return render(request,'personal/portfolio.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        phone =request.POST.get("phone")
        email=request.POST.get("email")
        message=request.POST.get("message")
        #email to ourself the submitted contact message
        subject='Contact Form Received' 
        from_email= settings.DEFAULT_FROM_EMAIL
        to_email=[settings.DEFAULT_FROM_EMAIL]
        
        #format
        context={
            'user':name,
            'email':email,
            'message':message
        }
        contact_message=get_template('contact_message.txt').render(context)
        send_mail(subject,contact_message, from_email,to_email, fail_silently=True)
        messagebox.showinfo("Thank you ", "your message  been succussfully received .")
        return redirect("/contact/")
    return render(request,'personal/contact.html')



    
            
            