from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

from .forms import StoneForm
# Create your views here.


def index(request):
    page = "| Home"
    stones = Stone.objects.all()
    projects = Project.objects.all()

    context = {
        'page': page,
        'stones': stones,
        'projects': projects,
    }
    return render(request, 'mazeras/index.html', context)


def view_stone(request, id):
    stone = Stone.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def add(request):
    if request.method == 'POST':
        form = StoneForm(request.POST)
        if form.is_valid():
            new_stone_name = form.cleaned_data['name']
            new_stone_description = form.cleaned_data['description']
            new_stone_price = form.cleaned_data['price']
            new_stone_stock = form.cleaned_data['stock']

            new_stone = Stone(
                name=new_stone_name,
                description=new_stone_description,
                price=new_stone_price,
                stock=new_stone_stock,
            )
            new_stone.save()

            return render(request, 'mazeras/add.html', {
                'form': StoneForm(),
                'success': True,
            })
        else:
            form = StoneForm()
    return render(request, 'mazeras/add.html', {
        'form': StoneForm()
    })
