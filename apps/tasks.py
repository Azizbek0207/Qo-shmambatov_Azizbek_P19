# from celery import shared_task
# from django.core.mail import send_mail
# from django.http import HttpResponse

#
# from apps.models import Email
# from root import settings
#
#
# @shared_task
# def send_message(msg):
#     emails = Email.objects.values_list('email', flat=True)
#     for email in emails:
#         send_mail('python', msg, settings.EMAIL_HOST_USER, [email])
#     return f'Ketti'
