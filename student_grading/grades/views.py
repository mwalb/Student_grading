from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Result, Subject
import csv
import logging

# Get the logger you defined in settings.py
logger = logging.getLogger('activity')


def add_result(request):
    if request.method == "POST":
        student = Student.objects.get(id=request.POST['student'])
        subject = Subject.objects.get(id=request.POST['subject'])
        marks = request.POST['marks']

        Result.objects.create(
            student=student,
            subject=subject,
            marks=marks
        )

        # ✅ THIS is all you need
        logger.info(
            f"Result added | Student: {student.name} | Subject: {subject.name} | Marks: {marks}"
        )

        return redirect('student_list')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})


def student_results(request, id):
    results = Result.objects.filter(student_id=id)
    return render(request, 'results.html', {'results': results})


def export_results(request):
    # ✅ Log export event
    logger.info("Results exported to CSV")

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="results.csv"'

    writer = csv.writer(response)
    writer.writerow(['Student', 'Subject', 'Marks', 'Grade'])

    for r in Result.objects.all():
        writer.writerow([
            r.student.name,
            r.subject.name,
            r.marks,
            r.grade
        ])

    return response
