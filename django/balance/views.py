from balance.models import Transaction
from balance.forms import TransactionForm
from django.contrib.auth.decorators import login_required

@login_required
def new_transaction(request):
