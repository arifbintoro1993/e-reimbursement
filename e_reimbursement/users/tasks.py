from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail

from celery import shared_task


@shared_task(bind=True, max_retries=5)
def send_email_created_user_info(self, username, password, email):
    try:
        msg_subject = 'E-reimbursemet login information'
        msg_recipient = email
        msg_plain = render_to_string(
            'email/email.html',
            {'username': username, 'password': password, 'email': email}
        )
        send_mail(msg_subject, msg_plain, settings.DEFAULT_FROM_EMAIL, [msg_recipient], html_message=msg_plain,)

    except Exception as e:
        print(e)
        self.retry(countdown=2 ** self.request.retries)
