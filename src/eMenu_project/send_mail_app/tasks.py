from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from eMenu import settings
import datetime
from django.db.models import Q
from api.models import Dish


@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    yesterday = datetime.date.fromordinal(
        datetime.date.today().toordinal()-1).strftime('%Y-%m-%d')
    dishes = Dish.objects.filter(Q(created=yesterday) | Q(updated=yesterday))
    for user in users:
        mail_subject = "Nowe dania"
        message = "Zapoznaj się nowymi/zmodyfikowanymi daniami:"
        for dish in dishes:
            message += '\n\r' + dish.name + '\n\r' + dish.description + '\n\r' + \
                'Cena: ' + dish.price + '\n\r' + 'Czas przygotowania: ' + dish.preparation_time

        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"
