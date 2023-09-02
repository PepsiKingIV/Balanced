from django.db import models
from django.conf import settings


def get_default_something():
    return {"debit": [], "credit": []}


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email_verify = models.BooleanField(default=False)
    number_of_emails = models.IntegerField(default=0)
    telegram_id = models.CharField(max_length=30, name="telegram_id", default=0)
    category = models.JSONField(default=get_default_something)

    def __str__(self):
        return self.user.username
