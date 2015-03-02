from django.contrib import messages

def process_transaction(user, other, credit):
    # TODO: process transaction
    messages.success(request, '&#1336;%d verzonden naar %s' % (credit, other))
