from django.db import models

# Create your models here.
from django.urls import reverse

PaymentStatus = (
    (1, 'Waiting'),
    (2, 'Confirmed'),
    (3, 'Refunded'),
)


class Payment(models.Model):

    number = models.CharField('number', max_length=50, db_index=True)
    date = models.DateTimeField('date', auto_now_add=False)
    amount = models.DecimalField('amount', max_digits=9, decimal_places=2, default='0.0')
    purpose_of_payment = models.TextField('purpose of payment', max_length=150)
    status = models.IntegerField(choices=PaymentStatus, default=1)

    def __str__(self):
        return "Payments №{}".format(self.number)

    def get_update_url(self):
        return reverse('payment_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('payment_delete_url', kwargs={'id':self.id})


