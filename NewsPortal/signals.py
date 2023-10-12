from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import PostCategory
from .config import send_notifications


@receiver(m2m_changed, sender=PostCategory)
def notif_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categoty.all()
        sub_emails = []
        subscribers = []

        for cat in categories:
            subscribers += cat.subscribers.all()
            sub_emails += [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.title, sub_emails)


