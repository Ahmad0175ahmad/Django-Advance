from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string

# def send_test_email(request):
#     subject ="Welcome to my Blog"
#     message="Thank you for subscribing to my Blog!"
#     from_email="ahmadnew1818@gmail.com"
#     recipient_list=["ahmadbro175@gmail.com"]

#     send_mail(subject,message,from_email,recipient_list)
#     return HttpResponse("Test email send successfully")

def send_test_email(request):
    subject="Welcome to my Blog"
    message=render_to_string('email/welcome_email.html',{
        'username':'Ahmad',
        'course':'Django Tutorial',
    })

    email =EmailMessage(
        subject,
        message,
        "ahmadnew1818@gmail.com",
        ["ahmadbro175@gmail.com"]
    )
    email.content_subtype="html"  #Main content is now text/html
    email.send()
    return HttpResponse("Email send successfully!")

