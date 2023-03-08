from client.forms import ClientForm
from client.models import Client
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.


def home(request):
    return render(request, 'client/home.html')


def listClients(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'client/client_list.html', context)


def createClient(request):
    form = ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/client/list')

    context = {'form': form}
    return render(request, 'create_form.html', context)


def updateClient(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/client/list')

    context = {'form': form}
    return render(request, 'create_form.html', context)


def deleteClient(request, pk):
    client = Client.objects.get(id=pk)
    client.delete()
    return HttpResponseRedirect(reverse('list_client'))
