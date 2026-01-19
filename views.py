from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {
        'students': students
    })

from django.shortcuts import redirect

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        course = request.POST['course']

        Student.objects.create(
            name=name,
            email=email,
            age=age,
            course=course
        )
        return redirect('student_list')

    return render(request, 'students/add_student.html')

from django.shortcuts import get_object_or_404

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')

from .models import Student

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    marks = student.marks.all()  
    return render(request, 'students/student_detail.html', {
        'student': student,
        'marks': marks
    })

# from django.shortcuts import render, get_object_or_404
# from .models import Student

# def student_detail(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     return render(request, 'students/student_detail.html', {'student': student})


from django.shortcuts import render, get_object_or_404
from .models import Student, Marks
from django.db.models import Avg, Sum

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    marks = student.marks.all()

    total_marks = marks.aggregate(Sum('score'))['score__sum'] or 0
    average_marks = marks.aggregate(Avg('score'))['score__avg'] or 0
    average_marks = round(average_marks, 2)

    if average_marks >= 75:
        progress_color = "#4caf50"   # green
    elif average_marks >= 50:
        progress_color = "#ff9800"   # orange
    else:
        progress_color = "#f44336"   # red

    return render(request, "students/student_detail.html", {
        "student": student,
        "marks": marks,
        "total_marks": total_marks,
        "average_marks": average_marks,
        "progress_color": progress_color,
    })


from .models import Student, Marks
from django.shortcuts import redirect

def add_marks(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        test_name = request.POST.get("test_name")
        score = request.POST.get("score")

        Marks.objects.create(
            student=student,
            test_name=test_name,
            score=score
        )

        return redirect('student_detail', student_id=student.id)

    return render(request, 'students/add_marks.html', {'student': student})


