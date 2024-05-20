from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy


@shared_task
def send_password_reset_email(user_email, reset_url):
	subject = 'Password Reset Request'
	message = f'Please click on the link below to reset your password:\n{reset_url}'
	sender_email = settings.EMAIL_HOST_USER
	recipient_list = [user_email]

	send_mail(subject, message, sender_email, recipient_list)


@shared_task
def send_password_reset_urls(user_email):
	base_url = 'http://127.0.0.1.com'
	password_reset_url = reverse_lazy("accounts:password_reset")
	reset_url = f'{base_url}{password_reset_url}'

	send_password_reset_email.delay(user_email, reset_url)

	password_reset_done_url = reverse_lazy("accounts:password_reset_done")
	reset_done_url = f'{base_url}{password_reset_done_url}'
	send_password_reset_email.delay(user_email, reset_done_url)
