from django.shortcuts import render

# Create your views here.

from credit.forms import CreditForm
from credit.models import Credit
from django.shortcuts import render, redirect

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
            return redirect('/credit/list')

    context = {'form': form}
    return render(request, 'create_form.html', context)
