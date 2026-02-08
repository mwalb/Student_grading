from django.contrib import admin
from .models import Student, Subject, Result


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'reg_no')
    search_fields = ('name', 'reg_no')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks', 'grade')
    list_filter = ('subject',)
    search_fields = ('student__name',)
