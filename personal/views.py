from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
from .forms import ContactForm

def index(request):
    return render(request,'personal/home.html')

def about(request):
    return render(request,'personal/about.html')


def website_template(request):
    return render(request,'personal/website-template.html')

def dynamic_website(request):
    return render(request,'personal/dynamic-website.html')
def digital_marketing(request):
    return render(request,'personal/digital-marketing.html')

def blog(request):
    return render(request,'personal/blog.html')

def contact(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        form_email=form.cleaned_data.get('email')
        form_message=form.cleaned_data.get('message')
        form_first_name=form.cleaned_data.get('first_name')
        form_last_name=form.cleaned_data.get('last_name')

        subject= 'Mail From Your Website'
        from_email= settings.EMAIL_HOST_USER
        to_email=[from_email, 'm.suleiman1997@gmail.com']

        contact_message= "%s: %s via %s"%(
            form_first_name,
            form_last_name,
            form_message,
            form_email)
        some_html_message= """
          <h1>Hello </h1>
          """
        send_mail(subject,
                  contact_message,
                  form_email,
                  to_email,
                  fail_silently=False)


    context={
        "form": form,
        }

    return render(request,'personal/contact.html')





