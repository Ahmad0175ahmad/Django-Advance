from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        print(f"New user created: {instance.username}")

        subject="Welcome to Muhammad Ahmad!"
        message=f"Hi {instance.username}, thankyou for registering at Muhammad Ahmad"
        from_email="ahmadnew1818@gmail.com"
        recipient_list=[instance.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        print(f"welcome email sent successfully")
