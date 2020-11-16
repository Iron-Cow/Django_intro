from django.shortcuts import render
from .models import Student


def students_details(request, group_id: int, student_id: int):
    student = Student.objects.get(group__id=group_id, id=student_id)
    data = {}
    data['student'] = student
    return render(request, 'students/students_details.html', data)

# Create your views here.
