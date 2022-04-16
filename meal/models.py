from django.db import models
import datetime
from django.utils.timezone import localtime, now,localdate
from django.contrib.auth import get_user_model


class Meal(models.Model):
    meal_number     = models.IntegerField(verbose_name='meal number',default=0)
    guest_meal      = models.IntegerField(verbose_name='guest meal number',default=0)
    total_meal      = models.IntegerField(verbose_name='total meal number',default=0)
    date            = models.DateField(default=localdate())
    user            = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        unique_together = ('date', 'user',)
        constraints = [
                models.UniqueConstraint(fields=['date', 'user'], name='user_unique_day_meal')
        ]

    def __str__(self):
        return str(self.date)

    def save(self, *args, **kwargs):
        self.total_meal = self.meal_number + self.guest_meal
        super().save(*args, **kwargs)  # Call the "real" save() method.



class Expenses(models.Model):
    total_amount    = models.DecimalField(decimal_places=2,max_digits=9999,default=0)
    date            = models.DateField(default=localdate())
    user            = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return '%s-%s' % (self.id, self.date)



class Product(models.Model):
    name          = models.CharField(verbose_name="product name",max_length=20)
    quantity      = models.DecimalField(max_digits=40,decimal_places=3,help_text="quantity in kg/ltr",null=True,blank=True)
    amount        = models.DecimalField(decimal_places=2,max_digits=9999,help_text="amount in TK")
    date          = models.DateField(default=localdate())
    user          = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name



