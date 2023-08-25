from django.db import models

class userСategories(models.Model):
    user_id = models.CharField(max_length=30, name='user_id')
    telegram_id = models.CharField(max_length=30, name='telegram_id')
    category = models.JSONField(name='category')
    
    def __str__(self) -> str:
        return self.user_id
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
