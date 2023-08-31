from django.db import models


# Create your models here.

class data(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=30)
    date = models.CharField()
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'

    def record(form):
        try:
            if data.objects.exists():
                record = data.objects.order_by('-id').all()[0]
                new_id = record.id + 1
            else:
                new_id = 1
            data.objects.create(
                id=new_id,
                user_id=form['user_id'],
                date=form['date'],
                category=form['category'],
                amount=form['amount'])
            return True
        except Exception as e:
            print(e)
            return False

    def delete(request):
        try:
            id = int(request['record_id'])
            data.objects.filter(id=id).delete()
            return True
        except:
            return False


class credit(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=30)
    date = models.CharField()
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    priority = models.IntegerField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'

    def record(form):
        try:
            if credit.objects.exists():
                record = credit.objects.order_by('-id').all()[0]
                new_id = record.id + 1
            else:
                new_id = 1
            credit.objects.create(
                id = new_id,
                user_id=form['user_id'],
                date=form['date'],
                category=form['category'],
                amount=form['amount'],
                priority=form['priority'])
            return True
        except:
            return False

    def delete(request):
        try:
            id = int(request['record_id'])
            credit.objects.filter(id=id).delete()
            return True
        except:
            return False
