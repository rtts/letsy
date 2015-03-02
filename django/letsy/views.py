from balance.models import Transaction
from balance.forms import TransactionForm
from balance.utils import process_transaction
from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated():
       return overview(request)
    else:
       return homepage(request)
  
def homepage(request):
    return render(request, 'home.html', {})

def overview(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            process_transaction(
                user   = request.user,
                other  = form.cleaned_data['beneficiary'],
                credit = form.cleaned_data['amount'],
                )
            return redirect('home')
    else:
        form = TransactionForm()

    transactions = Transaction.objects.filter(user=request.user) # .select_related('other')
    return render(request, 'overview.html', {
            'form': form,
            'transactions': transactions,
            })
