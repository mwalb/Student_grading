from django.shortcuts import render
from .models import Student,Result


def student_list(request):
  students=Student.objects.all()
  return render(request,'students.html',{'students':students})

def student_results(request,id):
  results=Result.objects.filter(student_id=id)
  return render(request,'results.html',{'results':results})

