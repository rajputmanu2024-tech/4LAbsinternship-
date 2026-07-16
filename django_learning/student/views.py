from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from .models import *

def student_home(request):
    context = {
        "total_students": Student.objects.count(),
        "total_departments": Department.objects.count(),
        "total_subjects": Subject.objects.count(),
        "total_marks": SubjectMarks.objects.count(),
    }

    return render(request, "student/student_home.html", context)


def student_list(request):
    queryset = Student.objects.all()

    paginator = Paginator(queryset, 10)   

    page_number = request.GET.get("page")
    students = paginator.get_page(page_number)
    return render(request, 'student/student.html', {'students': students})