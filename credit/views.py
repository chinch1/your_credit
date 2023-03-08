from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from credit.forms import CreditForm
from credit.models import Credit
from client.models import Client

# Create your views here.


def showCredit(request, pk):
    credit = Credit.objects.get(id=pk)
    context = {'credit': credit}
    return render(request, 'credit/credit_show.html', context)


def listCredits(request):
    credits = Credit.objects.all()
    context = {'credits': credits}
    return render(request, 'credit/credit_list.html', context)


def createCredit(request):
    form = CreditForm()

    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            form.save()

            # Fetching the client id from the form
            # client_id = request.POST['client']
            # client = Client.objects.get(id=client_id)

            # Sending email to the client
            # email_to = client.email
            # email_subject = 'Credit created'
            # email_body = 'You created a credit'
            # email_from = settings.EMAIL_HOST_USER
            # send_mail(email_subject, email_body, email_from,
            #           [email_to], fail_silently=False)

            return redirect('/credit/list')

    context = {'form': form}
    return render(request, 'create_form.html', context)
