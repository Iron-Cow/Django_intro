from django.shortcuts import render, redirect
from .models import Group
from .forms import GroupForm


def index(request):
    return render(request, 'groups/index.html')


def create_group(request):
    data = {}
    if request.method == "GET":
        group_form = GroupForm()
        data['group_form'] = group_form
        return render(request, 'groups/create.html', context=data)
    elif request.method == "POST":
        group_form = GroupForm(request.POST)
        group_form.save()
        return redirect('/groups/list')


def delete_group(request, id: int):
    return render(request, 'groups/delete.html')


def group_detail(request, id: int):
    return render(request, 'groups/details.html')


def group_list(request):
    data = {}
    all_groups = Group.objects.all()

    data['groups'] = all_groups
    return render(request, 'groups/group_list.html', context=data)


def update_group(request, id: int):
    return render(request, 'groups/update.html')

