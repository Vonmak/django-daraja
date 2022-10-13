from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0791665710'
    amount = 1
    account_reference = 'Victor'
    transaction_desc = 'News'
    callback_url = "https://sandbox.safaricom.co.ke/mpesa/"
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)
