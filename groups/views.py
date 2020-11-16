from django.shortcuts import render, redirect
from .models import Group
from students.models import Student
from .forms import GroupForm
from django.http import Http404


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
    data = {}
    if not request.user.is_authenticated or not Group.objects.filter(id=id).exists():
        raise Http404
    group = Group.objects.get(id=id)
    if request.method == "GET":
        data['group'] = group
        return render(request, 'groups/delete.html', context=data)
    elif request.method == "POST":
        group.delete()
        return redirect('/groups/list')


def group_detail(request, id: int):
    data = {}
    # groups = Group.objects.filter(id=id)
    # print(groups)
    # if not groups.exists():
    if not Group.objects.filter(id=id).exists():
        raise Http404
    group = Group.objects.get(id=id)


    # Секция со студентами
    students = Student.objects.filter(group__id=group.id)
    print(students
    data['group'] = group
    data['students'] = students
    return render(request, 'groups/details.html', context=data)


def group_list(request):
    data = {}
    all_groups = Group.objects.all()
    data['groups'] = all_groups
    return render(request, 'groups/group_list.html', context=data)


def update_group(request, id: int):
    data = {}
    if not request.user.is_authenticated or not Group.objects.filter(id=id).exists():
        raise Http404
    group = Group.objects.get(id=id)
    data['group'] = group
    if request.method == "GET":
        group_form = GroupForm(instance=group)
        data['group_form'] = group_form
        return render(request, 'groups/update.html', context=data)
    elif request.method == "POST":
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            group.name = group_form.cleaned_data['name']
            group.about = '[EDITED] ' + group_form.cleaned_data['about']
            group.max_student = group_form.cleaned_data['max_student']
            group.is_evening_group = group_form.cleaned_data['is_evening_group']
            group.save()
        else:
            print('NOT VALID FORM!')

        return redirect('/groups/list')
