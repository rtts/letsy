from django.db import models
from django.contrib.auth import get_user_model

class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    debit = models.IntegerField();
    credit = models.IntegerField();
    balance_before = models.IntegerField();
    balance_after = models.IntegerField();
    user = models.ForeignKey(get_user_model(), related_name='transactions');
    other = models.ForeignKey(get_user_model(), related_name='others_transactions');
    description = models.CharField(max_length=200);
    def __unicode__(self):
        return u'User: %s, other: %s, debit: \u0538%d, credit: \u0538%d' % (
            self.user, self.other, self.debit, self.credit)

