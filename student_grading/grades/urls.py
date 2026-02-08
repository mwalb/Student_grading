from django.urls import path
from . import views

urlpatterns=[
  path('',views.student_list),
  path('results/<int:id>',views.student_results),
]