from bank.forms import BankForm
from bank.models import Bank
from django.shortcuts import render, redirect

# Create your views here.


def showBank(request, pk):
    bank = Bank.objects.get(id=pk)
    context = {'bank': bank}
    return render(request, 'bank/bank_show.html', context)


def listBanks(request):
    banks = Bank.objects.all()
    context = {'banks': banks}
    return render(request, 'bank/bank_list.html', context)


def createBank(request):
    form = BankForm()

    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bank/list')

    context = {'form': form}
    return render(request, 'create_form.html', context)
