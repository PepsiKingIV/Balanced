from django.db import models
from django.conf import settings

class userСategories(models.Model):
    user_id = models.CharField(max_length=30, name='user_id')
    telegram_id = models.CharField(max_length=30, name='telegram_id')
    category = models.JSONField()
    
    def __str__(self) -> str:
        return self.user_id
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    email_verify = models.BooleanField(default=False)
    number_of_emails = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username