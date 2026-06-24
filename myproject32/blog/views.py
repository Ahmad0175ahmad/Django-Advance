from django.shortcuts import render
from django.core.mail import send_mass_mail
from django.http import HttpResponse
# Create your views here.
def send_bulk_email(request):
    messages1=('Welcome User 1','Hello User 1, Welcome to our platform','ahmadnew1818@gmail.com',['ahmadbro175@gmail.com'])
    messages2=('Welcome User 2','Hello User 2, Welcome to our platform','ahmadnew1818@gmail.com',['ahmadbro175@gmail.com'])
    
    send_mass_mail((messages1,messages2),fail_silently=False)
    return HttpResponse("Bulk emails sent successfully")
