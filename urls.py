from django.urls import path
from .views import student_list, add_student, delete_student, student_detail, add_marks

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('add/', add_student, name='add_student'),
    path('delete/<int:student_id>/', delete_student, name='delete_student'),
    path('student/<int:student_id>/', student_detail, name='student_detail'),
    path('student/<int:student_id>/add-marks/', add_marks, name='add_marks'),
]
