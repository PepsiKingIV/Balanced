from django.db import models

# Create your models here.

class debit(models.Model):
    user_id = models.CharField(max_length=30)
    date = models.DateField()
    categoty = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'
    
    
class credit(models.Model):
    user_id = models.CharField(max_length=30)
    date = models.DateField()
    categoty = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    priority = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'