from django.urls import path
from .views import students_details

urlpatterns = [
    path('<int:group_id>/student/<int:student_id>', students_details, name='students_details'),
]



