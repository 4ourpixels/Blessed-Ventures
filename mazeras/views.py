from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

from .forms import *
# Create your views here.


def index(request):
    page = "| Home"
    stones = Stone.objects.all()
    projects = Project.objects.all()
    uncut_mazeras = UncutMazeras.objects.all()
    cut_mazeras = CutMazeras.objects.all()

    context = {
        'page': page,
        'stones': stones,
        'projects': projects,
        'uncut_mazeras': uncut_mazeras,
        'cut_mazeras': cut_mazeras,
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


def edit(request, id):
    if request.method == "POST":
        stone = Stone.objects.get(pk=id)
        form = StoneForm(request.POST, instance=stone)
        if form.is_valid():
            form.save()
            return render(request, 'mazeras/edit.html', {
                'form': form,
                'success': True
            })
    else:
        stone = Stone.objects.get(pk=id)
        form = StoneForm(instance=stone)
    return render(request, 'mazeras/edit.html', {
        'form': form,
    })


def delete(request, id):
    if request.method == 'POST':
        stone = Stone.objects.get(pk=id)
        stone.delete()
    return HttpResponseRedirect(reverse('index'))

# Project Functions


def view_project(request, id):
    project = Project.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project_name = form.cleaned_data['name']
            new_project_description = form.cleaned_data['description']
            new_project_location = form.cleaned_data['location']
            new_project_stones = form.cleaned_data['stones']
            new_project_created_at = form.cleaned_data['created_at']
            new_project_status = form.cleaned_data['status']

            new_project = Project(
                name=new_project_name,
                description=new_project_description,
                location=new_project_location,
                stones=new_project_stones,
                created_at=new_project_created_at,
                status=new_project_status,
            )
            new_project.save()

            return render(request, 'mazeras/new_project.html', {
                'form': ProjectForm(),
                'success': True,
            })
        else:
            form = ProjectForm()
    return render(request, 'mazeras/new_project.html', {
        'form': ProjectForm()
    })


def edit_project(request, id):
    project = Project.objects.get(pk=id)
    if request.method == "POST":
        project = Project.objects.get(pk=id)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return render(request, 'mazeras/edit_project.html', {
                'form': form,
                'success': True
            })
    else:
        project = Project.objects.get(pk=id)
        form = ProjectForm(instance=project)
    return render(request, 'mazeras/edit_project.html', {
        'form': form,
    })


def delete_project(request, id):
    if request.method == 'POST':
        project = Project.objects.get(pk=id)
        project.delete()
    return HttpResponseRedirect(reverse('index'))


def dashboard(request):
    stones = Stone.objects.all()
    projects = Project.objects.all()

    context = {
        'stones': stones,
        'projects': projects,
    }

    return render(request, 'mazeras/dashboard.html', context)


def mazeras(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }

    return render(request, 'mazeras/mazeras.html', context)


def thetap(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }

    return render(request, 'mazeras/thetap.html', context)


def add_uncut_mazeras(request):
    if request.method == 'POST':
        form = UncutMazerasForm(request.POST)
        if form.is_valid():
            new_stone_name = form.cleaned_data['name']
            new_stone_price = form.cleaned_data['price']

            new_stone = UncutMazeras(
                name=new_stone_name,
                price=new_stone_price,
            )
            new_stone.save()

            return render(request, 'mazeras/add_uncut_mazeras.html', {
                'form': UncutMazerasForm(),
                'success': True,
            })
        else:
            form = UncutMazerasForm()
    return render(request, 'mazeras/add_uncut_mazeras.html', {
        'form': UncutMazerasForm()
    })


def edit_uncut_mazeras(request, id):
    if request.method == "POST":
        stone = UncutMazeras.objects.get(pk=id)
        form = UncutMazerasForm(request.POST, instance=stone)
        if form.is_valid():
            form.save()
            return render(request, 'mazeras/edit_uncut_mazeras.html', {
                'form': form,
                'success': True
            })
    else:
        stone = UncutMazeras.objects.get(pk=id)
        form = UncutMazerasForm(instance=stone)
    return render(request, 'mazeras/edit_uncut_mazeras.html', {
        'form': form,
    })


def add_cut_mazeras(request):
    if request.method == 'POST':
        form = CutMazerasForm(request.POST)
        if form.is_valid():
            new_stone_name = form.cleaned_data['name']
            new_stone_price = form.cleaned_data['price']

            new_stone = CutMazeras(
                name=new_stone_name,
                price=new_stone_price,
            )
            new_stone.save()

            return render(request, 'mazeras/add_cut_mazeras.html', {
                'form': CutMazerasForm(),
                'success': True,
            })
        else:
            form = CutMazerasForm()
    return render(request, 'mazeras/add_cut_mazeras.html', {
        'form': CutMazerasForm()
    })


def edit_cut_mazeras(request, id):
    if request.method == "POST":
        stone = CutMazeras.objects.get(pk=id)
        form = CutMazerasForm(request.POST, instance=stone)
        if form.is_valid():
            form.save()
            return render(request, 'mazeras/edit_cut_mazeras.html', {
                'form': form,
                'success': True
            })
    else:
        stone = CutMazeras.objects.get(pk=id)
        form = CutMazerasForm(instance=stone)
    return render(request, 'mazeras/edit_cut_mazeras.html', {
        'form': form,
    })


def view_uncut_mazeras(request, id):
    uncut = UncutMazeras.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def view_cut_mazeras(request, id):
    cut = CutMazeras.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def delete_uncut_mazeras(request, id):
    if request.method == 'POST':
        uncut = UncutMazeras.objects.get(pk=id)
        uncut.delete()
    return HttpResponseRedirect(reverse('index'))


def delete_cut_mazeras(request, id):
    if request.method == 'POST':
        cut = CutMazeras.objects.get(pk=id)
        cut.delete()
    return HttpResponseRedirect(reverse('index'))
